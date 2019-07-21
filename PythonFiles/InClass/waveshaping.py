import math
import librosa
import numpy as np 


### Waveshaping ###
# Waveshaping is the method of modifying samples in a signal using a transfer function. 
# Transfer functions are just functions that represent the relationship between the input and output of a system.
# Most often, the transfer function is represented as f(x) where x is the input function and f(x) is the output function. 
# Seen as a 2-dimensional graph, if you slide your sample value x between x = -1.0 and x = 1.0, you'll see the transfer function on the y-axis. 
# Often, these functions are designed to add harmonic distortion to the signal. 

### Linearity and Time-invariance ###
# Two important concepts in signal processing are linearity and time-invariance. 
# Linear systems fulfill the following property:
# for a system f(x) and its input x and any two input values a and b, f(a) + f(b) = f(a + b).
# What does this mean in English? 
# The sum of the individual outputs of the function for inputs a and b must be equal to the function of the sum of inputs a and b.
# So, is a waveshaper linear? If it has the transfer funciton f(x) = x, yes. Otherwise, no. 
# Waveshapers are not linear because if we add some sets of two values together and take their output, the result is different than the sum of their results. We can see this on the desmos graph. 
# Time-invariant functions are those who don't depend on the time position of a signal.
# waveshapers are time-invariant because they don't depend on the index of the signal. 

# Let's define some transfer functions for common waveshapers. 
# First, there are a few that will be defined that depend only on one ipnut -- the input value x.

def nothing(x):
    """this represents the transfer function y=x."""
    return x

def softClip(x):
    """ returns a soft-clipping cubic function of x"""
    print(type(x))
    
    if x >= (2./3.):
        return (2./3.)
    elif x <= (-2./3.):
        return (-2./3.)
    else:
        return (x - ((x**3.) / 3.))

# Second, there are some that depend on another input value. 

def hardClip(x, a):
    """ returns a hard clipped signal of x at level a."""
    if x >= a:
        return a
    elif x <= -1.*a:
        return -1.*a 
    else: 
        return x

def arctan(x, a):
    """ returns arctan distortion of x at amount a."""
    return (2./math.pi) * math.atan((1. + (a * 9.) * x))


# we can load an audio file, loop through its samples, and run each through this function.

# load in audio file
y, sr = librosa.core.load('../../AudioFiles/KickOut.wav', mono=True, sr=44100)

x = []
for sample in y:
    x.append(softClip(sample))

librosa.output.write_wav('./softClip.wav', x, sr)

x = []
for sample in y:
    x.append(hardClip(sample, 1.))

librosa.output.write_wav('./hardClip.wav', x, sr)

x = []
for sample in y:
    x.append(arctan(sample, 1.))

librosa.output.write_wav('./arctan.wav', x, sr)