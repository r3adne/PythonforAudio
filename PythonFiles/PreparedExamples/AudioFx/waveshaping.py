import math
import librosa
import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 

### Waveshaping ###

# Here's a graph that will help us understand waveshapers: https://www.desmos.com/calculator/sp8lae1nzq

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
    """this represents the transfer function y = x."""
    return x

def softClip(x):
    """ returns a soft-clipping cubic function of x"""   
    if x >= (1.):
        return (1.)
    elif x <= (-1.):
        return (-1.)
    else:
        return 1.5 * (x - ((x**3.) / 3.))

# Second, there are some that depend on another input value. 

def hardClip(x, a):
    """ returns a hard clipped signal of x at level a."""
    if x >= 1/(a*2):
        return 1.
    elif x <= -1./(a*2):
        return -1.
    else: 
        return x * 2 * a

def arctan(x, a):
    """ returns arctan distortion of x at amount a."""
    return ((2./math.pi) * math.atan((1. + a * 9.) * x))

def square(x):
    if x > 0.0:
        return 1.0
    else:
        return -1.0

def ternary(x):
    if x > 0.001:
        return 1. 
    elif x < -0.001: 
        return -1. 
    
    return 0.



# we can load an audio file, loop through its samples, and run each through each function.

# load in audio file
y, sr = librosa.core.load('../../../AudioFiles/KickOut.wav', mono=True, sr=44100)

x = []
for sample in y:
    x.append(softClip(sample))

librosa.output.write_wav('./softClip.wav', np.array(x, dtype=np.float32), sr)

x = []
for sample in y:
    x.append(hardClip(sample, 1000.))

librosa.output.write_wav('./hardClip.wav', np.array(x, dtype=np.float32), sr)

x = []
for sample in y:
    x.append(arctan(sample, 2.))

librosa.output.write_wav('./arctan.wav', np.array(x, dtype=np.float32), sr)

x = []
for sample in y:
    x.append(square(sample))

librosa.output.write_wav('./square.wav', np.array(x, dtype=np.float32), sr)

x = []
for sample in y:
    x.append(ternary(sample))

librosa.output.write_wav('./ternary.wav', np.array(x, dtype=np.float32), sr)

hard, soft, arc, squ, tern, line = [], [], [], [], [], []

for i in range(-1000, 1000, 1):
    y = i/1000.
    hard.append(hardClip(y, 1000.))
    soft.append(softClip(y))
    arc.append(arctan(y, 1.))
    tern.append(ternary(y))
    line.append(y)
    squ.append(square(i))



fig, ax = plt.subplots() # figure, axes 

ax.plot(line, hard)
ax.plot(line, soft)
ax.plot(line, arc)
ax.plot(line, squ)
ax.plot(line, tern)
ax.plot(line, line)


ax.set(xlabel="input value", ylabel="output value", title="various transfer functions")
ax.grid()

plt.show()




