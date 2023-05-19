import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import rand
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet, pylsl, local_clock
from scipy import signal
from sklearn.cross_decomposition import CCA
# EEG channels used
channels = ['Fp1', 'Fz', 'F3', 'F7', 'F9', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'Pz', 'P3', 'P7'
    , 'P9', 'O1', 'Oz', 'O2', 'P10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'C4', 'Cz'
    , 'FC2', 'FC6', 'F10', 'F8', 'F4', 'Fp2', 'ACC_X', 'ACC_Y', 'ACC_Z']

# Channels where electrodes are removed from EEG
removed_channels = ['Fp1', 'F8', 'F7', 'Fp2', 'F3', 'F4']

#The frequencies used for the SSVEP speller
#frequencies_main = [4,5,6,7,9,11]
frequencies_main = [4,5,5.5,6,7,7.4]
#frequencies_main = [8.18,9,10,11.25,12.86,15]

#The channels used for the BCI Speller combined with CCA
occ_channels = ['O1', 'O2', 'Oz', 'P3', 'P4', 'Pz', 'P7', 'P8']

#Names of all frequencies with harmonics being used

frequencies = ['8.18_sin_h1', '8.18_cos_h1', '8.18_sin_h2', '8.18_cos_h2', '8.18_sin_h3', '8.18_cos_h3',
               '9_sin_h1', '9_cos_h1', '9_sin_h2', '9_cos_h2', '9_sin_h3', '9_cos_h3',
               '10_sin_h1', '10_cos_h1', '10_sin_h2', '10_cos_h2', '10_sin_h3', '10_cos_h3',
               '11.25_sin_h1', '11.25_cos_h1', '11.25_sin_h2', '11.25_cos_h2', '11.25_sin_h3', '11.25_cos_h3',
               '12.85_sin_h1', '12.85_cos_h1', '12.85_sin_h2', '12.85_cos_h2', '12.85_sin_h3', '12.85_cos_h3',
               '15_sin_h1', '15_cos_h1', '15_sin_h2', '15_cos_h2', '15_sin_h3', '15_cos_h3'
               ]

"""
Method to normalise data, to better fit plotting
"""
def normalize_data(data, lower_bound=-1, upper_bound=1):
    min_value = data.min()
    max_value = data.max()
    normalized_data = lower_bound + (data - min_value) * (upper_bound - lower_bound) / (max_value - min_value)
    return normalized_data

"""
Method to plot a single EEG channel
"""
def plot_single(df, column):
    t = np.arange(0, 10, 1 / fs)
    #df[column] = normalize_data(df[column])
    axis = plt.subplot()
    axis.plot(t[:len(df[column])], df[column])
    axis.set_title(column)
    plt.show()

"""
Method to initialise the output stream for streaming the CCA answerser via LSL
"""
def init_stream():
    # Create an LSL stream
    stream_name = 'CCA'
    stream_type = 'cca'
    channel_count = 1
    sampling_rate = 1  # Irregular sampling rate (use a positive number for a regular sampling rate)
    channel_format = 'float32'

    # Create the stream info object
    info = StreamInfo(stream_name, stream_type, channel_count, sampling_rate, channel_format, 'cca')

    # Create the LSL outlet
    outlet = StreamOutlet(info)
    return info, outlet
"""
Methods to add/remove padding, and formula for padding
Used when filtering the EEG signal, because of distortion at the start and end of EEG signal when using other filters
"""
def add_padding(data, lenght=100):
    return padding(data, lenght)

def remove_padding(data, length=100):
    return data.iloc[length:-length].reset_index(drop=True)

def padding(data, pad_length = 100):
    return np.pad(data, (pad_length, pad_length), mode="reflect")

"""
Method for return a dataframe with all frequencies used for comparison in the CCA method with the different EEG signals
N: Number of samples (seconds * frequency)
"""
def get_freqs(N):
    start_time = time.time()
    # fs = [8.18, 9, 10, 11.25, 12.86, 15]
    #fs = [13.0909, 14.4, 16, 18, 20.5714, 24]
    #fs = [13, 14, 16, 18, 20, 24]
    fs = frequencies_main
    #fs = [7, 6, 5, 4, 10, 13]
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

"""
Method that performs CCA between the EEG signal and the frequencies
Uses only a single coefficient from CCA
"""
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
"""
Method that performs CCA between the EEG signal and the frequencies
Uses two correlation coefficients from CCA
"""
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

"""
Method to send value in the output LSL stream used in the unity Speller
"""
def return_index(index, info, outlet):
    # Send a single value
    value = float(index)
    timestamp = time.time()
    outlet.push_sample([value], timestamp)

"""
Method to apply a zero-phase Butterworth filter to the data
Uses bandpass [1-15], and order 3
"""
def zero_phase_butter(data):
    # Butterworth filter parameters
    fs = 250
    lowcut = 1.0
    highcut = 15.0
    order = 3

    # Design Butterworth bandpass filter
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b_bandpass, a_bandpass = signal.butter(order, [low, high], btype="band")

    # Zero-phase filtering using filtfilt
    return signal.filtfilt(b_bandpass, a_bandpass, data)

"""
Method to apply a notch filter to EEG data
"""
def notch(data):
    fs = 250.0  # Sample frequency (Hz)
    f0 = 50.0  # Frequency to be removed from signal (Hz)
    Q = 30.0  # Quality factor
    # Design notch filter
    b_notch, a_notch = signal.iirnotch(f0, Q, fs)
    return signal.lfilter(b_notch, a_notch, data)


info, outlet = init_stream()
print("Looking for an LSL stream...")
streams_counter = resolve_stream('type', 'DejitteredSpeller')
streams_eeg = resolve_stream('type', 'DEEG')
inlet = StreamInlet(streams_counter[0]) #LSL Eyetracker data
inlet_2 = StreamInlet(streams_eeg[0])# LSL EEG data

fs = 250  # Sampling frequency
delay = 0.160 #Occular delay
#delay = 0.00 #Occular delay

fragment_duration = 6+delay  # Fragment duration in seconds

fragment_samples = round(fs * fragment_duration)


pad_length = 100 #Padding length (padding in filtering)
while True:
    buffer = []
    buffer_eeg = []
    triggered = False
    start_time = None #To track time

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


        if (len(buffer) == fragment_samples) and buffer[0][0] == 1:
            if (buffer[fragment_samples - round(delay * fs) - 1][0] != (fragment_samples - round(delay * fs))):
                print("Found invalid stare")
                continue

            fragment = np.array(buffer[:fragment_samples])
            fragment_eeg = np.array(buffer_eeg[:fragment_samples])
            triggered = True
            print("Fragment: found")

            # Makes both streams to a single dataframe
            df = pd.concat([pd.DataFrame(np.array(fragment)), pd.DataFrame(np.array(fragment_eeg))], axis=1, join='inner')

            df.columns = ['N'] + channels


            start_time = time.time()
            # Adds padding to the signals
            df = df.apply(lambda x: add_padding(x, pad_length))

            # Adds Notch filter to the occular channels
            df[occ_channels] = df[occ_channels].apply(lambda x: notch(x))
            #Adds Butterworth filter to the occular channels
            df[occ_channels] = df[occ_channels].apply(lambda x: zero_phase_butter(x))
            # Removes padding from signal
            df = df.apply(lambda x: remove_padding(x, pad_length))


            print("--- Filter time:  %s seconds ---" % (time.time() - start_time))


            df['N'] = df['N'].shift(round(delay * fs))
            df = df.iloc[round(delay * fs):]
            # Reset the index
            df = df.reset_index(drop=True)
            N = df['N']

            df = pd.concat([df, get_freqs(N)], axis=1, join='inner')

            #print([(index, row['O1']) for index, row in df.iterrows() if pd.isna(row['O1'])])
            #print(df)
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
                freqs.append(p1)
                #p2 = np.corrcoef(X_c[:, 1], Y_c[:, 1])[0][1]
                #freqs.append(np.sqrt(p1 ** 2 + p2 ** 2))
            cca = freqs
            #print("CCA single: " + str(perform_cca(df,1)))
            print(cca)
            index = np.argmax(cca)
            print("Looking at: " + str(frequencies_main[index]) + "Hz")
            #Sends result in LSL stream
            return_index(index, info, outlet)
