import numpy
import librosa
import math
import matplotlib
import matplotlib.pyplot as plt
import statistics as stats
import os
import time

### Compressors ### 
# What do we want out of a compressor? There are a few common features: 
# The threshold is the level at which the signal begins to be effected. 
# The ratio is the ratio of the input to output signals if the signal is above the threshold
# The attack and release mediate the rate at which the signal is reduced during compression

# let's talk about the simplest compressor.
# the simplest compressor is simply a waveshaper that has a particular transfer function: 

def compressor(x, threshold, ratio, gain):
    """ compresses the single sample x with threshold (0.0, 1.0) at ratio (0.0, inf), and applies gain gain """
    rat = 1./ratio
    if x > threshold:
        return (threshold + ((x - threshold) * rat )) * gain
    elif x < -threshold:
        return -1. * gain * (threshold + (math.fabs(x) - threshold) * rat)
    else:
        return x * gain

# Let's graph this transfer function

# line, comp = [], [] # sets up two empty lists

# for i in range(-1000, 1000, 1):
#     # loops through -1000, 1000 in steps of 1.
#     y = i/1000. # makes the (-1000, 1000) loop into (-1., 1.)
#     comp.append(compressor(y, 0.5, 2, 1.2)) # adds the compressed sample to the list comp
#     line.append(y) # adds the unprocessed sample to the list line
    

# # sets up plot and plots it #
# fig, ax = plt.subplots()
# ax.plot(line, comp)
# # ax.plot(line, line)
# ax.set(xlabel="input value", ylabel="output value", title="Compressor")
# ax.grid()
# plt.show()




##################################################




# A crucial part of compression is measuring the level of the signal -- if we don't know what the level is we will be unable to know when to compress the signal. 
# This can be done a variety of ways, but as for things we've already learned, the most obvious solution is RMS. 
# Let's take an RMS function from our previous RMS example

def RMS(test_samples):
    #### We already talked about RMS. Here's the solution we came up with.
    squaredsamples = 0
    for sample in test_samples:
        squaredsamples += sample ** 2 
    
    average_squared_samples = squaredsamples / len(test_samples) # average of the squares

    rms = math.sqrt(average_squared_samples)

    return rms


# Now, we need to decide how often we want to measure the RMS of the signal. Because we're not doing this in real-time, we can feel free to measure the RMS of the signal before starting the processing.

# Note that RMS requires many samples. To do this we will do something called Windowing. Windowing is simply taking overlapping samples and 


def window(samples, n_samples_to_window, n_samples_overlap):
    """ Windows a signal with a hamming window and variable overlap. 
    Input: 
        samples (ndarray): 1-d samples
        n_samples_to_window (int): number of samples per windowing region
        n_samples_overlap (int): number of samples to overlap in each direction between windows

    Output: 
        output (list): list of arrays of windowed samples

    """
    origsamplen = len(samples)
    totalwindow = n_samples_to_window + (n_samples_overlap * 2)
    extra_samples = len(samples) % totalwindow
    samples = numpy.concatenate((samples, numpy.zeros(extra_samples)))
    n_output = (len(samples) // n_samples_to_window)  # This should be the total number of output windows
    output = [] # stores output windowed windows.
    window = numpy.hamming(totalwindow) # this creates a hamming window (google the hamming window)
    print(window)

    start = 0 
    end = totalwindow
    
    print('origsamplen: {}\n extrasamples: {}'.format(origsamplen, extra_samples))


    for i in range(n_output):
        # this appends the windowed samples to output.
        # print('{} : {}'.format(start, end))
        # print('samples[start:end]: {}\nwindow: {}'.format(samples[start:end], window))
        # print('')
        output.append(numpy.multiply(samples[start : end], window))
        # iterates pointers
        start += totalwindow
        end += totalwindow

        if end > len(samples):
            output.append([0.00000001])
            break
        

    return output 




# by now, we can take an array of samples and break them up into windows. What we need to do next is create a mask. 
# masks are generally used to tell us something about an existing piece of data. in this case, the mask is a list of RMS measurements for our windows, so that we can know what the approximate rms value at each sample is when we actually go to do compression.

# The last thing we need to find the RMS in dBu is to convert from amplitude RMS to dBFS

def rms_to_dbfs(value):
    # There are two ways to do this. I'll do the one I'm more comfortable with tbh, and the one that is considered mathematically correct. Deriving the other way requires some calc, which isn't really ccrucial to the demonstration at hand.
    if value > -0.0000000000001 and value < 0.000000000000001:
        return 0
    return 20. * math.log10(value)

def dbfs_to_amp(value):
    # again, two ways to do this, this one is easier.
    return 10. ** (value/20.)

def make_rms_mask(samples, n_samples_to_window, n_samples_overlap):
    """ makes a mask of windowed RMS values for samples """
    windowed_samples = window(samples, n_samples_to_window, n_samples_overlap)
    mask = []
    print("len(windowed_samples): {}".format(len(windowed_samples)))
    for window_ in windowed_samples:
        mask.append(rms_to_dbfs(RMS(window_)))
    return mask


# now that we can make a mask for RMS of the samples, we can compress them based on the percieved loudness instead of sample values

def compressor2(samples, threshold, ratio, gain, n_samples_to_window, n_samples_overlap):
    mask = make_rms_mask(samples, n_samples_to_window, n_samples_overlap)
    output = []

    # print(max(mask))
    # print("max: {} \nmin: {}\nmean: {}\n".format(max(mask), min(mask), stats.mean(mask)))
    # minimum, maximum = min(mask), max(mask)

    mask_index = 0
    mask_counter = 1   

    test_samples_counter = -1

    for sample in samples: # sample loop # 
        test_samples_counter += 1
        if mask_counter == n_samples_to_window:
            mask_index += 1
            mask_counter = 0   

        
        # print("{}, {}".format(mask[mask_index], threshold))
        if mask[mask_index] > threshold:
            redux = (mask[mask_index] - threshold) * ratio # the GR in dB.
            # print(redux) 
            output.append((sample/dbfs_to_amp(redux)) * gain)

        else:

            output.append(sample * gain)    
        
        mask_counter += 1

    return output



# y, sr = librosa.core.load('../../AudioFiles/KickOut.wav', mono=True, sr=44100)

# x = compressor2(y, -24., 10., 1., 4, 1)

# librosa.output.write_wav('./comp2.wav', numpy.array(x, dtype=numpy.float32), sr)


### but this actually sounds pretty trash. This is becasue we still haven't done attack and release times properly. 

def compressor4(samples, threshold, ratio, gain, attack, release, n_samples_to_window, n_samples_overlap):
    mask = make_rms_mask(samples, n_samples_to_window, n_samples_overlap) # makes the mask with settings
    output = []

    mask_index = 0 # this represents which mask we'll be using
    mask_counter = 1 # this represents how many samples are left in the current mask frame.

    samples_counter = -1 # the cuerrent sample number
    gr = 0. # holds current gain reduction value
    last_gr = 0. # holds previous gain reduction value
    grlist = [] # holds previous GRs for analysis and testing. Unnecessary for runtime.

    samp_since_attack = attack + 1 # this makes sure they don't trigger attack or release conditions.
    samp_since_release = release + 1

    for sample in samples: ### main sample loop ###
        samples_counter += 1

        if mask_counter == n_samples_to_window + (n_samples_overlap * 2): # if we're on the next mask, do these things
            mask_index += 1 # iterate mask index
            mask_counter = 0 #  resets mask_counter

        if mask[mask_index] > threshold: # if the signal is above the threshold
            if last_gr == 0:
                # this is an attack
                samp_since_attack = 0

            redux = (mask[mask_index] - threshold) * ratio # the GR in dB.

            if samp_since_attack <= attack:
                gr += redux / release
            else:
                gr = redux

            output.append((sample/dbfs_to_amp(gr)) * gain)
            last_gr = gr

            samp_since_attack += 1

        else: # if the signal is below the threshiold
            if gr > 0: # when the signal is below threshold, and if the gain reduction is currently > 0, release condition is met.
                samp_since_release = 0
                released_gr = gr 
            
            if samp_since_release <= release:
                gr -= (released_gr / release) 
            else:
                gr = 0

            output.append((sample/dbfs_to_amp(gr)) * gain)   
            samp_since_release += 1 

        
        mask_counter += 1

        grlist.append(1./dbfs_to_amp(gr))
    return output, grlist


# now that we have a way of 





y, sr = librosa.core.load('../../AudioFiles/KickOut.wav', mono=True, sr=44100)

x, gr= compressor4(y, -40., 2., 4., 128, 4410, 2, 1)

librosa.output.write_wav('./comp4.wav', numpy.array(x, dtype=numpy.float32), sr)

# # sets up plot and plots it #
fig, ax = plt.subplots()
ax.plot(x)
ax.plot(y)
ax.plot(gr)
# ax.set(xlabel="input value", ylabel="output value", title="Compressor")
# ax.grid()
plt.show()