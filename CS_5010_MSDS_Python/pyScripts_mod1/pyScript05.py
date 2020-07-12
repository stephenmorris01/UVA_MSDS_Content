# File: pyScript05.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Numbers, strings, lists, dictionaries, tuples

## Numbers: built in mathematical functions
# -- pow : power
print(pow(2,3)) # 2 raised to 3 = 8

# -- abs : absolute value
print(abs(-2)) # returns 2, the absolute value of its argument

# -- round : rounding up or down its argument (to closest whole number)
print(round(2.8)) # rounds up to 3.0
print(round(1.1)) # rounds down to 1.0

print("==================================")

## Importing math functions
import math # Typically best to put this line of code at the TOP of the file
print(math.sqrt(12)) # using the square-root function from the math library

print(math.floor(2.5)) # returns largest whole number less than the argument
print(math.floor(2.9))
print(math.floor(2.1))

# Literature will give a full list of all mathematical functions

print("==================================")

## Importing Random - for random number generation
import random # Typically best to put this line of code at the TOP of the file
print(random.random()) # using random() function in random library
    # will return a number between 0 and 1
                       
print(random.randint(1,100)) # specify a range in the parenthesis
    # this will return a random integer in the range 1-100
    
print("==================================")

## Strings
myString = 'hello, world!'

# -- String concatenation
my2ndString = myString + ' Goodbye, world!'
print(my2ndString)

# -- len : built-in length funciton tells us how many characters in the string
print(len(my2ndString))

# -- Indexing
# Strings are sequences in Python where each character of the string has a 
#  unique position

print(myString[0]) # displays the first character of the string
                  # first position is position zero. Will display 'h'
                
print(myString[0:4]) # First four characters (index positions 0-3)
print(myString[:4]) # Beginning (0) to (n-1) position
print(myString[4:]) # Fifth character and onwards until the end of the string

# -- repetition
print(myString*2)                     

print("==================================")    

## Split a string based on a delimiter using split() function
montyPythonQuote = 'are.you.suggesting.coconuts.migrate'
print(montyPythonQuote)
print(montyPythonQuote.split('.')) # split by the '.' delimiter. Result: a list!

print("==================================")

## Strip out extra whitespace using strip(), rstrip() and lstrip() functions
str1 = '  hello, world!'    # white space at the beginning
str2 = '  hello, world!  '  # white space at both ends
str3 = 'hello, world!  '    # white space at the end

# strip() function removes white space from anywhere
# rstrip() only removes white space from the right-hand-side of the string
# lstrip() only removes white space from the left-hand-side of the string
print(str1.lstrip())
print(str1.rstrip())
print(str2.strip())
print(str2.rstrip())
print(str2.lstrip())
print(str3.rstrip())
# Try these examples using the interactive shell (don't use the print functions)
# for a better idea at how the strip() function works  E.g.:
# In [27]: str2.lstrip()
# Out[27]: 'hello, world!  '
# You can see the white space remaining on the right-hand-side 

print("==================================")

## List structure -- [] -- uses square brackets
numbers = [1,2,3,4] # Creates a list called numbers with the values 1,2,3,4
print(numbers[0]) # Access first element (output: 1)
print(numbers[0] + numbers[3]) # doing arithmetic with the values (output: 5)
# -- slice
print(numbers[0:2]) # Output: [1, 2]
print(numbers[1:3]) # Output: [2, 3]
print(len(numbers)) # use len() function to find the size. Output: 4
print(numbers[2:])  # Output: [3, 4]
print(numbers*2)    # Output: [1, 2, 3, 4, 1, 2, 3, 4]
numbers2 = [30,40,50]
print(numbers + numbers2) # concatenate two lists. 
                          # Output: [1, 2, 3, 4, 30, 40, 50]
# -- can mix types:                          
myList = ['coconuts', 777, 7.25, 'Sir Robin', 80.0, True]
print(myList)

# -- nested lists
names = ['Darrell', 'Clayton', ['Billie Jean'], 'Samantha']
print(names[2]) # returns a *list*
print(names[0]) # returns a *string*

print("==================================")

## Dictionary structure -- {} -- uses curly brackets
# Is like a hash table. Has key-value pairs.
phonelist = {'Tom':123, 'Bob':456, 'Sam':897}

# -- retrieve a value - just write a key as the *index*
print(phonelist['Bob'])

# -- print list of keys, or print list of values
# use keys() or values() functions
# No ordering in a dictionary
print(phonelist.keys())
print(phonelist.values())
print(phonelist) # note the data returned is not the same as the data entered
print("Using 'in' to check if the key 'Sam' is in the dictionary (answer: True)")
print('Sam' in phonelist)

print("==================================")

## Tuple structure -- () -- uses parenthesis
numbers = (1,2,3,4) # numbers 1,2,3,4 stored in a tuple
print(len(numbers)) # size
# ... you can do all operations just like a list...

# a tuple is like a list but with one big difference
# *** A tuple is an immutable object! ***
# Can't change a tuple once it's created
# numbers[0] = 5 # Trying to assign a new value 5 to the first position
# If you uncomment the above, you will get an error
# Error message:  TypeError: 'tuple' object does not support item assignment 

print("==================================")

