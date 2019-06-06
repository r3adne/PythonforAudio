# External Modules in Python
#### Zachary Lewis-Towbes; BerkleeMakes; June 2019

### Installing PIP

While we often use the `import` command to reuse our own code, we can also use it to use external modules made by other groups of programmers. 

To do this, we will install pip, the Package Installer for Python. Run these lines on your terminal:

`cu https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

`python3 get-pip.py`

`pip install --upgrade pip`

Now we can install any package with:

`pip install <name of package>`

We'll start with a few basic packages:

`pip install numpy`

`pip install scipy`

`pip install matplotlib`

`pip install librosa`

`pip install pydub`

Now, even though these files aren't in the same directory as our python file, we can use `import` to use the functions inside these files. This is because they are installed **globally**. 


### Module Basics

We will review the functionality of each of these modules below, along with a few modules that we have installed by default:

#### Numpy

Numpy is a python library for scientific computing in Python. It offers great array objects, which are like lists but faster and feature easy multi-dimensional functionality. These are called `numpy.ndarray`. They have a great pseudorandom number generator, `numpy.random`. There's also a great fft algorithm, `numpy.fft`. For the time being, we'll just cover the random and ndarray functionality, but we'll discuss the fft in the future. 

Note: the `import` function allows us to change the name we use to reference the file. Due to how common Numpy is, many people use `import numpy as np` and then refer to numpy as `np`. 

##### numpy.ndarray

Numpy's array objects are different than lists because they are faster. We can discuss why later, but numpy arrays are much better for audio because of their increased speed. They also have a data type that must be declared.

Let's make an array like this:

	import numpy
	
	a = numpy.ndarray([[1, 2, 3], [4, 5, 6]], numpy.int32]
	
We've just made a two-dimensional array with 32-bit integer data type. Let's look at the size of the array.

	print(a.shape) 

Shows us `(2, 3)`. This makes sense because if we think about the array graphically, we might see:

	[1, 2, 3],
	[4, 5, 6]

This is 2 units tall and three across. 

Just as a simple example, if we had audio samples as two separate stereo streams:

	# L samples [0.12034, -0.12499, 0.95323, 0.15924, 0.51942, -0.59342]
	# R samples [-0.51243, -0.01294, 0.59322, 0.12494, 0.12483, 0.12948]
	
	# Let's make this stereo file a numpy array
	
	a = numpy.array([[0.12034, -0.12499, 0.95323, 0.15924, 0.51942, -0.59342], [-0.51243, -0.01294, 0.59322, 0.12494, 0.12483, 0.12948]], numpy.float32)
	
	print(a.shape)

gives us `(2, 6)` 
	
	
Let's say we have an algorithm that expects a stereo file in the opposite configuration, where each sample is formatted `[[left sample 0, right sample 0], [left sample 1, right sample 1], ... [left sample n, right sample n]]`

In other words, we want to change 

	[[0.12034, -0.12499, 0.95323, 0.15924, 0.51942, -0.59342],
	[-0.51243, -0.01294, 0.59322, 0.12494, 0.12483, 0.12948]]

to

	[[ 0.12034, -0.51243],
	[-0.12499, -0.01294],
   	[ 0.95323,  0.59322],
   	[ 0.15924,  0.12494],
	[ 0.51942,  0.12483],
   	[-0.59342,  0.12948]]
   	
This is another way of saying that we want our shape to be `(6, 2)` instead of `(2, 6)`. In Linear Algebra, this is called Transform. We can invoke this using `.T`:

	b = a.T
	print(b.shape)

gives us `(6, 2)`

##### numpy.random

numpy.random is a library that gives us pseudorandom numbers. We say pseudorandom because it's impossible to be completely random when generating numbers in a computer. Numpy.random has some of the best random number generators avaliable to python. There are many different ways to generate random numbers, and we'll describe three.

	import numpy
	
	numpy.random.random()
	
	numpy.random.randint(0, high = 10)
	
	numpy.random.choice([1, 12, 190, 4129, 1384192])
	
`numpy.random.random()` gives a random float between 0 and 1. 

`numpy.random.randint(low, high = high)` gives a random integer between low and high if high is given.

`numpy.random.choice(list)` gives us a random value from the list given. 

There are many other ways to generate random numbers, and you can read about them in the documentation. 


#### Scipy




#### Matplotlib

Matplotlib is the go-to library for graphing and plotting data in Python. 


#### Librosa

Librosa is a fantastic library for music information retrieval, i.e. anaylsis of music. It has loading and saving utilities, oscillators, resampling algorithms, ffts and related spectral techniques, loudness measurements, and time/pitch warping. Much of this we can (and will) figure out how to implement ourselves, but if we just need to get something up and running, we should do so through librosa. 


#### PyDub
