# File: pyScript15.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:

#   - Higher-order functions
#       o Map
#       o Filter
#       o Reduce


# ** Map **
#    Takes a function and applies it to *all* of the elements
#    of a given sequence

# ** Filter **
#    Takes a function, often a Boolean function, and returns only those
#    elements of the sequence that meet the criteria 
#    (that are TRUE when passed to the function)

# ** Reduce **
#    Applies a function on two arguments cumulatively to the items of 
#    an iterable object (a sequence such as a list) so as to reduce 
#    the iterable object to a single value. 
#    (Need to import functools)

#    For example, 
#    reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
#    Often used as an easy way to sum the numbers of a sequence   


print("An example using Map - Turns a list of words into an acronym\n")

# Another example using Map 
# - Turns a sentence (list of words) into an acronym

# as soon as possible
# ASAP

def first(word):        # returns the first letter of the word (helper func)
   return word[0]

def acronym(words):     # create the acronym
   acro = ''
   acro = acro.join(list(map(first, words))).upper()
   return acro

words = ['as','soon','as','possible']
print(words)
#acro = list(map(first, words)) # makes a list of first letters
#print(acro)
#acro = ''
# # joins to become one string as well as converting the letters to uppercase
#acro = acro.join(list(map(first, words))).upper() 
acro = acronym(words) #  made a function out of the above lines (acronym)
print(acro)