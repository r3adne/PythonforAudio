import numpy
import librosa
import math

### Compressors ### 
# What do we want out of a compressor? There are a few common features: 
# The threshold is the level at which the signal begins to be effected. 
# The ratio is the ratio of the input to output signals if the signal is above the threshold
# The attack and release mediate the rate at which the signal is reduced during compression

# A crucial part of compression is measuring the level of the signal -- if we don't know what the level is we will be unable to know when to compress the signal. 
# This can be done a variety of ways, but as for things we've already learned, the most obvious solution is RMS. 
# Let's take an RMS function from our previous RMS example

def RMS(test_samples):
    #### Define the function here 
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
        n_samples_overlap (int): number of samples to overlap between windows

    Output: 
        output (list): list of arrays of windowed samples

    """
    
    n_output = len(samples) // n_samples_to_window 
    output = []
    window = numpy.hamming(n_samples_to_window + n_samples_overlap)

    start = 0
    end = n_samples_to_window

    output.append(numpy.multiply(samples[0 : n_samples_to_window + (n_samples_overlap / 2)], window))


    start += n_samples_to_window
    end += n_samples_to_window

    for i in range(n_output):
        output.append(numpy.multiply(samples[start : end], window))

        if end + n_samples_to_window > len(samples):
            start += n_samples_to_window
            end += n_samples_to_window


