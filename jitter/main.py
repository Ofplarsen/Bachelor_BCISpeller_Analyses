import pyxdf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Blink:
    def __init__(self, timestamp, index):
        self.timestamp = timestamp
        self.index = index


def get_time_stamps(stamps: list):
    start = []
    end = []
    more_than_one = False

    for i in range(len(stamps)):
        if i == (len(stamps)-1):
            break

        if(stamps[i] == (stamps[i+1] - 1)):
            if not more_than_one:
                start.append(stamps[i])
            more_than_one = True
            continue
        else:
            if more_than_one:
                end.append(stamps[i])
                more_than_one = False

    return start, end


data, header = pyxdf.load_xdf('data/data18022023/eeg-and-eyetracking.xdf')
eeg, header_egg = pyxdf.load_xdf('data/LSLData2/LSLData/raw-eeg.xdf')

left_blinks = None
right_blinks = None
both_blink = None
for stream in data:
    y = stream['time_series']
    blinking_df = pd.DataFrame(y)
    blinking_df.rename(index={3: "left", 4: "right", 5: "both"})
    blinking_df.drop([0, 1, 2], inplace=True, axis=1)

    print(blinking_df)
    left_blinks = blinking_df.index[(blinking_df[3] >= 1) & (blinking_df[4] != 1)].tolist()
    right_blinks = blinking_df.index[(blinking_df[4] >= 1) & (blinking_df[3] != 1)].tolist()
    both_blink = blinking_df.index[blinking_df[5] == 1].tolist()
    print(left_blinks)
    pass
channels = ['Fp1', 'Fz', 'F3', 'F7', 'F9', 'FC5', 'FC1', 'C3', 'T7', 'CP5', 'CP1', 'Pz', 'P3', 'P7'
            , 'P9', 'O1', 'Oz', 'O2', 'P10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'C4', 'Cz'
            , 'FC2', 'FC6', 'F10', 'F8', 'F4', 'Fp2', 'AUX_1', 'AUX_2']
removed_channels = ['Fp1', 'F8', 'F7', 'Fp2', 'F3', 'F4']


start, end = get_time_stamps(right_blinks)
print(start, end)
rang = 50
for stream in eeg:
    for j in range(len(start)):
        y = stream['time_series']
        blinking_df = pd.DataFrame(y)
        blinking_df = blinking_df[start[j] - rang:end[j] + rang]
        #print(blinking_df.info())
        blinking_y = blinking_df.to_numpy()
        index = 0
        for i in range(32):
            index += 1
            if channels[i] in removed_channels:
                index -= 1
            else:
                axis = plt.subplot(7, 4, index)
                axis.axvline(stream['time_stamps'][start[j]], color='red')  # y = 0
                axis.axvline(stream['time_stamps'][end[j]], color='red')
                axis.plot(stream['time_stamps'][start[j]-rang:end[j]+rang], blinking_df[blinking_df.columns[i]])
                axis.set_title(channels[i])

        plt.show()





