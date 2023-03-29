import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet

# Define the LSL stream parameters
num_channels = 35
sampling_rate = 250
channel_format = 'float32'
stream_name = 'MockEEG'
stream_type = 'EEG'

# Create the LSL stream info and outlet
info = StreamInfo(stream_name, stream_type, num_channels, sampling_rate, channel_format)
outlet = StreamOutlet(info)

# Define the signal generation parameters
duration = 6  # Duration of each segment of the signal (seconds)
base_frequency = 24  # Frequency of the sinusoidal components (Hz)
noise_amplitude = 0.5  # Amplitude of the random noise component

# Continuously generate and stream mock EEG data
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
        outlet.push_sample(sample)
        time.sleep(1/sampling_rate)
