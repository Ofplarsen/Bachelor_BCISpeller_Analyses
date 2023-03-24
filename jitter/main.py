import time

import numpy as np
import pandas as pd
from numpy.random import rand
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet, pylsl, local_clock
from sklearn.cross_decomposition import CCA

help_string = 'SendData.py -s <sampling_rate> -n <stream_name> -t <stream_type>'
channels = ['Fp1', 'Fz', 'F3', 'F7', 'F9', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'Pz', 'P3', 'P7'
            , 'P9', 'O1', 'Oz', 'O2', 'P10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'C4', 'Cz'
            , 'FC2', 'FC6', 'F10', 'F8', 'F4', 'Fp2', 'ACC_X', 'ACC_Y', 'ACC_Z']
removed_channels = ['Fp1', 'F8', 'F7', 'Fp2', 'F3', 'F4']
frequencies_main = ['8.18', '9', '10', '11.25', '12.85', '15']
frequencies = ['8.18_sin_h1','8.18_cos_h1','8.18_sin_h2','8.18_cos_h2','8.18_sin_h3','8.18_cos_h3',
               '9_sin_h1', '9_cos_h1','9_sin_h2', '9_cos_h2','9_sin_h3', '9_cos_h3',
               '10_sin_h1','10_cos_h1','10_sin_h2','10_cos_h2','10_sin_h3','10_cos_h3',
               '11.25_sin_h1','11.25_cos_h1','11.25_sin_h2','11.25_cos_h2','11.25_sin_h3','11.25_cos_h3',
               '12.85_sin_h1','12.85_cos_h1','12.85_sin_h2','12.85_cos_h2','12.85_sin_h3','12.85_cos_h3',
               '15_sin_h1', '15_cos_h1', '15_sin_h2', '15_cos_h2', '15_sin_h3', '15_cos_h3'
               ]
fs = 250  # Sampling frequency
fragment_duration = 5  # Fragment duration in seconds
fragment_samples = fs * fragment_duration

# Create an LSL stream
stream_name = 'CCA'
stream_type = 'cca'
channel_count = 1
sampling_rate = 0  # Irregular sampling rate (use a positive number for a regular sampling rate)
channel_format = 'float32'

# Create the stream info object
info = StreamInfo(stream_name, stream_type, channel_count, sampling_rate, channel_format, 'myuid34234')

# Create the LSL outlet
outlet = StreamOutlet(info)


# Resolve an LSL stream on the network
print("Looking for an LSL stream...")
streams = resolve_stream('type', 'Test')
inlet = StreamInlet(streams[0])


def perform_cca(fragment, n_components):
    X = fragment[:][['O1', 'O2', 'Oz', 'P3', 'P4', 'Pz', 'P7', 'P8']]
    freqs = []
    t = 0
    for i in range(0, len(frequencies), 6):
        t = t + 1
        Y = fragment[:][frequencies[i:6 * t]]
        #print(Y.shape)
        ca = CCA(n_components=1)
        ca.fit(X, Y)
        X_c, Y_c = ca.transform(X, Y)
        #print([np.corrcoef(X_c[:, i], Y_c[:, i])[0, 1] for i in range(1)])
        freqs.append(np.corrcoef(X_c[:, 0], Y_c[:, 0])[0][1])
    return freqs

def return_index(index, info, outlet):
    # Send a single value
    value = float(index)
    timestamp = time.time()
    outlet.push_sample([value], timestamp)

buffer = []

print("now sending data...")

while True:
    # Receive data from the LSL stream
    sample, timestamp = inlet.pull_sample()

    # Append the received sample to the buffer
    buffer.append(sample)
    val = -1
    if len(buffer) >= fragment_samples:
        # Convert the buffer to a NumPy array and reshape it
        fragment = np.array(buffer[:fragment_samples])

        # Process the 5-second fragment here (e.g., apply a filter, analyze, or save it)
        print("Received a 5-second fragment:", fragment)
        # Remove the processed fragment from the buffer
        buffer = buffer[fragment_samples:]
        df = pd.DataFrame(fragment)
        df.columns = frequencies + channels
        cca = perform_cca(df,1)
        print(cca)
        val = np.argmax(cca)
        print(val)
        return_index(val, info, outlet)