import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet, local_clock

# LSL EEG Stream parameters
num_channels = 35
sampling_rate = 500
channel_format = 'float32'
eeg_stream_name = 'MockEEG'
eeg_stream_type = 'EEG'

# Create LSL Stream
eeg_info = StreamInfo(eeg_stream_name, eeg_stream_type, num_channels, sampling_rate, channel_format)
eeg_outlet = StreamOutlet(eeg_info)

# LSL Eye Tracking stream
sample_stream_name = 'MockN'
sample_stream_type = 'MockN'
sample_channels = 1

# Create LSL stream
sample_info = StreamInfo(sample_stream_name, sample_stream_type, sample_channels, sampling_rate, channel_format)
sample_outlet = StreamOutlet(sample_info)

duration = 6     # Signal duration (s)
base_frequency = 24  # Frequency of mock signal (Hz)
noise_amplitude = 50  # Noise amplitude
t = np.arange(0, duration, 1/sampling_rate)
eeg_channel = np.sin(2 * np.pi * base_frequency * t) + noise_amplitude * np.random.randn(len(t))

start_time = local_clock()
channels = [11, 12, 13, 14, 15, 16, 18, 19]
while True:
    t = np.arange(0, duration, 1/sampling_rate)
    sample_value = 0  # The value N for the single sample stream
    eeg_data = []

    for ch in range(num_channels):
        eeg_channel = np.sin(2 * np.pi * base_frequency * t) + noise_amplitude * np.random.randn(len(t))
        eeg_data.append(eeg_channel)

    # Transpose the data for correct format
    eeg_data = np.array(eeg_data).T

    # Stream Mock EEG data and Eye Tracking data
    x = 0
    for sample in eeg_data:
        if x % 2 == 0: # Every other N (250 hz frequency)
            sample_value = sample_value + 1
            sample_outlet.push_sample([sample_value])

        # Every N (500 hz Frequency)
        eeg_outlet.push_sample(sample)
        x = x+1
        time.sleep(1 / sampling_rate)

