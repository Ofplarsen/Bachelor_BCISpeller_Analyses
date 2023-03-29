import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet

# Define the LSL stream parameters for the EEG stream
num_channels = 8
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
duration = 7  # Duration of each segment of the signal (seconds)
base_frequency = 24  # Frequency of the sinusoidal components (Hz)
noise_amplitude = 50  # Amplitude of the random noise component
sample_value = 0  # The value N for the single sample stream

# Continuously generate and stream mock EEG data and the single sample value
while True:
    t = np.arange(0, duration, 1/sampling_rate)
    eeg_data = []

    for ch in range(num_channels):
        eeg_channel = np.sin(2 * np.pi * base_frequency * t) + noise_amplitude * np.random.randn(len(t))
        eeg_data.append(eeg_channel)

    # Transpose the data to match the expected format (time x channels)
    eeg_data = np.array(eeg_data).T

    # Stream the generated mock EEG data
    for sample in eeg_data:
        sample_value = sample_value + 1
        eeg_outlet.push_sample(sample)
        sample_outlet.push_sample([sample_value])  #
