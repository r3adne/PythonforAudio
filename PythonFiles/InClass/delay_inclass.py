import librosa
import numpy as np 
import math

y, sr = librosa.core.load('../../AudioFiles/KickOut.wav', mono=True, sr=44100)

### The Simplest Delay ###
def simpleDelay(samples, n):
    out = []

    for i in range(len(samples) + n):
        if i - n < 0:
            out.append(0)
        else:
            out.append(samples[i-n])
    
    return out

### The Seconds Delay ###
def secondsDelay(samples, time_seconds, SR):
    n = int(SR * time_seconds) # length in samples (int)

    out = []
    for i in range(len(samples) + n):
        if i - n < 0:
            out.append(0)
        else:
            out.append(samples[i-n])
    
    return out

### The Mix Delay ### 
def mixDelay(samples, time_seconds, SR, mix):
    # mix is 0.0 1.0
    # 0.0 is all dry
    # 1.0 is all wet

    n = int(SR * time_seconds) # length in samples (int)

    notmix = (mix - 1.0) + 1.0

    out = []
    for i in range(len(samples) + n):
        if i - n < 0:
            out.append(0)
        else:
            out.append((samples[i-n] * mix) + (samples[i] * notmix))
    
    return out


### The Feedback Delay ### 



### Our ideal delay ### 
# Feedback
# Time control 
# Saturation x 
# Mix



librosa.output.write_wav('./output.wav', output, sr)