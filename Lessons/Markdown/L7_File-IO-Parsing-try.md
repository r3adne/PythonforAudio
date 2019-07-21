# File I/O, Parsing Datasets,try...except 

#### Zachary Lewis-Towbes; BerkleeMakes; July 2019 

Python has built-in file input and output functionality which can open basically any type of file. Today we'll focus on text files, especially those containing data we plan to process. There are a number of publicly avaliable datasets containing lyrics of pop songs. We'll use one of these. 

### Opening files
Python makes opening files very easy. To open any type of file in python, we use the `open()` function, which takes one argument -- the path. In this case:

	file = open('test_file.txt')

opens our datset. With a file open, we can read it in many ways, but the most common is line-by-line. To do this we'll use `file.readline()`, which simply reads the next unread line from the dataset. Let's try this in the interpreter on test_file.txt, which is in PreparedExamples. 

This works just fine, but there's one catch. When opening a file in python like this, python sets aside memory for the entire size of the file. This memory won't be freed up until the program is done executing. For such a small file, that's fine, but we may find datasets that are many gigabytes or larger. 

To get around this, we use `with ___ as ___:` which might look familiar from how we import modules. `import numpy as np` imports the module `numpy`, but gives us the name `np`. The same is true of `with ___ as ___:`. We specifically use:

	with open('song_dataset.csv') as file:
		# do something to file
	
	# now that we're out of the with statement, the memory we used loading the file is free.
	
This is how we'll do this for our project:

First, we need to define a list of the raw data we'll get out of this, which we'll have to clean further if we run into problems.

	raw_songs = []
	with open('billboard_lyrics.csv') as f:
	
Then, we need to load each song. Each song is conveniently formatted as one line. 

	raw_songs = []
	with open('billboard_lyrics.csv') as f:
	 for i in range(5100):
        raw_songs.append(f.readline())
	        

This makes sense, but we'll run into one problem. Let's try printing out these lines:

	raw_songs = []
	with open('billboard_lyrics.csv') as f:
	 for i in range(5100):
        raw_songs.append(f.readline())
       
    print(raw_songs[0])
    
We actually want a list of each property of the song. To do this, we want to make a list out of the line. Conveniently, Python has a way of splitting strings into lists by a certain character. The `String.split()` method splits a string based on a character. To split a string of words into a list of each word, we'd split by the `' '` character. You may notice that this file is split up by the `,` character. So, instead of the above, we can do this:


	raw_songs = []
	with open('billboard_lyrics.csv') as f:
	 for i in range(5100):
        raw_songs.append(f.readline().split(','))
       
    print(raw_songs[0])

I tried this and ran into some sort of error trying to decode the file. This only occurred at a certain line. I'm not sure why, but it's a good opportunity to bring up a new Python idea. 

### try...except

In the past, when we've seen errors in Python, they've meant that we need to stop our execution and fix a problem. Python actually gives us the opportunity to disregard some errors using `try: ` and `except: `. These can be read as `try` to do this, `except` if it doesn't work. 

Let's do something we know is wrong, adding a string to an integer. 

	'a' + 1
	
This gives us the error:

	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: can only concatenate str (not "int") to str
	
The important thing here is that it's a `TypeError`. `TypeError` is actually just a class that represents an error in Python, so let's use a `try: except:` clause to catch this error.

	try:
		'a' + 1
	except:
		print('oops')
	
If we're doing a few things but we're only looking to catch the `TypeError`, we can do so like this:

	try:
		'a' + 1
	except TypeError:
		print('oops')
		
Now if we change the `TypeError` out for a different error, such as `IndexError`, we'll still get it:

	try:
		b = [0]
		b[1]
		'a' + 1
	except TypeError:
		print('oops')

	
Now, we still get the `IndexError`, which tells us that we've asked for a list index that is out of range (the list b doesn't have a 1st value, only the 0th.)

The error I kept getting was `UnicodeDecodeError`, which means the file we read had some weird character that couldn't be decoded. In this case we'll catch the error and print something out, but we won't stop the program.

	
	raw_songs = []
	with open('billboard_lyrics.csv') as f:
	    for i in range(5100): # this is how many songs are in the dataset...
	        try:
	            raw_songs.append(f.readline().split(','))
	        except UnicodeDecodeError: 
	            print('not sure why this error is coming up, but it should be fine.')
	
Finally, `try: except:` clauses also have a few more options. the only thing we'll use today is `else:`. If we have a `try: except:` pair with `else:` at the end, it will simply execute what's inside the `else:` only if the `try:` worked and found no exception.


### Sets
Python sets are fancy data types that are basically lists without duplicates. Later down the line we'll use `list(set())` to remove duplicates from a list.

