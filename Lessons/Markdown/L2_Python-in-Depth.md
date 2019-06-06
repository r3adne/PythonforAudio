# Python in Depth

#### Zachary Lewis-Towbes; BerkleeMakes; June 2019

###Contents

1. [Review existing Python concepts (Variables, Types, Functions)](#ReviewingPython)
2. [More about functions](#MoreAboutFunctions) 
	* [Not Returning](#notReturning)
	* [Default Arguments](#defaultArguments)
	* [Keyword Arguments](#keywordArguments)
	* [Docstrings](#docstrings)
3. [Common built-in functions](#Builtins)
	* [print()](#print)
	* [range()](#range)
	* [len()](#len)
	* [type()](#type)
	* [Type Conversion](#conversion)
	* [String.format()](#format)
	* [List Methods](#listMethods)
4. [Importing modules](#Imports)
5. [Built-in Modules](#Modules)
	* [os](#os)
	* [math](#math)
	* [statistics](#stats)
6. [Style](#Style) 


<a name="ReviewingPython"></a>
### Reviewing Python 

In the last two lessons we learned about Variables and their Types; Arithmetic, Definition, and Identity operators; Comparators; Looping and if, elif, else; and Functions. If you have any questions about these, now is the time to ask.


<br/>

<a name="MoreAboutFunctions"></a>
### More about Functions

We've already seen how functions can be used to manipulate and return data. We know how to pass arguments to functions and how to return data from the functions. Now let's look at some other ways we can make functions even more useful.

* [Not Returning](#notReturning)
* [Default Arguments](#defaultArguments)
* [Keyword Arguments](#keywordArguments)
* [Docstrings](#docstrings)

<a name="notReturning"></a>
#### Not Returning

What happens if we don't return from a function? Intuitively, nothing happens, but in reality, it still returns *something*. This something is actually its own type: `None`.  In other words, if we make a function which doesn't return anything and then call it in a definition, what happens?

	def printHelloWorld():
		print('hello world')
	
	a = printHelloWorld()
	
First, in the function `printHelloWorld()`, python prints `hello world` to the command line. Then, it sets `a` to `None`. Any function that doesn't have a `return` function returns `None`. `None` is the lack of a type. 

<a name="defaultArguments"></a>
#### Default Arguments

Sometimes there are functions that we want to use for certain basic functionality, but we still want to allow more advanced control of their behavior. We can do them using default arguments. Default arguments are simply arguments whose values we provide when writing the function, but which we can override later. For instance, in our function that solved the problem given at the end of L1, we can make an argument default like this:

	def pe1(a, b, number=1000):
		sum = 0
		for i in range(number):
		    if i % a == 0:
		        sum += i
		    elif i % b == 0:
		        sum += i 
		    
		return sum

This means that we can call the function using just:

	pe1(a, b)
	
and it will default the value of `number` to `1000`. 

If we need to, though, we can call it as:

	pe1(a, b, 100)

which will set the value of `number` to `100`. 

<a name="keywordArguments"></a>
#### Keyword Arguments

Similar to Default Arguments, Keyword Arguments are arguments that can be accessed by their keyword. Using the last function `pe1(a, b, number=1000)`, we can access number like this as well as the way we did above:

	pe1(a, b, number=959).

This is quite useful when there are multiple keywords. If we modified `pe1`, we could do this:

	def pe1(a=3, b=5, number=1000):
		sum = 0
		for i in range(number):
		    if i % a == 0:
		        sum += i
		    elif i % b == 0:
		        sum += i 
		    
		return sum

In this case, if we wanted to change only `number` and not `a` or `b`, we can do so:

	pe1(number=10)	

without calling `a` or `b`.

<a name="docstrings"></a>
#### Docstrings

Documentation strings are simple ways of describing to future readers what a function does. While it doesn't do anything to the execution of the function, it assists people using your function. They look like this:

	def pe1(a, b, number=1000):
		""" 
		finds the sum of numbers divisible by either a or b under 1000.
		"""
		sum = 0
		for i in range(number):
		    if i % a == 0:
		        sum += i
		    elif i % b == 0:
		        sum += i 
		    
		return sum

This is also how we can generally format multi-line comments in Python. if you have a long block of code you'd like to comment out, you may use """ """.


<br/>

<a name="Builtins"></a>
### Common Built-in Functions and Methods

Here we'll cover many of the most common built-in functions. 

* [print()](#print)
* [range()](#range)
* [len()](#len)
* [type()](#type)
* [Type Conversion](#conversion)
* [String.format()](#format)
* [List Methods](#listMethods)

<a name="print"></a>
#### print()

We already know how to use print(), but it's a built-in function so we'll mention it here.

<a name="range"></a>
#### range()

`range(n, m)` returns the integers from n to m, exclusive.

The first argument is optional and defaults to 0:

`range(10)` is equivalent to `range(0, 10)`

range can also be used with a step amount: `range(start, stop, step=1)`

For instance, `list(range(0, 10, 2))` is `[0, 2, 4, 6, 8]`.

`range()` is most often used in for loops.


Note: `range()` doesn't return a list. rather, to read it as a list we must call `list(range(n))`. That said, it is used in for loops in that it is interpreted as a sequence. 

<a name="len"></a>
#### len()

len() returns the length of a string, dict, or list. 

	len('hello world') # is 11
	len([1, 2, 3, 4]) # is 4

<a name="type"></a>
#### type()

The type() function checks the type of its first argument:

	a = 1
	
	print(type(a))	

this prints `<class 'int'>`, meaning that a is an integer. 


<a name="conversion"></a>
#### Type conversion

You may need to take input from a user as a string, for instance, which looks like this `"13.2"`. In order to use this data numerically, you'll need to convert it to a float. We can do this simply by calling `float("13.2")`. There are similar functions for each other type:

	list('[1, 2, 3, 4]') # is [1, 2, 3, 4]
	list("Hello World") # is ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
	int('139') # is 139
	str(139) # is '139'

This is quite useful especially when formatting strings manually. As we know, we can use the `+` to append one string to another. 


	nGiraffes = 12
	nPonies = 2
	name = 'Erin'

	print('We have ' + str(nGiraffes) + ' giraffes and ' + str(nPonies) + ' ponies, ' + name + '.') 


<a name="format"></a>
#### String.format()

To do the same thing we just did above in a simpler way, we can use String.format().

	nGiraffes = 12
	nPonies = 2
	name = 'Erin'
	
	print('We have {} giraffes and {} ponies, {}.'.format(nGiraffes, nPonies, name))

This will print: 

	We have 12 giraffes and 2 ponies, Erin.


<a name="listMethods"></a>
#### List Methods

Lists have many features that we won't get into for now, but the bulk of them are:

	List.append()
	List.pop()
	List.count()
	List.remove()
	List.sort()
	min(list)
	max(list)
	

##### List.append()

`List.append()` adds a given item to the end of a list. 

	a = [1, 2, 3, 4]
	a.append(5)
	print(a)
	
prints `[1, 2, 3, 4, 5]`.


##### List.pop()

`List.pop()` _removes and returns_ the item at the given index. If no index is given, it will return the last item of the list.

	a = [1, 2, 3, 4]
	print(a.pop(2))
	

prints `3`. Now a is `[1, 2, 4]`.

	print(a.pop())

prints `4` because `a.pop()` defaults to remoivng the last item. 

##### List.count()

`List.count(i)` returns the number of times that i occurs in a list.

	a = [1, 2, 3, 1, 1, 12, 109, 2, 1]
	print(a.count(1))
	
This prints `4` because there are 4 occurrences of the item 1 in the list a.

##### List.remove()

`List.remove(a)` removes the first occurrence of a in the list.

	a = [1, 2, 3, 1, 1, 12, 109, 2, 1] 
	a.remove(1)

now a is `[2, 3, 1, 1, 12, 109, 2, 1]`

	a.remove(1)
	
now a is `[2, 3, 1, 12, 109, 2, 1]`
	
	a.remove(1)
	
now a is `[2, 3, 12, 109, 2, 1]`

##### List.sort() 

`List.sort()` simply sorts the list in ascending order. 

	a = [1, 2, 3, 1, 1, 12, 109, 2, 1] 
	a.sort()
	
now a is `[1, 1, 1, 1, 2, 2, 3, 12, 109]`

##### max(a), min(a)

These simply return the highest and lowest values of a list:

	a = [1, 2, 3, 1, 1, 12, 109, 2, 1]
	print(max(a))
	
prints `109`.

	print(min(a))

prints `1`.

<br/>

<a name="Imports"></a>
### Importing Modules

Python supports the use of third-party modules and code using the `import` keyword. At the top of a file, you can `import` a function from another python file. Let's say we have a file with our `divisibleByThree` function:

	# this file is called 'divisibility.py'
	
	def divisibleByThree(number):
	    sum = 0
	    for i in list(str(number)):
	        sum += int(i)
	
	    if len(str(sum)) > 1:
	        if divisibleByThree(sum) == True:
	            return True
	    else:
	        if (sum == 9 or sum == 6 or sum == 3):
	            return True
	        else:
	            return False
	            
Now, in the same folder, we can make another file:

	# this file is called 'L2-0.py'
	
	import divisibility
	 
	print(divisibility.divisibleByThree(2145)
	print(divisibility.divisibleByThree(19)
	
This file will successfully use the function from the other file. The `.` tells us that `divisibleByThree` is a member of `divisibility`. We'll discuss membership in L3. 


<br/>

<a name="Modules"></a>
### Built-in modules

Python has a few modules that are installed with python. We'll go over the basic functionality of a few of them here.

* [os](#os)
* [math](#math)
* [statistics](#stats)

<a name="os"></a>
#### os

The `os` module gives us access to certain functionality that is built in to our operating system.

##### os.listdir()

Listdir simply lists the items in a directory. For instance, in our directory 'PythonforAudio', if we run 

	import os
	print(os.listdir())
	
we will see `['.DS_Store', 'README.md', '.gitignore', 'PythonFiles', 'Lessons', '.git']`.

##### os.system()

System executes any shell command (terminal command) within python. 

	print(os.system('ls')) 

prints the output of `ls` on the terminal.

##### os.rename(src, dst)

This renames any file. `src` should be the path of the existing file and `dst` should be the path to the new file.

##### os.uname()

`uname()` returns information about the operating system. 

`os` has documentation [here](https://docs.python.org/3/library/os.html).

<a name="math"></a>
#### math

Python has a library that performs basic math functions such as logarithms and trig functions. It also has several constants. For instance:

	import math
	
	pi = math.pi
	inf = math.inf
	e = math.e
	
	math.cos(pi) # is -1
	math.sqrt(16) # is 4
	math.log(e) # is 1; log defaults to ln()
	
You can see more about `math` [here](https://docs.python.org/3/library/math.html).

<a name="stats"></a>
#### statistics

The `statistics` module has all sorts of statistical tools. For instance:

	import statistics as stats # I don't want to type statistics over and over again
	stats.mean([1, 2, 5]) # is 2.66666...
	stats.median([1, 2, 5]) # is 2
	stats.stdev([1, 2, 5]) is 2.081665999466133

Read more about it [here](https://docs.python.org/3/library/statistics.html).

<br/>

<a name="Style"> </a>
### Style

Python developers are expected to write readable code. Python helps with this due to its design, but we must hold up our end as well. Here are some tips on how to maintain consistent style.

#### tabs and spaces

The Python interpreter cannot tell the difference between tabs and sets of spaces, but it's best to understand which to use and when. For most text editors meant for writing code, tabs are automatically converted to spaces. In Python, this is generally 4 spaces. For our purposes, tabs are easier to write, but if you're working in a text editor that is very simple and does not convert tabs to spaces, it's worth considering using spaces instead. 

#### wrapping

Each line of Python should be no longer than 79 characters. This usually does not cause problems, but it's best to try to maintain this standard practice. You may use the `\` character as a line break when necessary -- python will not read any newlines immediately after the `\` character 


#### blank lines

Add blank lines between functions, classes, and large code blocks. This helps readability. 

#### comment lines	

Try to put comments on their own lines, unless they're sufficiently short. It is acceptable to write multi-line comments as many separate lines or as multi-line comments using `""" """`. 


#### use docstrings

Just use them.

#### use a consistent naming convention

Most people name functions with `lower_case_letters_separated_by_underscores()` and classes as `CamelCase` or `camelCase`. Personally, I tend to use `lowercaseFirstCamels` for variables, `lower_case_underscored	` for functions, and `CamelCase` for classes. 

#### use spaces after operators

and commas. The only common exception to this rule is in keyword and default arguments, where there are no spaces between the arguments and their definition operators.

#### use normal characters

Unless you're specifically writing a program in a non-latin script language, try to stay within the ASCII character set. 