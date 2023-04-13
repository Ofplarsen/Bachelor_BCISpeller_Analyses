import time
from pylsl import StreamInfo, StreamOutlet, local_clock

# Create a StreamInfo instance for the marker stream
marker_info = StreamInfo('Markers', 'Markers', 1, 0)

# Create a StreamOutlet for the marker stream
marker_outlet = StreamOutlet(marker_info)

# Send a marker with a timestamp
marker = 1

while True:
    # Alternatively, send a marker without a timestamp (LSL will add a timestamp automatically)
    marker_outlet.push_sample([marker])

    # Wait for a while before closing the stream
    time.sleep(5)
