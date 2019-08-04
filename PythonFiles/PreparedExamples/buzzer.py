import matplotlib
import matplotlib.pyplot as plt
import math
import librosa
import numpy as np 
import scipy as scp 

np.seterr(all="print")

twopi = np.pi * 2.0

wavetable_size = 44100
wavetable = np.ndarray(wavetable_size)

for j, i in zip(np.arange(0., 1., 1./wavetable_size), range(wavetable_size)):
    # j is the current position along sin, i is the current index
    wavetable[i] = np.sin(twopi*j) / twopi
    print(wavetable[i])



ax, fig = plt.subplots()
fig.plot(wavetable)
plt.show()

def lin_interp(table, pos):
    # linear interpolation for our table
    lower = table[math.floor(pos)] 
    upper = table[math.ceil(pos)]
    floor = pos - math.floor(pos)
    ceil = math.ceil(pos) - pos 

    return (lower * ceil + upper * floor)

########



spacing = 50 # Hz
fundamental = 50 # Hz
maximum = 20000 # Hz
weights = [1.0 for i in np.arange(fundamental, maximum, spacing)]

length = 10 # seconds
sr = 44100 # Hz
samp_length = length * sr


# 400 hz at 44100 is how many samples per cycle?  
# 1/frequency * sr.

output = np.ndarray(samp_length)

for i in np.arange(fundamental, maximum, spacing):

    samples_per_cycle = sr/float(i) # converts hz to samples based on SR
    table_length = math.ceil(wavetable_size / samples_per_cycle) # the length of this frequency's table

    table = np.ndarray(table_length) # this frequency's table
    
    for j, l  in zip(range(0, wavetable_size, table_length), range(table_length)): # makes table fior this current f
        table[l] = lin_interp(wavetable, j) # add to table.
    
    iter = 0
    for k in range(math.floor(samp_length / table_length)): # this one actually adds to output
        iter %= table_length
        output[k] += table[iter]
        output[k] /= 2.
        iter += 1
 
