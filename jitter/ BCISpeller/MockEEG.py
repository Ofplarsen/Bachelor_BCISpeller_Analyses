import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet, local_clock

# Define the LSL stream parameters
num_channels = 35
sampling_rate = 500
channel_format = 'float32'
eeg_stream_name = 'MockEEG'
eeg_stream_type = 'EEG'

# Create the LSL stream info and outlet for the EEG stream
eeg_info = StreamInfo(eeg_stream_name, eeg_stream_type, num_channels, sampling_rate, channel_format)
eeg_outlet = StreamOutlet(eeg_info)

# Define the LSL stream parameters for the single sample stream
sample_stream_name = 'MockN'
sample_stream_type = 'MockN'
sample_channels = 1

# Create the LSL stream info and outlet for the single sample stream
sample_info = StreamInfo(sample_stream_name, sample_stream_type, sample_channels, sampling_rate, channel_format)
sample_outlet = StreamOutlet(sample_info)

# Define the signal generation parameters
duration = 6     # Duration of each segment of the signal (seconds)
base_frequency = 24  # Frequency of the sinusoidal components (Hz)
noise_amplitude = 50  # Amplitude of the random noise component


# Continuously generate and stream mock EEG data and the single sample value
start_time = local_clock()
channels = [11, 12, 13, 14, 15, 16, 18, 19]
while True:
    t = np.arange(0, duration, 1/sampling_rate)
    sample_value = 0  # The value N for the single sample stream
    eeg_data = []

    for ch in range(num_channels):
        eeg_channel = np.sin(2 * np.pi * base_frequency * t) + noise_amplitude * np.random.randn(len(t))
        eeg_data.append(eeg_channel)

    # Transpose the data to match the expected format (time x channels)
    eeg_data = np.array(eeg_data).T

    # Stream the generated mock EEG data
    x = 0
    for sample in eeg_data:
        if x % 2 == 0:
            sample_value = sample_value + 1
            sample_outlet.push_sample([sample_value])

        eeg_outlet.push_sample(sample)
        x = x+1
        time.sleep(1 / sampling_rate)

