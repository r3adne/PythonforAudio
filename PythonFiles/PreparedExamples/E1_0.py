# E1 Problem 0
# loading audio files using librosa

import librosa



# This is the format which librosa.io.load() uses. It takes most audio file types and loads them at sampling rate sr. The mono=True option sums L and R if it's a stereo file.
#
# samples, sr = librosa.core.load(path, sr=44100, mono=True)
# 
# note that it returns sr and the samples. 
#
#
# Using this function, print the first 10 samples from the audio file "E3_0.wav" from the "AudioFiles" directory.

