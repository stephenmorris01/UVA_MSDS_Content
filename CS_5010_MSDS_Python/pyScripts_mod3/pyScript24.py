# File: pyScript24.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Exception Handling

## Handling errors that occur in Python
# These errors are called EXCEPTIONS
# Exceptions occur when something in a program goes wrong, such as
# a division by zero, or trying to open a file that doesn't exist

# We want to distinguish exceptions from other types of errors such as
# misspelling the name of a function (that's more of a typographical error)

# The types of errors disscussed will occur when the program is running
# (or at "run time")

# ==================================================================

# -- Divide by zero exception:
numer = int(input("Enter a numerator: "))
denom = int(input("Enter a denominator: "))
quotient = numer / denom
print(str(numer) + " / " + str(denom) + " = " + str(quotient))


# If you enter 8 (for numer) and 0 for denom, an exception will be "thrown"
# ==>  ZeroDivisionError: division by zero 
# Because we tried to divide by zero when computing the quotient

# ==================================================================

# -- Open a file that doesn't exist (open to read, *not* to write)
file = open('blah.txt', 'r')  # assuming blah.txt does NOT exit


# Here we get a FileNotFoundError error (a kind of IO error)
# ==>  FileNotFoundError: [Errno 2] No such file or directory: 'blah.txt' 
# Because it looks for the file to open but doesn't find it in the working dir

# ==================================================================

## One way to handle events that occur in a program is to use 
# Try-Except statements. Used to handle these errors and prevent the
# program from crashing
