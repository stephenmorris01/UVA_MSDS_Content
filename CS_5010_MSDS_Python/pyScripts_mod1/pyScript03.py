# File: pyScript03.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Quick overview
#             - data types
#             - Boolean examples
#             - Number examples
#             - Identity, using id() function
#             - Importing -- Math module: sqrt() function
#             - String examples
#             - Input from users

# import statement: (used below in math modeule section)
from math import sqrt

# ## DATA TYPES #############################################
# -- declaring a number of variables with different value types
integerEx = 8
longIntEx = 22000000000000000000000
floatEx = 2.2
stringEx = "Hello"
booleanEx = True

print(type(integerEx))
print(type(longIntEx))
print(type(floatEx))
print(type(stringEx))
print(type(booleanEx))
print ("===================================")


# -- deleting variables
x = 101.25
y = x + 50
del x  # delete the variable x
print("The value of y is: " + str(y))
# print x
# If you uncomment the above line and try to run this script you will
# get an error that says:  NameError: name 'x' is not defined 
print ("===================================")


# ## BOOLEAN EXAMPLES #######################################

booleanTwo = False

res1 = booleanEx and booleanTwo
print('{0} and {1} is {2}.'.format(booleanEx, booleanTwo, res1)) # Using vars
print(booleanEx and booleanTwo)
print("..........")

res2 = booleanEx or booleanTwo
print('{0} or {1} is {2}.'.format(booleanEx, booleanTwo, res2))
print(booleanEx or booleanTwo)
print("..........")

res3 = not booleanTwo
print('not {0} is {1}.'.format(booleanTwo, res3))
print(not booleanTwo)
print ("===================================")


# ## NUMBER EXAMPLES ########################################

intOne = 7
intTwo = 99
floatOne = 7.9
floatTwo = 9.8

# -- integer and float division;  type casting
print(intTwo / intOne) # This should be 14.14 (integer division!)
print(float(intTwo) / float(intOne))  # (float division)
print(int(floatOne))
print(int(booleanTwo)) # convert boolean (false) to integer ==> 0 for false
print ("===================================")

# -- standard Relational Operators
print(intOne > intTwo)
print(intOne >= intTwo)
print(intOne < intTwo)
print(intOne <= intTwo)
print(intOne != intTwo)
print(intOne == intTwo)
print ("===================================")

# -- standard mathematical operators;  order of precedence
# -- [addition, subtraction, multiplication, division, modulus, exponent]
print(intOne + intTwo)
print(intOne - intTwo)
print(intOne * intTwo)
print(intOne / intTwo)
print(intTwo % intOne)
print(intOne ** intTwo)
print ("===================================")


# ## IDENTITY ###############################################
# Returns the identity of an object --> is an integer (or long integer)
#   which is guaranteed to be unique and constant for this object 
#   during its lifetime.
# Can think of it like the address of the object in memory

print(id(floatOne))
print ("===================================")


# ## MATH MODULE - USING IMPORT #############################
# Importing sqrt() function in the math library

print(sqrt(intOne))
print ("===================================")

# ## STRING BASICS ##########################################

strOne = "Hello"
strTwo = "World"

print(strOne, strTwo)
print(strOne + strTwo)

longStr = '"This is a very long string that \
goes on forever and ever"'

print(longStr)
print("Printing out the first 3 characters of the string:")
print(longStr[0:3])
print ("===================================")


# ## INPUT FROM USERS #######################################

answer = input("What is your name? ")
print("Hello, " + answer + "!")
print ("===================================")

