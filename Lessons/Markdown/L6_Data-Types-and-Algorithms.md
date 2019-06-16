# Data Types and Algorithms
#### Zachary Lewis-Towbes; BerkleeMakes; June 2019 



### What is an Algorithm? 

In popular culture, we describe anything we don't understand as an algorithm. While useful for describing things we don't understand, we use the term incorrectly. An algorithm is actually *a set of instructions to perform a process*. This is very vague, but it should be. Some algorithms are simple. For instance, addition is an algorithm. It performs the process of adding two numbers. Google PageRank is also an algorithm, and has made Google billions of dollars due to its complexity and secrecy. It performs the process of deciding at what ranking each web page will appear when a certain term is searched. 

Essentially, everything we do in a computer will be an algorithm or the result of an algorithm. We've already made several in this course. 

When discussing algorithms in a more formal context, however, we'll discuss a few specific aspects of algorithms:

* how can we measure the efficiency of an algorithm?
* what makes one algorithm different from another?
* how do we know it will work in every possible situation?
* just how much do I need to care about this? 

In most cases, we don't need to impolement our own algorithms. Generally speaking, for our purposes, other people have written great algorithms that probably will work better than ours. That said, knowing which of theirs to pick is crucial to the performance of our programs. 

### What is a Data Type?

We've already spoken about data types. In our first week we discussed the differences between `int`, `float`, `string`, `list`, and others. These are all indeed data types, but they are not the only data types we will use in Python. 

Data types are ways of storing data that make our algorithms either simpler or faster. There are literally hundreds of data types, and we'll barely scratch the surface.

In order to understand data types, there are a few things we should review. 

### Prerequisites

Before we take the deep dive on data types and algorithms, there are a few things we should know. 

#### Memory

We already know what memory is. It's a way of storing information in a non-permanent manner, and it allows access to that information much faster than a SSD or HDD. 

We can imagine memory as a series of bins. For our purposes, each bin contains one value -- if we're talking about a 32-bit float, the bin would be 32 bits wide, and if we're talking about a boolean value, the bin would be 1 bit wide (0 is False, 1 is True). It doesn't matter how wide, but we can imagine that our memory is a series of bins with a certain constant width. 

When we assign a variable, for instance:

	a = 1

the computer links our name `a` to *a location in memory* where the number 1 is assigned. We can visualize this below:

| Memory Location | 0 | 1 | 2 | 3 | 4 | 5 |
|-----------------|---|---|---|---|---|---|
| Value           |   |   |   |   |   |   |

Here we see some unassigned memory. Then we run:

	a = 1
	
| Memory Location | 0 | 1 | 2 | 3 | 4 | 5 |
|-----------------|---|---|---|---|---|---|
| Value           |   |   |   | 1 |   |   |

The language now knows that to find the value of `a`, it must look in bin 3.

The bin number here is called a *memory address*. For our purposes, a computer can access an item from a memory address instantly. We'll discuss this more later. 

#### Time
While it may be tempting to use the 	`time` module to perform tests on different algorithms, there are actually better ways to measure how much work our algorithms are doing. This is generally called *Algorithmic Time*. It is measured many ways, but let's introduce the idea.



## Algorithms Part I


If you have a list and need to find a certain item within that list, how would we do so? We'll discuss a few algorithms that perform this operation. They are called [Searching Algorithms](#search).

A few weeks ago we learned about the `List.sort()` method, which sorts a list into ascending order. We take for granted that this will successfully sort the list, but how exactly does it do so? There are hundreds of sorting algorithms, of which we'll talk about a few. 

Some of the first known algorithms were invented in ancient Greece. They were performed by hand and designed to perform multiple operations. A good example is the Sieve of Eratosthenes, which found all prime numbers up to a certain limit. Invented before 200 BCE, it is still one of the most efficient algorithms that performs this task today. There are common algorithms to check whether a number is prime and to find all prime numbers up to a given value. We'll talk about both. 

### Naive Algorithms 
#### Naive Searching Algorithms
If we have a list of numbers and we want to find the first instance of a certain value in the list, we can probably imagine a simple way of doing so. Assume the list is randomly ordered.

`n` is the thing we wish to find and `list` is the list we wish to search through. In this case, we are simply checking whether there is an item in a list.

	def search0(list, n):
		for i in list:
			if i == n:
				return True
				
		return False
	
If you guessed this, you're right. This is called linear search becasue we simply go through the list and check whether the value is there. 

If we wanted to instead return *where* in the list the item came up, or `False` if the item never came up, we could do so easily:

	def search1(list, n):
		location = 0
		for i in list:
			if i == n:
				return location
			location += 1
			
		return False
	
#### Naive Sorting Algorithms

Like many algorithms, the best way to learn about how sorting algorithms works is by doing it ourselves. We have some index cards with numbers written on them. Around 10-20 cards will do for this demonstration. 

First, take a randomly shuffled set of index cards and sort them from low to high yourself. How did you do this? 

#### How can we do better?

These algorithms are called naive because they are the simplest possible approaches to the problem. They may also be considered "brute-force". They are the thing we would do naturally by hand when trying to perform these tasks. There are many ways we can speed things up though. 

For instance, consider a professor handing back an assignment searching through the stack of papers for a particular student's paper. They'll generally go through each paper looking for the right name, and hand it in once they find it. How could we do this faster? 

Unfortunately, the answer is basically that we can't under these conditions. But can we change the conditions to make this problem easier to solve?

Yes. There's a great real-world correlate here: Filing cabinets. Assuming a filing cabinet has the student's papers in alphabetical order, how could we perform this task faster? 

There are several ways. One of the most common is searching forwards vs backwards. If your last name starts with an 'X', it wouldn't make much sense to start at the beginning. We could just start at the end and work backwards. 

There's another way we'll discuss shortly called Bisectional Searching (or Binary Searching), which works like this:

1. Start in the middle of the pile. 
2. If the item is alphabetically after the current letter you're on, move halfway towards the end of the pile (for example, move from the 1/2 mark to the 3/4 mark)
3. Otherwise, if the item is alphabetically before the current letter you're on, move halfway towards the start of the pile (for example, move from the 1/2 mark to the 1/4 mark)
4. Repeat steps 2 and 3 until you find the item.

While we don't necessarily need to, I'll implement this in python: 

	def bisectionSearch(A, n):
		""" A is the ordered list to search through, n is the value we're trying to find """
		location = len(A) // 2
		bounds = [0, len(A)] 
		for i in range(A):
			if n == A[Location]:
				return location
			elif n > A[location]:
				bounds[0] = location
				location += (bounds[1] - location) // 2
			elif n < A[Location]:
				bounds[1] = location
				location -= (bounds[0] + location) // 2
			else:
				# n was not found.
				return False 

Let's do this with flash cards. Start with an ordered 10 flash cards. Just like last time, count the number of times we go through the loop.

We'll see that on average, bisection search took fewer comparisons than our naive algorithm.

### Algorithmic Time

Let's think back to our **naive search** algorithm. How many times did we loop? Can we figure out how many times we would loop in the best and worst case? 

In the best case scenario, the first item of the list is the item we're looking for. In this case it would only need 1 loop.

In the worst case scenario, the last item of the list is the item we're looking for, or the item isn't in the list at all. In this case we would need as many loops as the length of the list, which we can call n.


**Bisection** search is faster though. Much faster. Again, n is the length of the list. 

In the best case, the item we're looking for is in the middle of the list. In this case we would only need 1 loop. 

In the worst case, the item we're looking for is either not present in the list or is one less than a power of 2. This might not make sense initially, but if you think about it, it makes sense. In the worst case, our algorithm performs ceil(log(n)) loops. 

In general, because we don't know what our algorithms will get in advance, we are worried about the worst case performance.

We generalize the performance of our algorithms using **Big-O Notation** which looks like **O()**. The contents of this O depend on the number of input values, in this case the length of the list. Using worst-case values, our naive search had O(n). Our Bisection search had O(log(n)). It's worth noting that this is designed to describe the behavior of an algorithm as n approaches infinity. If you're only searching through 10 values at a time, the difference will be minimal. If you're searching through a massive dataset such as the names of everybody in the world, an O(n) algorithm might take millions of times longer than an O(log(n)) algorithm. 

While this course will not cover the methods used to derive algorithmic time in all cases, we aim to have an understanding of the performance of other algorithms when we try to create our own programs. 

There are several common O() values: 

* O(1)
* O(logn)
* O(nlogn)
* O(n)
* O(n**2)
* O(n!)

They grow in this order. In short, if you must pick between two algorithms, the choice higher on this list will perform better for most cases. 

### Why have naive algorithms then? 

So, if we had to pick between bisection search and naive search, we would pick bisection search, right? 

It's crucial to understand that these two algorithms *don't actually solve the same problem*. Let's look at their inputs and outputs:


Naive Search

Input: Any list of items, an item to search for.

Output: The location of the item.


Bisection Search

Input: An **ordered** list of items, an item to search for

Output: The location of the item. 



**This is why we have data structures**. 

An ordered list is a different data structure from an unordered list. 


## Data Structures 

Now that we know how much faster bisection search is, and because bisection search requires a sorted list as an input, we might want to keep any list that we need to search over sorted. As an example, let's make a class called SortedList:

	class SortedList:
		def __init__(self, items): 
			""" Initializes SortedList """
			self.contents = [].extend(items)
			self.contents.sort()
		
		def append(self, i):
			""" Appends i to SortedList """
			self.contents.append(i)
			self.contents.sort()
		
		def extend(self, I):
			""" appends all values in list I to SortedList """
			self.contents.extend(I)
			self.contents.sort()
			
		def pop(self, i=-1):	
			return self.contents.pop(i)
			
		def min(self):
			""" gets minimum value of SortedList """
			return self.contents[0]
			
		def max(self):
			""" gets maximum value of SortedList """
			return self.contents[-1]
			
		def find(self, n): 
			""" finds item n in SortedList; returns location using bisection sort (O(logn))"""
		
			location = len(self.contents) // 2
			bounds = [0, len(self.contents)]
			 
			for i in range(self.contents):
				if n == self.contents[Location]:
					return location
				elif n > self.contents[location]:
					bounds[0] = location
					location += (bounds[1] - location) // 2
				elif n < self.contents[Location]:
					bounds[1] = location
					location -= (bounds[0] + location) // 2
				else:
					# n was not found.
					return False 


By sorting the list every time we add something to it, we ensure that the list is always sorted. This makes finding a value in the list much faster. 

The trade off is that it makes adding items to the list slower -- remember that we have to sort the list each time we add values.

### Stacks

If you stack up books on a table, you've made a stack. Essentially a stack is a series of items with the property that:

* if you add something to the stack, it gets placed on top.
* if you remove something from the stack, you get the top item.

In other words, a stack is First-In Last-Out (FILO). 

They're useful for all sorts of things. For instance, if you had an application with an undo button, you'd need to store a list of previous items in such a way that you could store a user's actions in reverse-chronological order. 

### Queues

Unlike a stack, a queue is First-in First-Out (FIFO). 

* if you add an item to a queue, it gets placed on top.
* if you remove something from the queue, you get the bottom item.

A purpose for a queue might be an audio unit plugin. The DAW sends buffers of samples to the plugin, which stores them in a queue. When the DAW begins playback, the plugin reads from the oldest buffer in the queue because the plugin needs to process the audio in the order it occurs.

### Arrays

This is normally when we would introduce Linked Lists, but you already know what they are.

Arrays are sequences that are sequentially stored in memory. When we create an array, it is allocated in sequential memory locations. That means that if an array starts at location *m* in memory, the list's *n*th item is located at *m + n*. 

In this case, we can describe the worst-case running time of the algorithm as O(1) (AKA Constant time). In a constant time operation, no matter how large the value n (in this case, no matter how far into an array an item might be, the operation would take the same amount of time. 

Our lists in Python are not arrays but they are **dynamic arrays** which is a challenging concept to get behind. Essentially, Python lists are very fast to access values from (a task called indexing) but are slow to resize. They also waste a fair amount of memory. While this isn't a huge deal for us it can become problematic when using large audio datasets (see: MlExample.py). While its big-O algorithmic time is the same O(1) for indexing, it is still slower in terms of absolute time, and for this reason it is used much more often especially where efficiency counts. 

### Trees

Trees are what you might imagine. Just like family trees, they are made up of nodes and edges. We won't implement any ourselves, but you might see that if you make sure that a tree's items have certain properties, you can exploit these to perform certain tasks well. For instance, what if we had a tree which maintained the property that: 

* Each node may only have two children. 
* Each node must have children arranged such that the left child is less than the right child. 

This is, it turns out, an important idea in sorting lists. Let's jump back into algorithms to discuss the way we can use this data structure to sort lists. 

## Algorithms Part II

Data structures and Algorithms are inherently connected. Normally an algorithm is linked deeply with its implementation in a data type and vice versa. Because this is a very limited lesson on data structures and algorithms, we will just discuss one such example: Sorting algorithms

Let's take a look at a simple sorting algorithm.

### Naive sorting


##### Insertion sort

Most likely, you performed these steps:

1. Look for the lowest item
2. Put it in the front
3. Repeat steps 1-2 until the list is sorted.

This is called selection sort. Can we make this happen using lists in Python? Do this without using min(list).

	def selectionSort(A):
		for i in range(len(A)-1):
		
			# finds lowest value of the rest of the array
			min_location = i
			for j in range(i+1, len(A)):
				if A[min_location] > A[j]:
					min_location = j
			
			A[i], A[min_location] = A[min_location], A[i]
			
		return A
		
We can!


### Smart Sorting

#### MergeSort

Mergesort 