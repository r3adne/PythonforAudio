# Introduction to the Python Programming Language 
#### Zachary Lewis-Towbes; BerkleeMakes; April 2019

<br/>

### Goals  
 
By the end of this lesson, you’ll be able to:

	Solve simple mathematical problems such as Project Euler Problem 1.
	Understand Python data types and syntax.
	Read logical operators in Python.



Getting started: 

We’ll use Python 3 and our mac terminal to run python. This requires a tiny bit of set up.

<br/>

### Installing Python

First, we’ll run these lines:

`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

`export PATH="/usr/local/opt/python/libexec/bin:$PATH"`

`brew install python`

Now if we type:

`python3 --version`

The output will show our current version of python. For me this was 3.7.3, but it shouldn’t matter too much as long as it’s at least python 3.x.x.

Python 3 is now installed on your machine! Finally, let’s install one more thing before we get going.

<br/>

### Installing VSCode
VSCode is a text editor designed for working with code. It’s released by microsoft but it works on mac, windows, and linux. 
You should be able to download and install it easily at this link:
[https://code.visualstudio.com/download] (https://code.visualstudio.com/download)


<br/>


## Programming in Python  
### The Python Language 

Python is a programming language that is very **high-level**. Compared to some languages such as assemblers, and even other languages such as C and C++, Python is simple to read and write. This ease of use is at the expense of certain control over what you're writing. This makes it very effective for a few certain tasks 

1. Rapid development. Python makes it easy to make relatively complicated things quickly.
2. Scripting. Python makes it easy to write simple operations that can make your life easier.
3. Creativity. It doesn't take long to make an audio processor in Python. If you can think up a signal processing method that you can't implement in Max or your DAW, you can probably write it in Python in only a few minutes.


The first thing to know is that to print a variable or a statement to the terminal, you can use the `print` command like this: `print('hello world!')`. In this case, it takes the string `'hello world!'` and prints it out to the terminal. The output of lesson0_0.py would be `hello world!`.

### How to Run Python Code

Some languages like C and C++ are **compiled**. This means that to execute the code you must tell the computer to turn the program into machine code. Python is not like this -- it is **interpreted**. 

There are two basic ways to run Python: In a .py file and in "interactive mode". Let's try both.

#### Running a .py File

Using the Terminal, go to the directory `PythonCurriculum/PythonFiles/`. Open `L1-0.py` in a text editor. You'll see that it has one line, which we've discussed above: `print('hello world!')`. Now, in the terminal, type `python3 L1-0.py`. You'll see `hello world!` on the terminal. 


#### Using Interactive Mode

Now, in a new terminal tab or window, type `python3`. You should see `>>>` before your cursor instead of `$`. Next, type `print('hello world!')`. You'll see another line pop up with `hello world!`, just like when you ran the file. To exit the interpreter and return to the Bash shell (i.e. terminal), type `exit()` or type control + d.

<br/>

As you may have surmised, these two methods do the same thing, but one is typed out line-by-line and the other simply takes each line from the file. Other than that they are identical. For very short programs like those that we'll use to discuss types, we'll use interactive mode, but for longer projects this can become tedious at best and quite often unusable. 

<br/>


### Types  

If you're writing a program, you'll need to store data at some point. Maybe you're trying to process audio and you want to store your audio signal, or maybe you're trying to plan your schedule and you'd like to store information about what time a class takes place. You'll store these pieces of information in variables. For instance, if you're trying to add two numbers, you'd have to store a few things in different places. We'll see this below.

Unlike many languages, Python doesn't require that you declare a variable's type; it figures out the type using context and syntax. If you're already familiar with types like int, float, string, Bool, and list, you can skim through this section. 


#### Numerical types  

##### Integers

Python gives us access to a few different types that are specifically meant to be used as numbers. Here's an example of using integers:

`a = 1`

`b = 2`

`c = a + b`

`print(c)`

this would print `3` to the command line.

We've just stored three numbers: a, b, and c. Specifically, we're storing integers. In Python, integers are 24 bits and they are **signed** meaning that they offer both positive and negative numbers. For instance, if we changed our code to:

`a = 1`

`b = 2`

`c = a - b`

c is equal to -1. 

In the current version of Python, there is no size limit for integers except the size of your avaliable memory (i.e. very, very large: if n is the amount of avaliable memory in gb, you could have an int up to `2**(n*(10**9))` -- too big to worry about.)

##### Floats

Similarlty, we can use decimal points using **floating point** numbers, or floats. In python, floats work almost exactly the same way as ints:

`a = 1.5`

`b = 2.5`

`c = a - b`

`print(c)`  

this would output `-1.0` to the command line.



##### Strings  

A string is a series of characters. For instance, "hello world" is a string. In python, Strings can be designated with either '' or "" symbols. They can express any set of symbols, but in some cases these symbol sets are just letters, characters, and numbers, while in others they can include things like emoji. Let's declare a string:

`a = 'hello'`

Now, if we had:

`print(a)`

the output would be:

`hello`

Interestingly, we can do a few confusing things to strings. For instance:

`a = 'hello'`

`b = 'world'`

`c = a+b`

What should this output? 

Python does something rather helpful and clever when we try to add strings together. It simply appends the second string to the end of the first.

The above code would output `hello world`. This can be very helpful.

There are some other fun things we can do wtih strings but we'll save them for later.

##### Boolean  

Boolean might sound like a complicated word, but it's just another name for **true or false**. Boolean variables are either `True` or `False`. For instance, if you were making a video game and you wanted to know whether it was night or day in your virual world, you might say:

`is_daytime = False`

for when it's night time. 

There are many things you can do to boolean variables in python. We can use logic such as `not`, `and`, and `or` like this:

`a = not False`
`b = not True`

As you may have guessed, not simply switches the variable from `True` to `False`, or from `False` to `True`. in this case, the value of `a` is `True` and the value of `b` is `False`. 

`not` is the only thing we can do to booleans that only needs one input. `and` and `or` both take two inputs. 


`and` returns `False` if either of the two inputs is `False`. Let's see this in action:

`a = True and True # a is True`

`b = True and False # b is False`

`c = False and True # c is False`

`d = False and False # d is False`

<br/>

`or` returns `True` if either of the two inputs is `True`.

`a = True or True # a is True`

`b = True or False # b is True`

`c = False or True # c is True`

`d = False or False # d is False`

<br/>

Booleans are sometimes used as types of variables, such as in the `is_daytime = False` example, but more often they are used when comparing two things. We'll talk about that in the **comparators** section below.


##### Lists  

Lists are just what they sound like. They are a series of other types. that can be used to store sequential information. They are **ordered** in that they cannot change order without you telling them to. They are not to be confused with arrays from some other programming languages like C though, for several reasons, most importantly that Python lists can change size after being created. 

Lsts are declared with square brackets []. We can create an empty list like this:

`a = []`

Lists are resizable. If we wanted to put new information at the end of a list, we could do so using `a.append()`. This simply puts the value between the parentheses at the end of `a`. 

Let's say we took a list:

`a = [1, 2, 3, 4, 5, 6]`

If we wanted to see what value is at a given location in the list, we can do so like this:

`b = a[0]`

this takes the first item in the list and sets `b` to it. 

We can even use negative numbers to access the end of the list. If you wanted the last item in a list, you could use:

`b = a[-1]`.

You can also select slices of a list using this format

`b = a[0:2]`.

`b` is now equal to `[1, 2, 3]` because it has taken a slice of the list from index 0 to index 2.

<br/>

*Lists can contain any data type* inside them. For instance:

`a = ['hello', 'world']`

`b = [True, False]`

`c = [1.135235743, 8.9512057342, 41.4234]`

Lists can even share multiple different data types:

`d = [1, 2, 'hello', 'world', True, False, 1.135235743, 8.9512057342, 41.4234`

To make things even worse, lists can also contain other lists inside them (infinitely):

`e = [[1, 2], [3, 4]]`

This seems too complicated for some purposes, but it's actually quite useful. Consider processing a mono audio stream. As we know, audio is just a series of numbers, most often floating-point numbers. We could imagine a very short audio stream that looks like this:

`[0.0, 0.09280161904462148, 0.18560323808924295, 0.27840485714841634, 0.3712064761784859]`

What if we had a stereo signal though? If we're in stereo, we can use lists inside lists to help us. Our outer list will have two items. Left and Right channels. Our inner list will have the samples from each channel:

`[[0.0, 0.09280161904462148, -0.18560323808924295, 0.27840485714841634, 0.3712064761784859], [0.0, 0.1005799346968066, -0.2011598693936132, 0.3017398040904197, -0.4023197387872264]]`

This can help us organize our data more effectively. 

To access items of lists inside lists is quite intuitive:

`a = [[0.0, 0.09280161904462148, -0.18560323808924295, 0.27840485714841634, 0.3712064761784859], [0.0, 0.1005799346968066, -0.2011598693936132, 0.3017398040904197, -0.4023197387872264]]`

if we wanted to find the 3nd sample of the 2nd channel, we would write:

`a[1][2]`. 

In this case, that would be `0.1005799346968066`.

Several other things can be done to lists, but we won't get into those for today. There are also some third-party extensions to python that replace the functionality of lists, and we'll talk about one of these briefly in the next lesson.


Strings are essentially lists of characters. We can even access the characters of strings the same way we access items of lists:

`a = "hello world"`

`b = a[0]`

now `b` is equal to `'h'`.




##### Dictionaries  

Often times, we need to use python to relate one value to another. For instance, if we had a list of cars and the year they were made, we could store that data in a dictionary:

`a = {'toyota corolla': 1995, 'VW bug': 1965, 'Honda Pilot': 2001}`

We can access these values several ways, but the primary way is:

`b = a['toyota corolla']`

`print(b)`

would print `1995`.

We won't be using dictionaries today, but if you want to learn more, see any of the links at the bottom of this turorial.

<br/>


##### More about strings 

Strings in python are great. They allow us to do all sorts of things very easily using these extended functionalities:

    a = 'hello '
    b = 'world'

    c = a + b

as you've probably come to expect by now,`c` is `'hello world'`. the `+` operator simply tells the string to add the second string to the end of the first.

Similarly,

    a = 'hello '
    b = 'world'

    c = (a * 2) + b

now `c` is `'hello hello world'`. The `*` operator just repeats a string.

### Operators  

Operators in python consist of: `+`, `-`, `*`, `/`, `**`, `//`, `%`, `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `in`, `not in`. There are a few more that are useful in some cases, but we'll stick with these for now. 

#### Arithmetic Operators  

Python's arithmetic operators are `+`, `-`, `*`, `/`, `**`, `//`, `%`. The first four work just as you'd expect -- add, subtract, multiply, and divide. 

<br/>

`**` is the exponent operator. This works as expected: 


`a = 3`

`b = a**2`

`b` is now equal to 9.

<br/>

`//` is called floor division. If you're not familiar with it, floor division is just division that disregards everything after the decimal point. For instance:

`a = 12 // 5` 

`a` is now equal to 2, because 12 ÷ 5 = 2.4, and the floor returns the closest integer to the true value from below.

<br/>

`%` is the modulo operator. This returns the remainder of a division performed on the two inputs. It's incredibly useful for many purposes such as making very large numbers manageable. Let's use it:

`a = 12 % 3`

Because 12 ÷ 3 = 4, and has no remainder, `a` is equal to `0`.

If we have a huge number such as:

`a = 1230581235981275987192378569815`
and we want to see if it's divisible by 12000, we would run 

`b = a % 12000`. 

now `b` is equal to `1815`.

<br/>

#### Definition Operators 

We've already been using one definition operator all the time. `=` is the most self-explanitory definition operator. it simply sets the value of a variable equal to whatever is after it. The other definition operators are `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`. These are quite simply shortcuts for changing a value in terms of itself. Let's look:

<pre>
a = 1
b = 2
a = a + b
</pre>

at this point, it's clear that `a` is equal to 3. Let's try using the shortcut:

<pre>
a = 1
b = 2
a += b
</pre>

This does the exact same thing. The other operators just do their respective operations and work the exact same way otherwise. 

#### in and not in 

These are also very intuitive. If you have a list:

`a = [1, 2, 3, 4]`

and you wanted to check whether the number `0` is in the list, you could say:

`0 in a`

and it would return False. If you instead said

`1 in a`

it would return True. 

`not in` is simply the opposite of in:

`0 not in a`

is True,

`1 not in a` 

is False.

### Comparators  

Comparators are technically operators but they are used differently. Comparators, as it might seem, compare things. The comparators of Python are `==`, `!=`, `<=`, `<`, `>=`, and `>`. They make good sense. If `a = 20` and `b = 10`:

`a == b` returns False

`a != b` returns True

`a <= b` returns False

`a < b` returns False

`a >= b` returns True

`a > b` returns True

In words, they each mean:

`a == b` is `a` equal to `b`?

`a != b` is `a` unequal to `b`?

`a <= b` is `a` less than or equal to `b`?

`a < b` is `a` less than `b`?

`a >= b` is `a` greater or equal to `b`?

`a > b` is `a` greater than `b`?

They'll always return either `True` or `False`. 

The same rules apply to any other type than int.

NOTE: using `==` or `!=` on floats is generally a bad idea. Even if it seems to work, this can cause problems because of the implementation of floats in most languages, as they are inherently imprecise. 

<br/>
<br/>

### if, elif, else  

Often times during programming, we must change do certain operations based on certain conditions. For instance, in the example of a video game where it could be daytime or nighttime, we had this:

`is_daytime = False`

which indicates that it is night time. We might have a different background for our game if it's night or day. We could use `if` and `else` to change this background:


<pre>
if is_daytime:
   # set background image to day here
else:
    #set background image to night here
</pre>

In python, these sorts of statements depend on whitespace. each encapsulating `if`, `elif`, or `else` statement must be followed by a `:` and then each line that applies to it must be indented. There are **no brackets** like there are in other languages. The statement is over at the next unindented line. The same thing applies to function definitions, for and while loops, and several other cases. 

You can still nest these statements within one another, for instance:

<pre>
if is_daytime:
    if player_outside:
        # set background image to day here
    else:
        # player is inside
else:
    # set background image to night here
</pre>

The `if` and `elif` statements should be followed by a statement whose result is either `True` or `False`. While it is possible to use other values as input to an if statement, this can create problems when it comes to cross-platform and cross-version support. Avoid this if at all possible. 

(An exception to this case is that `while` loops which are supposed to act like `while True:` are often written as `while 1:`, inherited from the C language, which doesn't have boolean types and instead uses integers either 1 or 0 for True and False respectively.)


<br/>

### For and While  

Python offers two types of loops: for `loops` and `while` loops. For loops are formatted like this:

<pre>
for i in range(10):
    print(i)
</pre>

This statement is made up of a few new parts, so let's start with `range(10)`. This simply returns the list of integers counting up to 9 from 0. In this case, we would get `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` (in actuality it doesn't return a list exactly but that's okay for now.) If we ran:

<pre>
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)
</pre>

we would get 

<pre>
0
1
2
3
4
5
6
7
8
9
</pre>

The loop itself simply iterates through the list and loops until the list is over. 

<br/>

While loops are intuitive. They work like this:

<pre>
a = 40
while a > 0:
    a -= 1
</pre>

This code would count from 40 down to 0, and the loop would stop once the condition after `while` was False. 

It's often tempting to use `while` loops, but most of the time using a `for` loop is the best practice.

<br/>

The control flow of loops can be altered while in the loop using `break`, `continue`, and `pass`. 

`break` breaks out of a loop. if we ran:

<pre>
a = 0
while True:
    a += 1
    if a == 10:
        break
</pre>

the loop would count to 10 and then end. 


`continue` just skips the rest of an iteration of a loop, starting again from the top.

`pass` does nothing. This might seem useless, but it's useful when you need a placeholer. If I'm working on building a feature, I might set up my file and put `pass` where I'm not sure what will go there. This applies both to loops, if/else statements, functions, and more that we'll talk about soon.



<br/>
<br/>

### Functions

Okay, so now that we're through with the nuts and bolts, we can get to the good stuff: functions and classes. 

Functions are simply pieces of code that are meant to be reused. Instead of writing in every line of code to make a filter, for instance, you can simply write a function:

<pre>
def filter_audio(audio_to_filter, cutoff_frequency, slope):
    # some logic that filters the audio here


audioFiles = []
# put a bunch of audio files in audioFiles

for file in audioFiles:
    filter_audio(audio_to_filter, cutoff_frequency, slope)
</pre>

Functions are defined with `def` followed by the name of the function. Then, in parentheses, the function's arguments, then a `:`. A function can have no arguments, or as many as you'd like. The arguments can be any type. 

Argumnents are the inputs to a function. They are variables that are only used within the function. You cannot access them from any part of the code outside of the function. 

To get information back from a function, you can use the `return` keyword. 

Let's write a function that checks whether a number is divisible by three.

<pre>
def divisibleByThree(number):
    if number % 3 == 0:
        return True
    else:
        return False
</pre>

If we had this function, we could do the following:

`a = divisibleByThree(1)`

`b = divisibleByThree(6)`

`a` is now `False` and `b` is now `True`.

As you can see, when you want to use a function, you just use parentheses after it containing the arguments you'd like to give it.

Let's write a function that checks to see if someone has a class at a certain time. Here's what we'll start with:

We're given a list: `Schedule = []`

`Schedule` is filled with lists: `Schedule = [[], [], [], [], [], [], []]`

Each sub-list of Schedule represents a time block. For each class scheduled, another list is added with two integers: the start time and end time (we'll stick to on the the hours and not worry about minutes). For instance, if we had a class from 9 AM to 11 AM, our schedule would look like:

`Schedule = [[9, 11]]`

If we added another class from 2-4, we would see that:

`Schedule = [[9,11],[14,16]]`


If we wanted to make sure that a class isn't scheduled overlapping any other class, we could write a function. This function should make sure that our Schedule and our ClassTime fulfill a few characteristics:

1. The new class cannot *start* during an existing class
2. The new class cannot *end* during an existing class
3. The new class is a valid number of hours (i.e. non-negative, not exceeding 24, etc)

Let's call this function `AddClass`. It's arguments are `Schedule` and `NewClass`. We can see that `AddClass(Schedule, NewClass)` could be implemented like this:

<pre>
def AddClass(Schedule, NewClass):
    for Class in Schedule:
        if (NewClass[0] < Class[0] and NewClass[0] > Class[1]):
            # NewClass does not start during Class
        else:
            print('Error: NewClass starts during an existing Class')
            return 1

        if (NewClass[1] < Class[0] and NewClass[1] > Class[1]):
            # NewClass does not end during Class
        else:
            print('Error: NewClass ends during an existing Class')
            return 1

    print('NewClass doesn't interfere with any other classes. Adding class to schedule...')
    Schedule.append(NewClass)
</pre>

We could then add some helpful precautions to make sure that there are no random errors:

<pre>
def AddClass(Schedule, NewClass):
    for i in NewClass:
        if i > 24:
            print('NewClass contains a time higher than 24! Fix that.')
            return 1
        if i < 0: 
            print('NewClass contains a negative number. That doesn't make any sense.')
            return 1
        if type(i) != int:
            print('NewClass can only contain integers.')


    for Class in Schedule:
        if (NewClass[0] < Class[0] and NewClass[0] > Class[1]):
            # NewClass does not start during Class
        else:
            print('Error: NewClass starts during an existing Class')
            return 1

        if (NewClass[1] < Class[0] and NewClass[1] > Class[1]):
            # NewClass does not end during Class
        else:
            print('Error: NewClass ends during an existing Class')
            return 1

    print('NewClass doesn't interfere with any other classes. Adding class to schedule...')
    Schedule.append(NewClass)
</pre>



For an extra exercise, we can look at a recursive function. Recursive functions call themselves. This is sometimes a tedious mess, but other times it's necessary to solve a problem, or to solve it faster. For instance, if you'd like to try something else, come up with a non-recursive algorithm to come up with the nth member of the fibbonaci series. While it's possible, the fibbonaci series is an inherently recursive problem. The same is true of finding the factorial of a number. While there isn't necissarily a function that can only be defined recursively, there are functions that can only be defined recursively assuming there is a limited amount of memory. 

You may also know that any number whose digits add up to a number divisible by three is also divisible by three. Let's rewrite our function to use this rule. Before we do this, we must know one thing: we can use functions like `list()` and `str()` to make one type into another. For instance, `str(100)` is equal to `'100'`. We can similarly do `list('100')`, which returns `['1', '0', '0']`. Let's do that here:

<pre>
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
</pre>

Functions are the bread and butter of modern computing. Almost everything is done in a function. The new expansion built off of functions, however, are classes. 


<br/>
<br/>
<br/>
<br/>
<br/>
<br/>




### Review

At this point, we'll stop learning about Python basic concepts and begin talking about how we can use them. Let's look at a few problems: 

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

We can easily look at this problem and tell that we won't be able to solve it by hand. There are just too many numbers between 0 and 1000. Can you figure out how to do this? Write program that calculates the answer.

When you're done, modify your code so that it is in a function which finds the sum of all multiples of 3 and 5 between 0 and `n`. 

Then modify that function to find the sum of the multiples of any two positive integers `a` and `b` between 0 and `n`. 

