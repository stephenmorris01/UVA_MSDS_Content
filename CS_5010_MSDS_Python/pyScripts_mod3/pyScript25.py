# File: pyScript25.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Exception Handling - Try-Except statements

## Handling errors that occur in a program using Try-Except

# Format:
# try:
#   code to be executed - code that MIGHT lead to an exception
# except:
#   code to run to HANDLE exceptions - how to fix the problem

# =============================================================

# Try-Except example:
# We can specify specific TYPES of exceptions
# If you have a batch of code that could throw multiple exceptions,
# and you are aware of what these exceptions are, then you can have
# specific code to handle each exception
# (Or you can have a single except statement and 
# handle all the exceptions at once)

try:
    name = input("Enter the name of a file: ")
    file = open(name, 'r')  # try to open this file for reading
    
    numer = int(input("Enter a numerator: "))
    denom = int(input("Enter a denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
except FileNotFoundError:   # specifically for file errors [BEFORE IOError!]
    print("** FileNotFoundError >> Cannot open file! **")
    name = input("Enter the name of a file to open: ") # w2filegrades.txt
    file = open(name, 'r')
except IOError:  # for general IO errors
    print("** You caught a general IOError! **")
    name = input("Enter the name of a file to open: ") # w2filegrades.txt
    file = open(name, 'r')
#except FileNotFoundError:
#    print("** FileNotFoundError >> Cannot open file! **")
#    name = input("Enter the name of a file to open: ") # w2filegrades.txt
#    file = open(name, 'r')    
except ZeroDivisionError:  # for divide by zero error
    print("** Cannot divide by zero! **")
    denom = int(input("Enter a non-zero denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))


# =============================================================================
# Which exception will catch the error? 
# The very FIRST exception of the right kind.
# 
# Trying to open a non-existent  file is a kind of IO error and so can be 
# caught by the IOError exception. If the IOError was one of the exceptions 
# that could be caught, that's the one that will catch this error. More 
# specifically, however, opening a non-existent file is a FileNotFoundError 
# exception. A FileNotFoundError exception is a kind of (sub-class) IOError 
# exception. Therefore, both a FileNotFoundError exception and an IOError 
# exception will catch this kind of error. Since both catch this error, if 
# you need the more specific version (i.e. FileNotFoundError exception and 
# not the more general IOError exception) then you MUST place the more 
# specific FileNotFoundError exception BEFORE the more general IOError 
# exception (otherwise, if it's the other way around, the FileNotFoundError 
# exception would never be reached since the error would be caught by the 
# earlier IOError exception.) 
#
# To see this happen, comment back in the commented FileNotFoundError exception
# and comment out the earlier FileNotFoundError exception. Now, cause a
# file not found error to occur. You'll see the general 'IOError' message!
# =============================================================================

