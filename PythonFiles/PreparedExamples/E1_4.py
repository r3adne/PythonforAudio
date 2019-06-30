import librosa
import math


samples, sr = librosa.core.load('/Users/zt/Documents/PythonforAudio/AudioFiles/E3_0.wav')



def RMS(test_samples):
    #### Define the function here 
    squaredsamples = 0
    for sample in test_samples:
        squaredsamples += sample ** 2 
    
    average_squared_samples = squaredsamples / len(test_samples) # average of the squares

    rms = math.sqrt(average_squared_samples)

    return rms


print(RMS(samples))