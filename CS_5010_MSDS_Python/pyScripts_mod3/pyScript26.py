# File: pyScript26.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Exception Handling - Try-Except-Finally statements
#   - Exception Handling - raise statement


## An alternate version of the Try-Except statement is the Try-Except-Finally
# statement. The "Finally" clause is a set of statements that are executed
# when no other statements can be executed without throwing exceptions.

# The Finally clause is used to execute code that you want to run no matter
# what else happens throughout the rest of the exception-handling process

# Format:
#try:
#    set of statements that could throw exceptions
#except:
#    set of statements to try and fix the errors
#finally:
#    set of statements that we want to execute no matter what else happens
#    and right before the program ends
#    common use: close files, release resources, etc ...
    
# ===========================================================================

# -- Try-Except-Finally Example:

try:
    name = input("Enter the name of a file: ")
    file = open(name, 'r')
    for line in file:
        print(line),
except:
    name = input("Error: File not found!  Enter another file name: ")
    file = open(name, 'r')              # w2filegrades.txt
    for line in file:
        print(line),
finally:
    print("I'm in finally!")
    file.close()   # do this no matter what else is happening in the program
    
print("Outside try-except-finally") 
 
print("==============================")   
print("")

# ===========================================================================


# -- raise example:
# [ Note, not a complete Class, just for demonstration purposes ]

class Rational:
    def __init__(self, x, y):  # constructor
        numer = x
        if y == 0:  # if denom is zero...
            print(str(numer) + ' / ' + str(y))
            raise ZeroDivisionError()  # raise this kind of error
        else:
            denom = y
        print(str(numer) + ' / ' + str(denom))

try:
    rat1 = Rational(4,1)
    rat2 = Rational(3,0)  # !!
except:
    print("Cannot have a rational number with 0 for denominator!")
    # Want to print *this* message instead of the raw error message
