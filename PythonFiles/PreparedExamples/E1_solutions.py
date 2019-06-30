import librosa
import math
import statistics as stats 
import os


### Exercise 3
samples, sr = librosa.core.load('../AudioFiles/E3_0.wav', sr=44100, mono=True)
print(samples[:10])

### Exercise 4
samples, sr = librosa.core.load('../AudioFiles/E3_0.wav')

def RMS(test_samples):
    #### Define the function here 
    result = 0.
    for sample in test_samples:
        result += sample ** 2

    result /= len(test_samples)
    result = math.sqrt(result)
    return result

print(RMS(samples))


### Exercise 5

dataset = []

# fills dataset with samples from the files in ../AudioFiles/
for path in os.listdir('../AudioFiles/'):
    samples, sr = librosa.core.load(path, sr=44100, mono=True)
    dataset.append(samples)

for audioFile in samples:
    dataset.append(RMS(samples))


# haven't gotten to this yet... we'll cover it in class.
