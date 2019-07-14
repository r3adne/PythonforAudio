import librosa
import numpy as np 
import math

y, sr = librosa.core.load('../../AudioFiles/KickOut.wav', mono=True, sr=44100)



librosa.output.write_wav('./output.wav', output, sr)