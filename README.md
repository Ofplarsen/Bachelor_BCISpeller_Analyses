# Bachelor's Thesis

This project contains three different parts of William G. Tresselt and Olav F. P. Larsen's bachelor's thesis. 
The initial task was to synchronize an eye tracker and an EEG. The data was streamed using LabStreamingLayer (LSL)

## Synchronization of the EEG and Eye Tracker

This was done to enable other research that wants to explore the combination of these two technologies.
The analysis was done by applying a zero-phase ButterWorth filter to an EMG signal (EMG was synchronized with the EEG) recording a subject's blink,
and aligning the peak with the start of the eyes being fully closed, which the eye tracker recorded. This was then done multiple times (200+). The STD and mean
offset were then computed and adjusted when using the equipment combined.

## jitter/BCISpeller

After the equipment was synchronized, the group decided to prove the precision of the synchronization, by creating a BCI Speller. This Speller was created in Unity
and the repo is also uploaded to GitHub. The BCI Speller utilized SSVEP, eye tracking, and VR. The eye tracker was used in combination with clusters of letters. Only the letters
inside the cluster the subject was looking at, were flickering. This allowed the group to only use 6 frequencies in the speller, compared to one for each letter which is common
in traditional SSVEP spellers, instead of hybrid solutions. The VR environment was used to make the cluster with the letters "fly" toward the subject when looking at it. 

The EEG signal was filtered using zero-phase Butterworth, and a CCA was used to compare the EEG signal with the different target frequencies, to determine what frequency the
subject was looking at. The index of the frequency with the highest correlation was then streamed from the script also using LSL.

### 2DVEP
The 2DVEP folder contains a C program, which splits the PC screen into four different squares that flickers at different frequencies. This can be set by injecting arguments to the
program when running it from the terminal.

## Pipelines

The Pipelines folder contains the different NeuroPype pipelines used in the project. NeuroPype was slowly removed from the pipeline, due to the lack of documentation.
The group instead implemented the needed functionality using Python. 
