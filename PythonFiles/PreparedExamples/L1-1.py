# This file is a review of Python variable types, as well as a few simple commands. 

# this is a single-line comment

""" This is a 
multi-line
comment 

Comments are for human eyes only -- the interpreter doesn't see them and can't operate on the information inside them. 

Generally speaking, good programs have about equal amounts of comments and code.
This makes them more readable, which is especially important when working in a group.
"""

an_integer = 1

a_float = 1. # floats can be declared either with a decimal at the end of a number, a decimal followed by another number, or using the syntax float(1)
another_float = 1.0
yet_another_float = float(1)

a_string = "hello world" 
another_string = 'hello world' # strings can be declared with single or double quotations.

a_bool = True # booleans are capitalized -- True and False instead of true and false. 
another_bool = False

a_list = [] # lists are ordered sequences of items. Their items an have any type, including other lists.
a_list_of_ints = [1, 12, 32, 124, 134, 4501] 
a_list_of_ints.append(51204) # add 51204 to the end of the list

a = a_list_of_ints[0] # takes the first item of the list (1)
c = a_list_of_ints[3] # takes the fourth item of the list (124)
d = a_list_of_ints[-1] # takes the last item of the list (51204)

# we can also take slices of lists, more than one character long:
e = a_list_of_ints[0:2] # makes a list from the first item to the second ([1, 12]) NOTE: this is exclusive.


# we can also get characters from strings the same way we got items from lists:
a = a_string[0] # is 'h'

# strings also have some other special properties:
b = a_string + '!' # is 'hello world!'
c = a_string * 2 # is 'hello worldhello world'


a_dict = {} # this creates an empty dictionary. 
# The thing to remember about dictionaries is that they are made up of {key: value} pairs. You can ask the dictionary for a key's value.
a_dict['Berklee'] = 'College'
a_dict['UC Berkeley'] = 'University'

a = a_dict['Berklee'] # a is 'College'.

# we can also create a dictionary with items already in it using this syntax:
another_dict = {'Berklee': 'College', 'UC Berkeley': 'University', 'Monsters University': 'Bad Sequel'}


#
#
#
#
#
#

# Bonus material

# there are some other data types that you probably won't need to worry about, but for the sake of having everything in one place to reference, you can see them here:

# Complex numbers
a_complex = 1+2j
b_complex = 2+1j
c = a_complex + b_complex # 3+3j

# Tuples 
a_tuple = (1, 2, 3) # tuples are just like lists except that you can't update their contents later. 

# String special cases:
# sometimes you may be trying to write a ' or " character in a string. Do this by adding a \ in front of the ' or ":
another_string = 'hello, world. Don\'t worry, this string will work fine'
# we can imagine that this might cause issues itself because we may want to use the \ character in a string. Don't worry, this is as easy as:
yet_another_string = 'hello, here\'s a \\'
# for strings in which you're using a lot of ', \, or " characters, use this syntax to eliminate the need for \s:
more_strings = '''this string will include all the normally invalid characters: \ \ \ \ \ ' ' '' ' ' "" " until we give it the same triple quotes we started with'''
# if you want to add a new line or a tab character into the string, you can use: 
another_string = 'here are newlines \n and here are tabs \t'
# you can still use ''' ''' syntax to add newlines when you define the string:
more_strung = ''' here is a 
multiline
string
''' 


# sets, frozensets
# please don't worry about sets until you understand hash tables. They're a bit like lists but unordered, and they're faster at performing some operations like membership checking and removing duplicates. 


# None
# this represents nothing, which can be rather useful. For instance, if you make a function that has no return statement, it will return None.

# Byte
# bytes are raw binary data. They can be encoded and decoded easily.
