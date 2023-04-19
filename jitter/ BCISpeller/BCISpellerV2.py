import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import rand
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet, pylsl, local_clock
from sklearn.cross_decomposition import CCA

channels = ['Fp1', 'Fz', 'F3', 'F7', 'F9', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'Pz', 'P3', 'P7'
            , 'P9', 'O1', 'Oz', 'O2', 'P10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'C4', 'Cz'
            , 'FC2', 'FC6', 'F10', 'F8', 'F4', 'Fp2', 'ACC_X', 'ACC_Y', 'ACC_Z']
removed_channels = ['Fp1', 'F8', 'F7', 'Fp2', 'F3', 'F4']
frequencies_main = [4,5,6,7,9,11]
frequencies = ['8.18_sin_h1','8.18_cos_h1','8.18_sin_h2','8.18_cos_h2','8.18_sin_h3','8.18_cos_h3',
               '9_sin_h1', '9_cos_h1','9_sin_h2', '9_cos_h2','9_sin_h3', '9_cos_h3',
               '10_sin_h1','10_cos_h1','10_sin_h2','10_cos_h2','10_sin_h3','10_cos_h3',
               '11.25_sin_h1','11.25_cos_h1','11.25_sin_h2','11.25_cos_h2','11.25_sin_h3','11.25_cos_h3',
               '12.85_sin_h1','12.85_cos_h1','12.85_sin_h2','12.85_cos_h2','12.85_sin_h3','12.85_cos_h3',
               '15_sin_h1', '15_cos_h1', '15_sin_h2', '15_cos_h2', '15_sin_h3', '15_cos_h3'
               ]
occ_channels = ['O1', 'O2', 'Oz', 'P3', 'P4', 'Pz', 'P7', 'P8']
def init_stream():
    # Create an LSL stream
    stream_name = 'CCA2'
    stream_type = 'cca2'
    channel_count = 1
    sampling_rate = 1  # Irregular sampling rate (use a positive number for a regular sampling rate)
    channel_format = 'float32'

    # Create the stream info object
    info = StreamInfo(stream_name, stream_type, channel_count, sampling_rate, channel_format, 'cca')

    # Create the LSL outlet
    outlet = StreamOutlet(info)
    return info, outlet

def plot_single(df, column):
    t = np.arange(0, 10, 1 / fs)
    axis = plt.subplot()
    axis.plot(t[:len(df[column])], df[column])
    axis.set_title(column)
    plt.show()

def get_freqs(N):
    start_time = time.time()
    #fs = [8.18, 9, 10, 11.25, 12.86, 15]
    #fs = [13.0909, 14.4, 16, 18, 20.5714, 24]
    #fs = [13, 14, 16, 18, 20, 24]
    fs = frequencies_main
    t = N/250
    return_freqs = []
    for fk in fs:
        for i in range(1,4):
            return_freqs.append(np.sin(2*np.pi*i * (t*fk)).tolist())
            return_freqs.append(np.cos(2*np.pi*i * (t*fk)).tolist())

    df = pd.DataFrame(return_freqs)
    df = df.T
    df.columns = frequencies
    print("--- %s seconds ---" % (time.time() - start_time))
    return df

def perform_cca(fragment, n_components):
    X = fragment[:][occ_channels]#,
    freqs = []
    t = 0
    for i in range(0, len(frequencies), 6):
        t = t + 1
        Y = fragment[:][frequencies[i:6 * t]]
        #print(frequencies[i:6*t])
        ca = CCA(n_components=1)
        ca.fit(X, Y)
        X_c, Y_c = ca.transform(X, Y)
        coef = np.corrcoef(X_c[:, 0], Y_c[:, 0])
        #print(np.corrcoef(X_c[:,1], Y_c[:, 1]))
        freqs.append(coef[0][1])
        #print(coef)
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


info, outlet = init_stream()
print("Looking for an LSL stream...")
streams_counter = resolve_stream('type', 'DejitteredSpeller')
streams_eeg = resolve_stream('type', 'ButterEEG')
inlet = StreamInlet(streams_counter[0])
inlet_2 = StreamInlet(streams_eeg[0])


fs = 250  # Sampling frequency
delay = 0.061
fragment_duration = 4+delay  # Fragment duration in seconds
print(fragment_duration)
fragment_samples = round(fs * fragment_duration)
pre_trigger_samples = fs * 1
target_value = 0



while True:
    buffer = []
    buffer_eeg = []
    triggered = False
    start_time = None

    while not triggered:
        # Gets data from the Eye Tracker LSL stream, and the EEG LSL stream
        sample, timestamp = inlet.pull_sample()
        sample_eeg, timestamp_eeg = inlet_2.pull_sample()
        buffer.append(sample)
        buffer_eeg.append(sample_eeg)

        # Remove old samples from the buffer

        while len(buffer) > fragment_samples:
            buffer.pop(0)
            buffer_eeg.pop(0)

        # If buffer is filled with data ready to be compared in CCA, and the start of the buffer is the start of
        # the Eye Tracking data (Eye Tracking trigger)
        if (len(buffer) == fragment_samples) and buffer[0][0] == 1 and buffer[0][fragment_samples-round(delay*fs)] <= 0:
            print(len(buffer))
            fragment = np.array(buffer[:fragment_samples])
            fragment_eeg = np.array(buffer_eeg[:fragment_samples])

            triggered = True
            print("Fragment: found")

            # Makes both streams to a single dataframe
            df = pd.concat([pd.DataFrame(np.array(fragment)), pd.DataFrame(np.array(fragment_eeg))], axis=1, join='inner')

            # If any delay added, shift signal accordingly
            df['N'] = df['N'].shift(round(delay * fs))
            df = df.iloc[round(delay * fs):]
            # Reset the index
            df = df.reset_index(drop=True)
            N = df['N']
            print(df.shape)
            df = pd.concat([df, get_freqs(N)], axis=1, join='inner')
            print(df.shape)
            print([(index, row['O1']) for index, row in df.iterrows() if pd.isna(row['O1'])])


            N = df['N']
            frs = get_freqs(N)
            X = df[:][occ_channels]
            freqs = []
            h = 0
            # CCA on the target frequencies, and the occular channels
            for y in range(0, len(frequencies), 6):
                h = h + 1
                Y = frs[:][frequencies[y:6 * h]]
                ca = CCA(n_components=2)
                ca.fit(X, Y)
                X_c, Y_c = ca.transform(X, Y)
                # Uses two coefficients pk = sqrt(p1**2+p2*'2)
                p1 = np.corrcoef(X_c[:, 0], Y_c[:, 0])[0][1]
                p2 = np.corrcoef(X_c[:, 1], Y_c[:, 1])[0][1]
                freqs.append(np.sqrt(p1 ** 2 + p2 ** 2))
            cca = freqs
            # print("CCA single: " + str(perform_cca(df,1)))
            print(cca)
            index = np.argmax(cca)
            print("Looking at: " + str(frequencies_main[index]) + "Hz")
            # Sends result in LSL stream
            return_index(index, info, outlet)

