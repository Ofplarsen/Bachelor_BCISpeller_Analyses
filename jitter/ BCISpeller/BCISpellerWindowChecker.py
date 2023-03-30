import sys

import pandas as pd
import numpy as np
from pylsl import resolve_stream, StreamInlet
from scipy import signal
from sklearn.cross_decomposition import CCA

channels = ['Fp1', 'Fz', 'F3', 'F7', 'F9', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'Pz', 'P3', 'P7'
    , 'P9', 'O1', 'Oz', 'O2', 'P10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'C4', 'Cz'
    , 'FC2', 'FC6', 'F10', 'F8', 'F4', 'Fp2', 'ACC_X', 'ACC_Y', 'ACC_Z']
removed_channels = ['Fp1', 'F8', 'F7', 'Fp2', 'F3', 'F4']
frequencies_main = ['8.18', '9', '10', '11.25', '12.85', '15']
occ_channels = ['O1', 'O2', 'Oz', 'P3', 'P4', 'Pz', 'P7', 'P8']
frequencies = ['8.18_sin_h1', '8.18_cos_h1', '8.18_sin_h2', '8.18_cos_h2', '8.18_sin_h3', '8.18_cos_h3',
               '9_sin_h1', '9_cos_h1', '9_sin_h2', '9_cos_h2', '9_sin_h3', '9_cos_h3',
               '10_sin_h1', '10_cos_h1', '10_sin_h2', '10_cos_h2', '10_sin_h3', '10_cos_h3',
               '11.25_sin_h1', '11.25_cos_h1', '11.25_sin_h2', '11.25_cos_h2', '11.25_sin_h3', '11.25_cos_h3',
               '12.85_sin_h1', '12.85_cos_h1', '12.85_sin_h2', '12.85_cos_h2', '12.85_sin_h3', '12.85_cos_h3',
               '15_sin_h1', '15_cos_h1', '15_sin_h2', '15_cos_h2', '15_sin_h3', '15_cos_h3'
               ]

def add_padding(data, lenght=100):
    return padding(data, lenght)

def remove_padding(data, length=100):
    return data.iloc[length:-length].reset_index(drop=True)

def padding(data, pad_length = 100):
    return np.pad(data, (pad_length, pad_length), mode="reflect")

def zero_phase_butter(data):
    # Butterworth filter parameters
    fs = 250
    lowcut = 1
    highcut = 15
    order = 10

    # Design Butterworth bandpass filter
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b_bandpass, a_bandpass = signal.butter(order, [low, high], btype="band")

    # Zero-phase filtering using filtfilt
    return signal.filtfilt(b_bandpass, a_bandpass, data)


def notch(data):
    fs = 250.0  # Sample frequency (Hz)
    f0 = 50.0  # Frequency to be removed from signal (Hz)
    Q = 30.0  # Quality factor
    # Design notch filter
    b_notch, a_notch = signal.iirnotch(f0, Q, fs)
    return signal.lfilter(b_notch, a_notch, data)

def get_freqs(N):
    # fs = [8.18, 9, 10, 11.25, 12.86, 15]
    #fs = [13.0909, 14.4, 16, 18, 20.5714, 24]
    #fs = [13, 14, 16, 18, 20, 24]
    fs = [4,5,6,7,10,13]
    t = N / 250
    return_freqs = []
    for fk in fs:
        for i in range(1, 4):
            return_freqs.append(np.sin(2 * np.pi * i * (t * fk)).tolist())
            return_freqs.append(np.cos(2 * np.pi * i * (t * fk)).tolist())

    df = pd.DataFrame(return_freqs)
    df = df.T
    df.columns = frequencies
    return df

def cca_placeholder(X, N_s):
    freqs = []
    h = 0
    for y in range(0, len(frequencies), 6):
        h = h + 1
        Y = N_s[:][frequencies[y:6 * h]]
        ca = CCA(n_components=2)
        ca.fit(X, Y)
        X_c, Y_c = ca.transform(X, Y)
        p1 = np.corrcoef(X_c[:, 0], Y_c[:, 0])[0][1]
        p2 = np.corrcoef(X_c[:, 1], Y_c[:, 1])[0][1]
        freqs.append(np.sqrt(p1 ** 2 + p2 ** 2))
    return freqs


streams_counter = resolve_stream('type', 'DejitteredSpeller')
streams_eeg = resolve_stream('type', 'DEEG')
inlet = StreamInlet(streams_counter[0])
inlet_2 = StreamInlet(streams_eeg[0])
fs = 250  # Sampling frequency
fragment_duration = 15  # Fragment duration in seconds
fragment_samples = fs * fragment_duration
pre_trigger_samples = fs * 1
target_value = 0
delay = round(fs*0.01)
pad_length = 100
set_N = round(fragment_samples / 3)
while True:
    buffer = []
    buffer_eeg = []
    triggered = False
    start_time = None
    scan_values = False
    count = False
    target = 0
    i = 0
    while not triggered:
        sample, timestamp = inlet.pull_sample()
        sample_eeg, timestamp_eeg = inlet_2.pull_sample()
        buffer.append(sample)
        buffer_eeg.append(sample_eeg)
        # Remove old samples from the buffer
        while len(buffer) > fragment_samples:
            buffer.pop(0)
            buffer_eeg.pop(0)

        if (len(buffer) == fragment_samples):
            print(len(buffer))
            fragment = np.array(buffer[:fragment_samples])
            fragment_eeg = np.array(buffer_eeg[:fragment_samples])
            triggered = True
            print("Fragment: found")

            df = pd.concat([pd.DataFrame(np.array(fragment)), pd.DataFrame(np.array(fragment_eeg))], axis=1, join='inner')
            df.columns = ['N'] + channels

            df = df.apply(lambda x: add_padding(x, pad_length))
            df[occ_channels] = df[occ_channels].apply(lambda x: notch(x))
            df[occ_channels] = df[occ_channels].apply(lambda x: zero_phase_butter(x))
            df = df.apply(lambda x: remove_padding(x, pad_length))

            #N = df['N']
            start = set_N
            N = df['N'][start:start+6*fs]
            frs = get_freqs(N)
            start = 0
            highest = None
            while fragment_samples - start > 6*fs:
                cca_ = cca_placeholder(X =df[start:start+6*fs][occ_channels], N_s =frs)
                cca = cca_[target]
                if highest is None or cca > highest[1]:
                    print(cca_)
                    highest = (start, cca)
                    print(highest)
                    print(np.argpartition(cca_, -2)[-2:])
                start = start+ 1

            print(highest)
            print(fragment_samples)
            print(highest[0]-start)
            print(highest[0] - (N.eq(1).cumsum() == 1).idxmax())
            sys.exit()
