import pyxdf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data, header = pyxdf.load_xdf('data/LSLData2/LSLData/gaze-and-blinking.xdf')
eeg, header_egg = pyxdf.load_xdf('data/LSLData2/LSLData/raw-eeg.xdf')

for stream in eeg:
    y = stream['time_series']

    blinking_df = pd.DataFrame(y)
    blinking_df.drop([0,1,2], inplace=True, axis=1)
    print(blinking_df.info)
    blinking_y = blinking_df.to_numpy()
    figure, axis = plt.subplots(2, 2)
    axis[0, 0].plot(stream['time_stamps'], blinking_df[blinking_df.columns[0]])
    axis[0, 0].set_title("Left eye blink")

    axis[0, 1].plot(stream['time_stamps'], blinking_df[blinking_df.columns[1]])
    axis[0, 1].set_title("Right eye blink")

    axis[1, 0].plot(stream['time_stamps'], blinking_df[blinking_df.columns[2]])
    axis[1, 0].set_title("Both eye blink")
    # numeric data, draw as lines

plt.ylim(0, 3)
plt.show()