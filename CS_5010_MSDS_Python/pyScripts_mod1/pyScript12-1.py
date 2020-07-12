# File: pyScript12.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Iterators (with files, dictionaries, and tuples)

## Iterators
# An iterator is an object that allows you to traverse a sequence of data,
# such as a list, dictionary, tuple, or file

# The typical way to extract each element of a sequence like a list is:
numbers = [1,2,3]
for number in numbers:
    print(number)
    
# When executing a for-loop, internally an iterator is created
# It automatically points to the FIRST element of the sequence 
# The iterator knows if it is at the END of the sequence

# the for-loop controls the iterations, the iterator is actually controlling
# the traversal through the list

print("-----------------")

## Using "iter" and "next" for iterations
# -- Creating an explicit iterator (not an implied/internal one as in 
#    a for-loop)

# Using   it = iter(numbers)  creating a variable and call the
#                           function "iter" with a sequence of data
# To display the element use the "next" function with the iterator
# object as the argument to next.

numbers = [1,2,3]
it = iter(numbers)
print(next(it))  # will print 1
print(next(it))  # will print 2
print(next(it))  # will print 3
#print(next(it))  # should cause an error
# Behaves exactly like the for-loop above. But error will occur
# if you try to access the 'next' element with the iterator!

print("===========================================")

# -- iterator using files
# Files are handled the same way as lists, except a file object *IS* an iterator

# Create a file object fileIt
fileIt = open('w2filegrades.txt', 'r')     # open file for reading ('r')
# Call next function on the file iterator
print("Display first element of the file:")
print(next(fileIt))  # should display first element of the file, it adds a newline
# NOTICE - did not use the iter function with the file object since
# ** the file object is automatically set up as an iterator **


print("===========================================")

# -- Iterators and dictionaries

# The usual way to loop through a dictionary
# Pull each key from keys() function, and print the key and the value
# associated with the key by indexing into the dictionary
grades = {'Catherine':88, 'Darrell':77, 'Clayton':99}
for key in grades.keys():   # Note: for key in grades:   will also work
   print(key, grades[key])
   
print("-----------------")
   
it = iter(grades)
print(next(it))  # Gets a key and prints it
print(next(it))  # Gets another key and prints it
var1 = next(it)  # Gets the last key
print(var1, grades[var1])  # print the key and its associated value

print("===========================================")

# -- iterator with tuples

# Define a square by its points (x,y) coordinates:
square = ((10,8), (10,23), (25,23), (25,8))
# The usual way, using a for-loop:
#for points in square:
#   print(points)
squareit = iter(square)  # pass the tuple as the argument to the iterator
print(next(squareit))
print(next(squareit))
print(next(squareit))
print(next(squareit))

# Output:
# (10, 8)
# (10, 23)
# (25, 23)
# (25, 8)

print("===========================================")

