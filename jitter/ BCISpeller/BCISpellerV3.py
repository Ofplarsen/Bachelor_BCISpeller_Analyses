import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import rand
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet, pylsl, local_clock
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


def normalize_data(data, lower_bound=-1, upper_bound=1):
    min_value = data.min()
    max_value = data.max()
    normalized_data = lower_bound + (data - min_value) * (upper_bound - lower_bound) / (max_value - min_value)
    return normalized_data


def plot_single(df, column):
    t = np.arange(0, 10, 1 / fs)
    #df[column] = normalize_data(df[column])
    axis = plt.subplot()
    axis.plot(t[:len(df[column])], df[column])
    axis.set_title(column)
    plt.show()


def init_stream():
    # Create an LSL stream
    stream_name = 'CCA'
    stream_type = 'cca'
    channel_count = 1
    sampling_rate = 0  # Irregular sampling rate (use a positive number for a regular sampling rate)
    channel_format = 'float32'

    # Create the stream info object
    info = StreamInfo(stream_name, stream_type, channel_count, sampling_rate, channel_format, 'cca')

    # Create the LSL outlet
    outlet = StreamOutlet(info)
    return info, outlet


def get_freqs(N):
    start_time = time.time()
    # fs = [8.18, 9, 10, 11.25, 12.86, 15]
    fs = [13.0909, 14.4, 16, 18, 20.5714, 24]
    t = N / 250
    return_freqs = []
    for fk in fs:
        for i in range(1, 4):
            return_freqs.append(np.sin(2 * np.pi * i * (t * fk)).tolist())
            return_freqs.append(np.cos(2 * np.pi * i * (t * fk)).tolist())

    df = pd.DataFrame(return_freqs)
    df = df.T
    df.columns = frequencies
    print("--- %s seconds ---" % (time.time() - start_time))
    return df


def perform_cca(fragment, n_components):
    X = fragment[:][occ_channels]
    freqs = []
    t = 0
    for i in range(0, len(frequencies), 6):
        t = t + 1
        Y = fragment[:][frequencies[i:6 * t]]
        ca = CCA(n_components=2)
        ca.fit(X, Y)
        X_c, Y_c = ca.transform(X, Y)
        freqs.append(np.corrcoef(X_c[:, 0], Y_c[:, 0])[0][1])
    return freqs

def perform_cca_2(fragment):
    n_components = 2
    X = fragment[:][occ_channels]
    freqs = []
    t = 0
    for i in range(0, len(frequencies), 6):
        t = t + 1
        Y = fragment[:][frequencies[i:6 * t]]
        ca = CCA(n_components=n_components)
        ca.fit(X, Y)
        X_c, Y_c = ca.transform(X, Y)
        p1 = np.corrcoef(X_c[:, 0], Y_c[:, 0])[0][1]
        p2 = np.corrcoef(X_c[:, 1], Y_c[:, 1])[0][1]
        freqs.append(np.sqrt(p1**2+p2**2))
    return freqs


def return_index(index, info, outlet):
    # Send a single value
    value = float(index)
    timestamp = time.time()
    outlet.push_sample([value], timestamp)


def zero_phase_butter(data):
    # Butterworth filter parameters
    fs = 250
    lowcut = 12.0
    highcut = 25.0
    order = 3

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


info, outlet = init_stream()
print("Looking for an LSL stream...")
streams = resolve_stream('type', 'Speller')
inlet = StreamInlet(streams[0])

fs = 250  # Sampling frequency
fragment_duration = 4  # Fragment duration in seconds
fragment_samples = fs * fragment_duration
pre_trigger_samples = fs * 1
target_value = 0
delay = round(fs*0.14)

while True:
    buffer = []
    triggered = False
    start_time = None
    scan_values = False
    count = False
    i = 0
    while not triggered:
        sample, timestamp = inlet.pull_sample()
        buffer.append(sample)

        # Remove old samples from the buffer
        while len(buffer) > fragment_samples:
            buffer.pop(0)
        # print(sample[0])
        # Check if the current sample value is different from target_value
        if sample[0] != target_value and not scan_values:
            print("Deleting buffer")
            print(sample[0])
            del buffer[:-1]
            print(len(buffer))
            scan_values = True

        if scan_values and len(buffer) == delay and not count:
            print("Shifting for visual system delay")
            del buffer[:-1]
            count = True

        if count and sample[0] == target_value:
            i += 1

        if count and scan_values and (len(buffer) == fragment_samples or (i == delay)) :
            print(len(buffer))
            fragment = np.array(buffer[:fragment_samples])
            triggered = True
            print("Fragment: found")
            # Convert the buffer to a NumPy array and reshape it
            fragment = np.array(fragment)
            # Remove the processed fragment from the buffer
            # buffer = buffer[fragment_samples:]
            df = pd.DataFrame(fragment)
            df.columns = ['N'] + channels
            start_time = time.time()
            plot_single(df, 'O1')
            df[occ_channels] = df[occ_channels].apply(lambda x: notch(x))
            plot_single(df, 'O1')
            df[occ_channels] = df[occ_channels].apply(lambda x: zero_phase_butter(x))
            plot_single(df, 'O1')
            print("--- Filter time:  %s seconds ---" % (time.time() - start_time))
            N = np.arange(1, len(df['O1']) + 1)
            df = pd.concat([df, get_freqs(N)], axis=1, join='inner')
            plot_single(df, '8.18_sin_h1')
            df.columns = ['N'] + frequencies + channels
            cca = perform_cca(df, 1)
            print(df['N'])
            print(cca)
            index = np.argmax(cca)
            print(index)
            print(np.argpartition(cca, -2)[-2:])
            return_index(index, info, outlet)
