# Introduction to Programming for Audio 
#### Zachary Lewis-Towbes; BerkleeMakes; May 2019

<br/>

### Contents

1. [Goals](#Goals)
2. [What is a Computer?](#Computer)
3. [What is a Programming Language?](#Language)
4. [Why should I learn to code (in Python)](#Why)
5. [How to use the Terminal](#Terminal)
6. [Programming Baiscs](#Basics)
	* [Variables](#vars)
	* [Operators](#ops)
	* [Control Flow](#flow)
	* [Functions](#funcs)
7. [Appendix A: Git](#AppA)
	* [Making a new Repository](#newRepo)
	* [Logging Changes](#log)
	* [Updating from Github](#pull)
	* [Staging and Committing](#stage)
	* [Pushing to Remotes](#remotes)
	* [Branches](#branches)
	* [Other Resources](#other)
8. [Appendix B: Digital Audio Review](#AppB)
9. [Appendix C: Processors Review](#AppC)
10. [Appendix D: Words to Know](#AppD)

<a name="Goals"> </a>
### Goals

By the end of this lesson, you'll:
	
* Understand the concept of low- and high-level programming languages
* Understand the very basics of computing at a low level
* Learn about some of the uses of software in audio
* Learn the basics of the Mac and/or Linux command line (Terminal)
* 15-minute programming overview 
* Appendix A: Git
* Appendix B: Digital Audio Review
* Appendix C: Processors Review
* Appendix D: Words to Know

<a name="Computer"> </a>
### What is a Computer?

While this may be review for some people, let's clarify exactly how our computer works. 

The main functional components of a computer for our purposes are the Processor, the Memory, and the Storage. 

**Memory** is where our computer stores information it is using. It's relatively fast to read data from memory. We can imagine memory as an array of bins of which we can read and edit the contents. When you turn off your computer, the contents of the memory is deleted. This is why it's called *volatile* storage.

The **Processor** is where all of the processing happens. Simply speaking, the processor takes information from memory and manipulates it. It might add two values, compare them, or perform any number of other operations. 

The **Storage** is meant for keeping information that must remain even after the system is powered off and on again. It is where any files you save go. It's much slower than memory and it is generally not of too much concern to us when we're writing simple programs. 

A crucial thing to understand is that when we write code in Python (or any other programming language), the processor is what executes that code. Even though the processor runs our Python code when we tell it to, it doesn't actually understand Python. 

The processor actually only understands **machine langauge** or **machine code**. Each different brand and model of processor has its own machine language, and they are all expressed in literal 1's and 0's. The intricacies of how this works are irrelevent, but we need to understand the difference between writing machine language and writing something like Python. 

<a name="Langauge"> </a>
### What is a Programming Language? 

A programming language is a way of instructing a computer to perform specific operations and tasks.

The first programming languages were machine languages. Programmers literally sat around typing ones and zeros until their program was complete. This was very tedious, however, and was quickly replaced with something called assembler. Assembler was just like machine language, except that it was written in human-readable text. Assemblers are still used today. 

But when we think of modern programming languages, we don't consider having to work with machine language or assembler. We use languages more like C or Python.

In Python, to add two numbers a and b, we would write:
	
	a = 83
	b = -2
	c = a + b

In a particular version of machine language, we might use:

	0010 0001 0000 0100
	0001 0001 0000 0101
	0011 0001 0000 0110
	0111 0000 0000 0001
	0000 0000 0101 0011
	1111 1111 1111 1110
	0000 0000 0000 0000
	
This is obviously much more difficult than the Python version. 

This example is a great way to understand why we have so many different programming languages. We can imagine that some of these languages are closer to `a + b` and others are closer to machine language. 

Languages that are closer to machine language are **less abstract** and those closer to Python are **more abstract**. We describe this abstraction as **low-level** to **high-level**. Lower-level languages are closer to machine code and higher-level lagnuages are more like Python.

You may be thinking, "If there are high-level languages that are so easy to write in, why do we have low-level languages at all?" This is a very real question, and one that many people ask. There are many answers, but in general, lower-level languages perform the same tasks faster than higher-level languages. Additionally, in very-low-level languages, programmers can take advantage of the finer control of the hardware that low-level languages offer. 

For our purposes, high-level languages are plenty. Python is a higher-level language than C. We'll use Python for all sorts of things, but in general, "mission critical" applications should be written in languages like C as opposed to Python.

So what is a programming language for our purposes? 

A programming language is a means of instructing a computer to perform specific operations and tasks, and is readable by both humans and computers.

Python is among the highest-level languages around. In Python, you never need to interact directly with the hardware. This will make learning it much easier than something like C or an assembler. 

<a name="Why"> </a>
### Why should I learn to code (in Python)? 

Besides simply the joy of learning something new, programming can be valuable to everyone, even musicians and producers. For one thing, many positions at music tech companies use Python, either as a means of analyzing data, automating tasks such as advertisement campaigns, and testing music software. Python is even increasingly becoming popular in the web development world. 

Sometimes, you might have an idea for a sound that you want to make, but can't figure out how to using plugins or Max. You might be able to build this sort of program in Python to process audio offline. 

Python is also a great starter language to get into languages like Java and C++, which are commonly used in audio software. 

Python is among the leading languages of the Machine Learning world, which opens all sorts of opportunities for musicians and engineers. 

Even if you aren't interested in working for tech companies, learning Python can be very valuable to all sorts of employers, from advertising companies that need to analyze datasets of advertisement interactions to stores that need to keep track of their inventories.


<a name="Terminal"> </a>
### How to use the Terminal

First, let’s get familiar with the terminal. The terminal is a way for you to interact with your computer with very simple instructions.

We can do so many things with the terminal that we won’t get into today, but let’s figure out a few very basics.

One of the most simple features of the terminal is the ability to move around the filesystem and its folders. Let’s open up a terminal and figure this out.

Once your terminal is open, type 

`cd ~/Desktop`

And then 

`ls`

You should see a list of the files and folders on your desktop. 
Next, type

`mkdir python `

And then again type

`ls `

You’ll see a new addition to the list of items on your desktop, a folder called “python”. We just made a new folder from the command line. “mkdir” stands for “make directory”, and “directory” is just another name for “folder”.

We can go in finder to our desktop and confirm that there’s an empty folder there called python. 

Now, let’s try something else. Type:

`pwd`

This will give us something like Users/<username>/Desktop. 
This just tells us that we’re on the desktop. “pwd” stands for “Print Working Directory”. It tells us where we are. Let’s go to the folder we just made using a new command “cd”. “cd” stands for “Change Directory”. This will let us move from one folder to another. We want to change to our new “python” directory. We do this with

`cd python`

Now if we type

`pwd`

We’ll see Users/<username>/Desktop/python. This means we’ve moved to our new python directory.
If you want to move backwards, you can use:

`cd ../`

Which will bring us to Users/<username>/Desktop, and we can string “../” together repeatedly to move back multiple directories:

`cd ../../`

Which would bring us to Users.

This is just a very basic introduction, but the Terminal is great, and can be used to replace Finder. We will use it to run Python files and read what we print from Python.



<a name="Basics"> </a>
### 15-minute Programming Basics 

* [Variables](#vars)
* [Operators](#ops)
* [Control Flow](#flow)
* [Functions](#funcs)

Here are a few very quick concepts that will be part of almost any programming language you learn. We'll learn them in Python soon. This should be used as a reference and not thought of as an introduction to these concepts. 

<a name="vars"> </a>
#### Variables

A **variable** is a place where we store a piece of information. For instance, if we're making a clock, we'd have to store the time in hours, minutes, and seconds: `time_hours = 12` `time_minutes = 23` `time_seconds = 41` would represent the time 12:23:41.

All variables have a **type**, which tells the computer how the variable should be represented. For instance, most languages have an `int` type, which covers whole numbers, and a `float` type, which covers numbers with decimals. 

Some languages like C require that you tell it what type you're using in advance, while Python tries to figure it out without your input.

<a name="ops"> </a>
#### Operators

**Operators** are symbols that represent actions or processes. We know a bunch of operators because they're very intuitive: `1 + 2` uses the `+` operator, which represents the process of addition. In english, we could say "the `+` operator should give me the sum of the number before it and the number after it". The same goes for `-` for subtraction, `*` for multiplication, and `/` for division. Commonly, `**` is used for exponents, so that `4**2` is "four squared" or `16`.

Most languages have `%` which is called "modulo" or "mod". If you've never heard of it, `a % b` returns *the remainder* after dividing a by b. For instance, `12 % 4` is `0` because twelve divided by four is three, and three times four is twelve. `12 % 5` takes the remainder of `12 / 5`, which is `2`. 

The operators we've discussed so far are **arithmetic operators**. They are so called because they perform arithmetic operations. There are other operators in every language though. 

**Boolean logic** is a fancy name for logic performed on the values `True` and `False`. Boolean logical operators often include `and`, and `or`. These work like this: `a and b` is `True` if and only if *both* `a` and `b` are 	`True`, and is `False` otherwise. `a or b` is True if and only if *either* `a` and `b` are `True`, and is `False` only if `a` and `b` are both `False`.

There is also `not`, which only operates on one input, and works like this: `not a` is `False` if `a` is `True` and is `True` if `a` is `False`. In short, it returns the opposite of the input. 

Note: `and` is often replaced by the symbol `&&`, `or` by `||`, and `not` by `!`.

Other common boolean operators are `xor`, and `nand`, which are both built on the above three.


**Definition operators** are used to define the value of variables. This might seem obvious, but the operator `=` represents an action, specifically the action of setting a variable to a value. In english, this might be described as "set the value of the variable to the left of `=` to the value to the right of `=`. Note: most languages have shorthand operators that look like this: `+=`, `-=`, `*=`, and `/=`. `a += b` is just shorthand for `a = a + b`. This is very useful.

**Comparators** are a type of operator that compares two or more values. For instance, `a == b` checks whether `a` is equal to `b`, returning `True` if they are equivalent, and `False` if they are not. Other comparators are: `<`, `<=`, `>`, `>=`, and `!=`. The first four should be relatively evident, and `a != b` is equivalent to `not (a == b)`, returning `True` if `a` is not equal to `b` and `False` otherwise.

<a name="flow"> </a>
#### Control Flow

**Control flow** is the order in which statements are processed. This order can normally be manipulated with `if` statements, `if...else` statements, and `if...elif...else` statements. During the program's execution, when an `if` statement comes up, the following block of code will be executed only if whatever follows the `if` statement is `True`. For instance, 

	a = 1
	if a == 1:
		print "hello!"
	
This program would print `hello!` because `1` is equal to `1`. 

	a = 2
	if a == 1:
		print "hello!"

This program would not print `hello!` because `2` is not equal to `1`.

	a = 2
	if a == 1:
		print "hello!"
		
	else:
		print "goodbye."
		
This program would print `goodbye.` because `2` is not equal to `1`.

	a = 2
	if a == 1:
		print "hello!"
	elif a == 2:
		print "hey!"
	else:
		print "goodbye."
		
This program would print `hey!` because `2` is not equal to `1` and because `2` is equal to `2`.

	a = 3
	if a == 1:
		print "hello!"
	elif a == 2:
		print "hey!"
	else:
		print "goodbye."
		
This program would print `goodbye.` because `3` is not equal to `1` or `2`.
 
<a name="funcs"> </a>
#### Functions

**Functions** are blocks of code that you plan to use later. They can have **arguments**, or variables that they depend on, and they can have **results** which can be passed on.

Functions are not run unless they are called. You can have a huge function at the top of your file but if you never tell it to run (call, or invoke it) it will lay dormant. Functions are normally called like this: if you have a function `f(a)` with one argument `a`, you would run it with `f(1)` or `f(10124012)`. The point is you can change the argument and it will change the behavior of the function. We'll discuss functions at length while introducing Python.

<a name="AppA"> </a>
### Appendix A: Git

* [Making a new Repository](#newRepo)
* [Logging Changes](#log)
* [Updating from Github](#pull)
* [Staging and Committing](#stage)
* [Pushing to Remotes](#remotes)
* [Branches](#branches)
* [Other Resources](#other)

Git is a backup and collaboration tool for individuals and groups working together on software and hardware projects. GitHub is a particular platform on which a user can make use of Git features. 

Git repositories can be interacted with both via the command line and via the GitHub Desktop app, but most users become proficient with using the command line because it doesn't require you to download an extra piece of software and can be used on remote servers where you don't have access to anything but a terminal.

Git does this by recording the changes you've made to a file rather than the file itself. This is why a focus is put on the lines added and removed from a project during any commit. This system makes two things easier: First, a user can revert to any previous commit. Say your software worked well yesterday, but now it's broken. If you're simply editing a file on your computer, you have no way of looking through your past actions. With Git, you can simply use `git revert` to revert to a previous commit. Second, GitHub doesn't need to store large amounts of data to store simple changes, as it only records the differences between files as opposed to the files themselves. These differences can be read directly using `git diff`, which is useful to check the differences between files.

 
<a name="newRepo"> </a>
#### Making a New Repository 

A new Repository (Repo) can be created by executing 
`git init` 
in the directory where you'd like your repo to be stored locally. 

On Github Desktop, the same action can be performed by clicking "Current Repository" on the top left, and then "add", and then "create new repository".

A repo can also be downloaded from github using `git clone` followed by the URL of the GitHub page you'd like to download. This differs from simply downloading the project in that the cloned repository can be edited and changed from your machine.

On Github Desktop, the same action can be perforemd by clicking "Current Repository on the top left, and then "add", and then "clone repository". This will allow you to input the URL of the GitHub repo you'd like to clone and the destination you'd like to clone it to.

 
<a name="logs"> </a>
#### Logging Changes

Git has a simple feature that allows you to see the previous commits of a project. In a local GitHub repo, execute `git log` to see the log of previous commits. 

On Github Desktop, the same feature is available in the "History" pane.

 
<a name="pull"> </a>
#### Updating from GitHub

The changes made by other users to a repository aren't automatically downloaded to your computer. To initiate this process, the user must run `git pull` in a git repository. 

Whenever your repository is behind the online copy in Github Desktop, a "Fetch Origin" button appears on the top right, allowing you to achieve the same functionality. 

note: `git pull` actually performs `git fetch` and then `git merge`, changing your local repository to match the copy on the web. If you'd just like to see what's new on the web copy without changing your content, simply run `git fetch`.

 
<a name="stage"> </a>
#### Staging and Committing

While it might seem from using Github Desktop that committing is simply a transaction between the folder on your computer and the copy on the web, it is actually a little more complicated than that. 

Before a commit is put on the internet at all, two things happen:

* First, the changes are staged for committing. This is done with `git add`. It can either specify a certain file or all files in the directory. For instance, if you only want to commit changes to a specific folder within your repository, say "myFolder", you could run `git add myFolder`. If you instead wanted to stage all changes to commit them, you could run `git add .`, where `.` is the terminal's way of saying "this folder". This is called staging because `git add` stages changes to be committed.

* Next, the changes are committed to HEAD using `git commit`. All commits should be given a message describing why they're being made for future reference, and this is done with `git commit -m "put your message here"`. This also doesn't change anything on the web at all. It simply changes the local representation of the repository on your computer, at a location called HEAD. This is called committing because `git commit` updates your computer's tree of edits that have been performed on a repository. It is stored at .git/head.


These are the steps that the "Commit" button does on GitHub Desktop. It doesn't interact with the web at all. Instead, to change the copy on the web (aka the **remote**), we must "push".

 
<a name="remotes"> </a>
#### Pushing to remotes 

The web server that takes your commit and stores it in a long list of commits from various users is called a remote. To actually put your changes on the remote server, you must run `git push origin master`, or replace `master` with the branch of your choice. 

 
<a name="branches"> </a>
#### Branches

One particularly useful feature of Git is the ability to make **branches** which each have a certain feature or property. For instance, if I'm working on the UI of a plugin and my friend is working on the processing inside, we can each make a branch. Then, when we're both done, we can merge these two together. Usually, when working on separate parts of a file or separate files, this merge process goes smoothly. To make a branch, you can use either the GitHub Desktop app or the command line. A project can have many branches that sometimes merge together or break apart. The central branch is called **master** and is where your commits will go if no other branch is specified. branches exist as separate until a `merge` is executed.

To make a branch, you must run `git branch` followed by the name of the new branch.

To make a branch in the Github Desktop app, simply click on "Current Branch" in the top bar and then click "new branch".

To move from one branch to another, you can run `git checkout` followed by the name of the branch. 

To checkout a branch in the Github Desktop app, click "Current Branch" and then click on the branch you'd like to checkout.

To see a list of the branches in your repository, use `git branch --list`.

To delete a branch in your repository, use `git branch -d` followed by the name of the branch to be deleted. Only do this if you know you're okay with losing the contents.

When you're done working on a branch that's separate from the master, you can merge the branch into master. First, use `git diff` followed by the source branch and then the target branch. In this case, if we wanted to merge `mybranch` to `master` we would run `git diff mybranch master`. This would show us the differences between branches, and effectively would allow us to preview the changes that our merge will make. Then, we would make sure we're at the destination branch using `git checkout`. In this case, because we're merging to `master`, we would run `git checkout master`. Then finally we can run `git merge mybranch`. Assuming there are no conflicts between branches, the merge will occur.

To merge a branch on GitHub Desktop, click "Current Branch" and then "Choose a branch to merge into...".

<a name="other"> </a>
#### Other Resources 

There are many great online guides to Git, from a very simple one [here](http://rogerdudler.github.io/git-guide/) to a slightly more detailed one [here](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61). There is also a great [codecademy course](https://www.codecademy.com/learn/learn-git) on Git.





<a name="AppB"> </a>
### Appendix B: Digital Audio Review

Many of you probably already understand this, but I'll review the basics of Digital Audio for those who are new to the idea. 

*Digital audio is a representation of sound, which is a representation of pressure*. Pressure waves in the air create the sound that we hear. Specifically, we can hear sounds that are between 20Hz and 20,000Hz. We can record this sound using a microphone, which measures the displacement of this pressure wave. Analog audio is simply the electrical signal that represents where the microphone's capsule was at any given point in time. 

Digital Sampling Theory is the study of how we can take this analog signal and store it digitally. Essentially, many thousands of times a second, the computer asks the microphone (or other analog audio signal) for the location of the pressure wave. This is then converted into a digital value by the **Analog-Digital Converter (ADC)**. The rate at which the ADC checks the microphone is called the sampling rate. 

Because of Nyquist's theorum, which we won't get into now, this rate must be at least two times the highest frequency that we need to reproduce. For instance, at a sampling rate of 16,000Hz, a converter could reproduce sounds up to 8000Hz. To cover the audio range of 20Hz to 20kHz, we must sample at least 40,000 times per second. Common sampling rates are 44,100Hz, 48000Hz, and their integer multiples. 

The ADC is limited by both the sampling rate and the **bit depth**. Bit depth is the amount of data that is stored in each sample. A 16-bit audio file (CD quality) uses 131072 possible values (from -65,536 to 65,536; derived by 2^16) and a 24-bit audio file uses 33,554,432 possible values (from -16,777,216 to 16,777,216; derived by 2^24). Most of the time, we'll see audio represented as **floating point** values, scaled between -1.0 and 1.0. This makes processing much easier, and loses no precision (floats are normally 32-bit).

This means that an audio file is just a long stream of numbers between -1.0 and 1.0. Its length is the length of the audio in seconds times the sampling rate. When we process audio files, we normally loop through every single value of this list and then do something to them. 

Upon playback, the digital signal is converted back into an analog signal in the **Digital-Analog Converter (DAC)**, which takes our digital file and recreates an analog equivalent. 






<a name="AppC"> </a>
### Appendix C: Processers Review

While most of you have used these tools, it's worth rehashing. 

#### Equalizer

#### Compressor

#### Limiter

#### Reverb

#### Delay

#### Pitch Shift

<a name="AppD"> </a>
### Appendix D: Words to Know

* Instance. An instance is one particular occurrence of a program or a function. 
* RAM. Random-Access Memory, the type of memory we have in our computers. 
* Boolean Logic. A type of logic that uses only values True or False (or 0 and 1).
* Operator. A symbol that represents an action or process.
* 