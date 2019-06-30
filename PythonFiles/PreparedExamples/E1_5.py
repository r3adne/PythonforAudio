import librosa
import os
import math
import statistics as stats 


dataset = []

# fills dataset with samples from the files in ../AudioFiles/
for path in os.listdir('../AudioFiles/'):
    samples, sr = librosa.core.load(path, sr=44100, mono=True)
    dataset.append(samples)


#### add your code here




