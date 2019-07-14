# a very simple delay:
import librosa
import numpy as np


### The Simplest Delay ###
# The simplest delay has this property: 
# 
# For each time step, the sample n samples ago is output.

def sample_delay(samples, n):
    """ delays the signal `samples` by n samples """
    out = [] 
    for sample_number in range(len(samples) + n): 
        if sample_number <= n: 
            out.append(0)
        else:
            out.append(samples[sample_number - n])
    return out
    
print(sample_delay([0, 1, 2, 3, 4, 5, 6, 7], 3))
# this should output [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7].


### The Standard Delay ### 
# When we work in audio, there are a few things we expect from our delays. 
# First, the delay time is normally measured in seconds or milliseconds instead of samples
# Second, the delay normally has a mix control or wet/dry controls which allow the user to control the amount of input and delayed signal in the output.
# Third, most delays have a feedback mechanism which allows the delayed signal to repeat. 
# There is of course more that we nomally have on delays, but let's just try to implement the above for now. 


### The seconds delay ###
# This delay will take n in seconds rather than samples. To achieve this, we need another argument: the sampling rate. 

def seconds_delay(samples, time_seconds, SR):
    """ delays the input samples by time_seconds, given sampling rate SR """ 
    n = time_seconds * SR
    out = []

    for sample_number in range(len(samples) + n): 
        if sample_number <= n: 
            out.append(0)
        else:
            out.append(samples[sample_number - n])

    return out

# We'll notice that this is identical to sample_delay() save the modified arguments and the first line, converting time_seconds to n (samples)
    

### The Mix Delay ###
# This delay will implement our second idea -- the mix knob. If the mix is 0.0, the output will be identical to the input. If the mix is 1.0, the output will be just the delay. 

def mix_delay(samples, time_seconds, SR, mix):
    """ delays the input samples by time_seconds, given sampling rate SR, with mix controlled by mix.""" 
    n = time_seconds * SR
    
    dry_mix = (mix * -1) + 1

    out = []
    for sample_number in range(len(samples) + n): 
        if sample_number <= n: 
            out.append(samples[sample_number] * dry_mix)
        else:
            out.append((samples[sample_number - n] * mix) + (samples[sample_number] * dry_mix)) 

    return out


### The Feedback Delay ###
# The feedback delay represents a problem that cannot be implemented the same way our previous delays were. 
# While it's possible to do so, it's needlessly complicated and not particularly useful to learn.
# Instead, we'll use a common method for implementing delays in real-time: circular buffers. 

def feedback_delay(samples, time_seconds, SR, mix, feedback):
    """ delays the input samples by time_seconds, given sampling rate SR, with mix controlled by mix.""" 
    n = time_seconds * SR
    
    dry_mix = (mix * -1) + 1

    out = []
    for sample_number in range(len(samples) + n): 
        if sample_number <= n: 
            out.append(samples[sample_number] * dry_mix)
        else:
            next_out = 0.
            
            for loop in range(sample_number / n):
                # `sample_number / n` is the number of times so far that we've reached a place we need to feedback -- the fist delay cycle will not have any feedback because there is not any delayed material to feedback.
                next_out += samples[sample_number - (loop * n)] * (feedback ** loop)
                # this prepares the next output value -- we can explain this on the board.

            out.append((next_out * mix) + (samples[sample_number] * dry_mix)) 

    return out


# This implementation is pretty clunky and slow. It's not intuitive to our sense of feedback. This also is slower because we have to loop through the same feedback samples repeatedly. For instance, take a delay of `n = 4410` samples at `SR = 44100`, and if our samples buffer is 441,000 samples (10 seconds) long, when we reach the sample `sample_number = 4410 * 5 = 22050`, our inner for loop will call up the samples 4410 samples ago 5 times -- 17640, 13230, 8820, 4410, and 0. In the next example, we solve this more intuitively and in a way that is more similar to normal real-time implementations.

### The Circular Buffer Delay ### 
# The circular buffer is a list that represents the delayed samples. Here's how we use it to make a delay. 
# Make an array at least the length of the delay length in samples. 
# Set up two integers, read and write. write represents the index in the circular buffer that is currently being written to and read represents the index in the circular buffer that is currently being read from. 

def circbuff_delay(samples, time_seconds, SR, mix, feedback):
    """ delays the input samples by time_seconds, given sampling rate SR, with mix controlled by mix.""" 
    n = int(time_seconds * SR) + 1
    dry_mix = (mix * -1) + 1
    out = []

    circbuff = np.zeros(n * 2) # make circbuff twice the length of the delay time -- it doesn't need to be that long but there's no harm.
    write = n + 1 # put write in the middle of circbuff
    read = write - n
    bufflength = n * 2

    for sample in samples: 
        circbuff[write] = sample + (feedback * circbuff[write])
        out.append((circbuff[read] * mix) + (sample * dry_mix))

        write += 1 # increment write  
        read += 1 # increment read
        
        write %= bufflength # if write is longer than the buffer's length, it will return it to the beginning of the buffer.
        read %= bufflength # ""

    return np.array(out)


# This seems really complicated because it is. Circular buffers aren't simple to implement, but they begin to make sense when you realize the advantages. In the worst case scenario, the previous implementation would loop through the outer loop (for sample_number...) `len(samples)` times, and then could (assuming delay length in samples `n` = 1 sample) loop through the inner loop (for loop in range(sample_num) / n) `len(samples)` times as well. In our current implementation, the single-loop makes the worst-case scenario much faster. 

# If you're still confused by this, we can try to work this out graphically and on the board.



y, sr = librosa.core.load('../../AudioFiles/KickOut.wav', mono=True, sr=44100)
print(y)
print('running delay')
x = circbuff_delay(y, 0.05, sr, 0.5, 0.15)

print(x)

librosa.output.write_wav('./output.wav', x, sr)