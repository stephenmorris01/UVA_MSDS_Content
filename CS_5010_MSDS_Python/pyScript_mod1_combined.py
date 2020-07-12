


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript01.py
# File: pyScript01.py
# CS 5010
# Learning Python (Python version: 3)

# Simplest (complete) program: "Hello World"
# Use print() function
print("Hello, World!")


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript02.py
# File: pyScript02.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Basic printing; in-line and multi-line comments

# Printing basics
print("This is a simple print statement")

# Printing using special characters
# Tab character ( \t )
print("Hello,\tWorld! (With a tab character)")

# Inserting a new line (line feed) character ( \n )
print("Line one\nLine two, with newline character")

# Concatenation in strings: 
# Use plus sign ( + ) to concatenate the parts of the string
print("Concatenation," + "\t" + "in strings with tab in middle")

# If you wanted to print special characters
# Printing quotes
print('Printing "quotes" within a string') # mixing single and double quotes

# What if you needed to print special characters like (\) or (') or (")
print('If I want to print \'single quotes\' in a string, use backslash!')
print("If I want to print \"double quotes\" in a string, use backslash!")
print('If I want to print \\the backslash\\ in a string, also use backslash!')

# \\     Backslash (\)
# \'     Single quote (')
# \"     Double quote (")
# \n     ASCII Linefeed

#============================================================================

# COMMENTS -- have already been using. This is single-line comment.

'''
This is an
example of
a multi-line
comment: single quotes
'''

"""
Here is another
example of
a multi-line
comment: double quotes
"""


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript02B.py
# File: pyScript02B.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Data types, Expressions, Statements, Variables

"""
*** Using the Interactive Shell ***"""

### Basic expression: single data item (datum)
##
##  An expression that evaluates to itself. It's a literal datum
### ------------------------------------------------------------------

1



### More complicated expression (e.g. arithmetic expression)
##
##  Will evaluate to whatever the result is when applying the
##  arithmetic operator to the values
### ------------------------------------------------------------------

1 + 2
1 + 2 * 3 / 2



### Kinds of quotes don't matter in printing strings; and concatenation
##
### ------------------------------------------------------------------

'hello' + ' world!'             --> 'hello world!'
"hello" + " wordl!"             --> 'hello world!'



### More complicated expression (e.g. Boolean expression)
##
### ------------------------------------------------------------------

100 > 200
500 == 500



### Assignment statements and use of variable
##
##  Assign values to variables
##  You do NOT have to provide a DATA TYPE with the variable
##  Python automatically assigns data types based on the values that are
##   assigned to the variables
### ------------------------------------------------------------------

num = 100     # variable num assigned the value 100
num = "one"   # can do this, too. Now num holds the string "one"
              # variables are VERY flexible



### Use variables in expressions
##
##  Interpretor will look up their value, and evaluate it accordingly
### ------------------------------------------------------------------

num = 100
num1 = 200
num2 = num + num1
num2                # num=100; num1=200; the result (300) in variable num2

"""

# Summary:

## Expressions: numeric, string, Boolean (most common), There are others
## Variables, via Assignment statement,  and how they apply in experssions
## Upcoming, more on Numeric Data Types"""




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript03.py
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




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript04.py
# File: pyScript04.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Advanced printing techniques (including 'format string')

## Basic usagae of the str.zfill() method
## (pads a numeric string on the left with zeros)
## It understands about plus and minus signs

print('12'.zfill(5))       # Output: 00012
print('-3.14'.zfill(7))    # Output: -003.14
print('3.141592'.zfill(5)) # Output: 3.141592
#------------------------------------------------------------

## Basic usage of the str.format() method:
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# The brackets and characters within them (called format fields)
# are replaced with the objects passed into the str.format() method.
# A number in the brackets refers to the position of the object 
# passed into the str.format() method

print('{0} and {1}'.format('bits', 'bytes')) # Output: bits and bytes
print('{1} and {0}'.format('bits', 'bytes')) # Output: bytes and bits

# .........................

# If keyword arguments are used in the str.format() method, 
# their values are referred to by using the name of the argument.
print('On {day} it was {weather}.'.format(day='Friday', weather='sunny'))
# Output: On Friday it was sunny.

day = 'Wednesday'
weather = 'snowing'
print('On {0} it was {1}.'.format(day, weather)) # Using variables
# Output: On Wednesday it was snowing.
print("==================================")
#------------------------------------------------------------

## Format String
# If we have data like -
#   name = 'Mary'
#   grade = 81.7691
# and you want to display this data in one string, one way you can do this
# is to create a "format string" - telling Python how to display the data
name = 'Mary'
grade = 81.7691

record = '%s: %.2f' % (name, grade)
print(record)

# More examples (note how single or double quotes do not matter)
print('%.2f' % (182.7691))
print("%04d" % (87))   # Output: 0087   zero-fill 4 spaces


#------------------------------------------------------------



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript05.py
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




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06.py
# File: pyScript06.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Redefining/redirecting standard out (stdout) to print to a file
#    - Redirecting standard out (stdout) back to printing to the screen
# ----------------------------------------
# - Writing to the file:  pyScript06.txt -
# ----------------------------------------

## Printing to a file rather than to the screen

import sys # import the sys library

# -- this is the usual way to print to the screen
# Use the standard out (stdout) object of the sys library. It has
# a function called write()
sys.stdout.write("Hello goes to the screen!\n")  # Output to screen
print("   Next: printing to the file!")

# Save the reference to sys.stdout (screen) so we can restore it later
original = sys.stdout

# Redirect stdout (by default it goes to the screen) to the file
sys.stdout = open('pyScript06.txt', 'a') # open file for appending ('a')

# Any print statement from now until the end of the session (or until stdout
# is redirected back) will print to the file (instead of to the screen)
print(">>> Hello! This should go to the file!")
print(">>> Here's another line that should go to the file!")

x = 5
y = 10
z = x + y
# This output should also go to the file:
print(str(x) + " plus " + str(y) + " is: " + str(z))

# * Open the file in your working directory, to see text printed to the file *

# Restore stdout back to it's original form (to the screen)
sys.stdout = original

# Now any print statement will show on the screen (and not go to the file) 
print("\n>> Exercise is done! Open file 'pyScript06.txt' <<")

# # For more information, read the "sys" module documentation.

# If you run into any trouble, you can restart the Kernel on Spyder 
# to restore settings. For any problem file, you may wish to do this 
# both before and after running the file. [Not necessary for this file]


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06B.py
# File: pyScript06B.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Print to a file using f.write("..")
# ---------------------------------------------
# - Writing to the file:  pyScript06BFILE.txt -
# ---------------------------------------------


## Printing to a file rather than to the screen

# -- this is the usual way to print to the screen
print("Hello, this text should go to the screen!")

# -- redirect print to write to a file
# Create a file object (let's call it 'f')
f = open('pyScript06BFILE.txt', 'a') # open a file for appending ('a')

# print to that file by redirecting (use of '>>') Doesn't work in v.3
# so keep the following one line commented:
#print >> f, 'This should go to the file, not the screen!'

f.write('%%% This should go to the file, not the screen! %%%') # Another way
f.write('\n') # Just adding a new line character - optional

# You will not see changes made to the file until you close the file
f.close()

# Open the file now (pyScript06BFILE.txt) and you will see the text there.

print(">>> Exercise is done! This should now be printed to SCREEN.")

# The file looks like this:
print("-----\n>>> Printing the contents of pyScript06BFILE.txt file: \n-----")
print(open('pyScript06BFILE.txt').read())



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06C.py
# File: pyScript06C.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Another example of how to print to a file using "with open as"
# ---------------------------------------------
# - Writing to the file:  pyScript06CFILE.txt -
# ---------------------------------------------

print("To screen")

with open('pyScript06CFILE.txt', 'w') as f:
   f.write("line one to file\n")
   f.write('line two to file\n')
   
print(">> File 'pyScript06CFILE.txt' is ready for viewing! <<")


# The file looks like this:
print("-----\n>>> Printing the contents of pyScript06CFILE.txt file: \n-----")
print(open('pyScript06CFILE.txt').read())


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06D.py
# File: pyScript06D.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Reading from a file
# -------------------------------------------
# - Requires the file:  pyScript06D_READ.txt -
# -------------------------------------------


## Simple example to demonstrate how to read from a file (and print contents)
# -- make sure you are in the correct working directory (where the file is)

print("** Reading from file pyScript06D_READ.txt....")

with open("pyScript06D_READ.txt") as f:
    data = f.read() # Read from the file and store contents into 'data'
                    # At this point you can do what you want with 'data'
    print(data)     # Print data
    
# Output to screen:
# Hello I'm line one
# Hello I'm line two


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06E.py
# File: pyScript06E.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Final example for redirecting standard output
# -----------------------------------------
# - Writing to the file:  pyScript06E.txt -
# -----------------------------------------

import sys
 
## Handy function to write to a file
def redirect_to_file(text):  
    # Save reference to sys.stdout (screen)
    original = sys.stdout
    
    # Redirect stdout to a file
    sys.stdout = open('pyScript06E.txt', 'w')
    
    # Print to the file
    print('This is your redirected text:')
    print(text) # Writes the text from the parameter to the file
    
    # Restores stdout back to the screen
    sys.stdout = original
    
    # This output goes to stdout, NOT the file!
    print('>>> DONE! <<<')
 
if __name__ == '__main__': 
    redirect_to_file('Python rocks!')  # Gets written to the file
    
    # The file looks like this:
    print("-----\n>>> Printing the contents of pyScript06E.txt file: \n")
    print(open('pyScript06E.txt').read())


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript07.py
# File: pyScript07.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Getting input from the user
#    - If-statement // if-else statement // if-else-if statement


## Getting input from the user 

name = input("What is the name of the gift giver? ")
present = input("What did they give you? ")
age = int(input("How old are you? "))  # remember int() function!
myname = input("What is your name? ")
print("")

print("Dear " + name + ", ")
print("")
print("Thank you so much for the " + present + "!")
print("It was so nice. I can't belive I am " + str(age))
print("years old. Doesn't seem any different than when ")
print("I was " + str(age-1) + "!")
print("")
print("Sincerely, " + myname)

print("=====================================================")

## If-statement
# Comparisons are made using relational operators (returns a Boolean result)
# (True or False) Will combine relational expressions using logical operators.

# -- logical operators, examples: and, or, and not
hoursWorked = 39
salary = 39000
print((hoursWorked > 40) and (salary <= 50000)) # False

password = 'GUEST'
print((password == 'guest') or (password == 'GUEST')) # True

print(not(100 == 100)) # False
print(not(100 < 1)) # True

print("=====================================================")

# if-statement

# format:

# if relationalexpression:
#       statements

# if RE1 and RE2:       # using logical operator, like 'and'
#       statements

# -- simple if
hoursWorked = int(input("Enter hours worked: "))
rate = 25.00 # Amount per hour
if hoursWorked > 40:
    grossPay = (40 * rate) + ((hoursWorked - 40) * (rate * 1.5))
if hoursWorked <= 40:
    grossPay = hoursWorked * rate
print("Gross pay: " + str(grossPay))

# Second if-statement really isn't needed...

# if-else statement

# Format:
# if RE:
#   statementsA
# else:
#   statementsB

# RE is evaluated, if it is True, then execute statementsA, otherwise
# execute statementsB (RE was evaluated to be False)
# Therefore, one set of statements are executed

# -- if-else statement
hoursworked2 = int(input("Enter hours worked: "))
rate = 25.00 # Amount per hour
if hoursworked2 > 40:
    grossPay = (40 * rate) + ((hoursworked2 - 40) * (rate * 1.5))
else:     # No need for second if statement!
    grossPay = hoursworked2 * rate
print("Gross pay: " + str(grossPay))

# if-else-if statement

# Format:
# if RE1:
#   statementsA
# elif RE2:
#   statementsB
# elif RE3:
#   statementsC
# else:             # Optional else section
#   statementsD     

# elif stands for "else if"
# Order is very important here

# -- if-else-if statement
grade = int(input("Enter a numeric grade: "))
letterGrade = ""
if grade >= 90:
    letterGrade = "A"
elif grade >= 80:
    letterGrade = "B"
elif grade >= 70:
    letterGrade = "C"
elif grade >= 60:
    letterGrade = "D"
elif grade <= 59:
    letterGrade = "F"
else:
    print("Did not recognize input!")
    
print("Your letter grade is: " + letterGrade)


print("=====================================================")





##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript08.py
# File: pyScript08.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Guessing game example using if-else statements
#   - While loops
#   - "continue" / "break"



## Guessing game using multiple if-else statements
# A better way to do this is to write a program using a loop
# At this time we've not covered loops yet, we will soon!

answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
# response = input()
response = input()
if response == answer:
   print("That is right!")
else:
   response = input("Sorry. Guess again: ")
   if response == answer:
      print("That is right!")
   else:
      response = input("Sorry. One more guess: ")
      if response == answer:
         print("That is right!")
      else:
         print("Sorry. No more guesses. The answer is " + answer + ".")

print("=============================================")                  

## While loops

# Format:

# while relationalExpression:   # while value of RE is true...
#   statements                  # elecute the statements inside the body

# There are two kinds of while loops:
#   - count-controlled
#   - event-controlled

# -- count-controlled while loop
number = 1
while number <= 10:
    print(number)
    number = number + 1     # Important!
print("----------")    
# Last line is important. Must be some statement that will eventually
# cause the relational expression to become FALSE (else infinite loop!)
# Eventually number will become 11, RE would be false --> end looping

# Few more examples:

# Sum of the numbers
sum = 0
number = 1
while number <= 10:
   sum = sum + number
   number = number + 1
print("The sum is " + str(sum))
print("----------")

# How much would the balance increase growing at a simple interest
# of 2% per year for 10 years
balance = 5000
rate = 1.02
year = 1
while year <= 10:
   balance = balance * rate
   print("Year: " + str(year) + ": " + str(balance))
   year = year + 1
print("----------")   

# -- event-controlled while loop

# Looks for some occurrence / some event to occur to make the loop stop

# Sentinel value: 
#    a value that carries special meaning in the program, if entered
#   it will be the event that stops the while-loop

# Sentinel value in the following example is (-1)

average = 0.0
total = 0
count = 0
print("Enter a grade (-1 to quit): ")
grade = int(input())
while grade != -1:
   total = total + grade
   count = count + 1
   print("Enter a grade (-1 to quit): ")
   grade = int(input())
average = total / count
print("Average grade: " + str(average))


print("=============================================")

## Use of continue and break in loops

# -- continue statement
# Using continue causes the loop to to stop in the middle of executing
# the body and continue with the next iteration of the loop - 
# meaning, back to the top and testing the RE, then continuing back
# into the body of the loop (if appropriate)

# Format:

# while RE:
#   statements
#   continue
#   statements

# Generally there is a check to make before continue is issued
# if RE:
#   continue  # remaining statements do NOT get executed

# continue example
# take numerator and denominator and display the quotient
# n/d (only if d != 0)
numer = 0
denom = 0
while denom != -1:
    numer = float(input("Enter a numerator: "))
    denom = float(input("Enter a denominator (-1 to end): "))
    if denom == 0:
       continue     # We do not want to calculate the rest of the stmts!
    print(numer / denom)
print("----------")

# -- break statement

# The break statement is used to immediately exit a loop (prematurely)
# when a certain condition occurs
# Then transfers control to the statement AFTER the loop

# Format:

# while RE:
#   statements
#   if RE:
#       break
#   statements
# <-- break transfers control to here (after the loop)

# break example
# Averaging some numbers
number = 0
total = 0
average = 0.0
count = 0
while True:
    number = float(input("Enter a number (-1 to break): "))
    if number == -1:
       break
    total = total + number
    count = count + 1
average = total / count
print("Average: " + str(average))

### NOTE: This is probably NOT the best way to write this program
###         It would be better to write it like the example to average
###         the grades using a sentinel value
###         This example was written for demonstration purposes only.


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript09.py
# File: pyScript09.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - While loops and files
#     *** w2file.txt needs to be created ahead of time! ***

# Learn how to write data to a text file, and then read data from the text file

# -- writing data to a file

outFile = open('w2file.txt', 'w')
outFile.write('This is line 1 in w2file\n')
outFile.write('This is line 2 in w2file\n')
outFile.close()
print("Done! Look at file: 'w2file.txt' in working directory")



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript09B.py
# File: pyScript09B.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - While loops and files

# Learn how to write data to a text file, and then read data from the text file

# -- writing data to a file - another example
# Asking for grades and writing to file
# Data input as strings

outFile = open('w2filegrades.txt', 'w')
grade = 0
print("Enter a grade (q to quit): ") # initial prompt
grade = input()
while (grade != 'q'):  # While the user did not enter 'q' (for quit) ...
    outFile.write(grade + '\n')
    print("Enter a grade (q to quit): ")
    grade = input()

print("\n Done! Look at file w2filegrades.txt in dir")
outFile.close()  # It's very important to remember to close the file after opening it for writing!


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript09C.py
# File: pyScript09C.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - While loops and files

# Learn how to write data to a text file, and then read data from the text file

# ***************************************************************
# * Make sure to run pyScript09B.py first                       *
# * Ensure file: 'w2filegrades.txt' is in the working directory *
# ***************************************************************


# Read data from the file

count = 0
total = 0
inFile = open('w2filegrades.txt', 'r')
grade = inFile.readline()  # Read one line of the file
while (grade):  # While there are still lines in the file to read... 
    print(grade)
    count = count + 1
    total = total + int(grade)
    grade = inFile.readline() # Continue reading from the file... 

average = total / count
print("Average: " + str(average))



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript10.py
# File: pyScript10.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - For-loops, using a range, an index
#   - For-loops with tuples
#   - For-loops with dictionaries


## For-loops
# Like while-loops, the for-loop is another way to iterate over
# a set of statements

# The for-loop has some advantages over the while-loop, when working
# with data structures, including even files

# Format:

# for <target> in <collection>:  # target variable in some collection of data
#   statements

# Simple example:
for i in [1,2,3,4]:
    print(i)        # will display all of the numbers 1,2,3,4 in the list
print("")

# An iterator (an internal pointer) works its way through the list,
# taking each item out of the list and placing it in the target
# (e.g. the variable "i" above). Often times called the loop control variable

# Another example:
numbers = [1,2,3]
for x in numbers:  # Can use a variable representing a list
    print(x)       # prints out each element in the list like before
print("")

# Another example:
numbers = [1,2,3,4,5]
sum = 0
for x in numbers:
    sum = sum + x  # calculate the sum of the numbers in the list
print("The sum is: " + str(sum)+ "\n")

# Often a for-loop is used to extract values out of a data structure
# so that tasks can be performed on these items
# ** The for-loop is used to retrieve all the values in the structure **
# In the case above, the for-loop will iterate through all the 
# items in the list and stops when there are no more items in the list

print("=================================================")

# Using a for-loop to process characters in a string
# Remember a string is a sequence of data, just like a list, or any
# other structure. The string is a sequence of characters
word = "hello"
for letter in word:
    print(letter)	# should print h-e-l-l-o each on a new line
print("")    

# Count the number of vowels in a longer string (sentence)
sentence = "are you suggesting coconuts migrate"
count = 0   # keep track of the vowels found
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' \
            or letter == 'o' or letter == 'u':
        count = count + 1 # if letter is a vowel, increment the counter
print("\"" + sentence + "\"")
print("The number of vowels in the above sentence is " + str(count)) # print the result


# You are able to use the CONTINUE statement or the BREAK statement
# to modify the flow of control, but a for-loop is often used when
# we want to access all of the elements in the sequence

# Notes:
# While-loops are open-ended loops whereas for-loops are not since
# we can tell the range of the for-loop by looking at the code
# When processing a file, however, a while-loop is better suited since
# we do not know how many iterations are required (we may not know how
# many lines there are in the file to process)

print("=================================================")

# Processing a list with a for-loop
# Can use the for-loop with an index
numbers = [1,2,3,4,5,6,7,8]
for i in range(0,len(numbers)):
    print(numbers[i])  # print numbers sub i
print("")    
# Will print each number, one per line. Same if used "for number in numbers:"

# To access some partial set of the complete list
# Add one more argument to the range function, to indicate the increment
# Example of printing odd numbers
thenumbers = [1,2,3,4,5,6,7,8,9,10]
print("Printing odd numbers:")
for i in range(0, len(thenumbers), 2):
    print(thenumbers[i])
print("")


# As can be seen, even though the primary use of a for-loop is to 
# access each element in a sequence, it's not necessary to do so.
# All that is needed is to specify some type of range and an index 
# into the sequence to access the elements in that range

print("=================================================")

## For-loops with Tuples
# Tuples are like lists

print("Computing the sum:")
numbers = (1,2,3,4,5) # create a tuple of 5 numbers. Note the ()'s, not []'s
sum = 0
for num in numbers:
    sum = sum + num  # compute the sum
    print(sum)       # print each number
print("The sum is " + str(sum))
print("")

# Example using strings
words = ("data","science","is","fun") # A tuple of words
for word in words:
    print(word)    # display the words
print("")
    
# Figure out which word is the longest (using indexing into the tuple)
words = ("data","science","is","fun") # A tuple of words
max = 0  # assign max to index position 0
         # assume the first word in the tuple is the longest word
for i in range(1, len(words)):  # range starting at 1 to the end
    if len(words[i]) > len(words[max]):
        max = i  # change the index to point to current max word
                 # otherwise max doesn't change
print("The longest word is: " + words[max])

# Each iteration replaces the value of max with the index of the longest word
# so far. If the current word is shorter in length than the current max
# then max doesn't change, otherwise max is updated to record the current
# index representing the longest word so far. At the end of the loop
# max will point to the largest word. (In this case: "science". max: 1)


print("=================================================")

## For-loops with Dictionaries

# Example phone book - use a for-loop to display the dictionary
numbers = {'Michael':'4496', 'Angela':'2982', 'Sage':'7771'}
print(numbers.keys())  # display all keys in the dictionary (a list)
print(numbers.values())  # same for the values (a list)
for key in numbers.keys():  # Returns a list of keys (becomes the sequence)
    print(key + " extension is: " + numbers[key])
    # Should print out each name (key) with extensions (numbers[key])
print("")




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript11-1.py
# File: pyScript11.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - For-loops with files 
#   - Example using nested for-loops with files

## Using for-loops to process a file

# Reading a file line by line using readline():
#inFile = open('text.txt', 'r') # open file for reading
#line = inFile.readline() # read a line
#while(line):  # while there is data to read
#    print(line)
#    line = inFile.readline() # read another line
    
# Another example
#for line in open('text.txt'):
#    print(line)
    
# Reading grades file ("w2filegrades.txt") and calculating the average            
sum = 0
count = 0
for grade in open('w2filegrades.txt'):
    print(grade)
    sum = sum + int(grade)
    count = count + 1
average = sum / count
print("Average: " + str(average))
print("=============================================")

# Example using nested for-loops to build a histogram of the set of grades
# Will represent 5 points by one asterisk (*)

# File:  (Edit file to illustrate Histogram below)
# 90
# 77
# 85
# 65
# 100

print("\n\nHISTOGRAM:")
print("============================")
bar = ""  # variable to hold the asterisks
for grade in open('w2filegrades.txt'):  # loop through grades file
    for i in range(1, int(grade)+1):    # loop over range 1-(GR+1)
                    # to be inclusive of the actual number
        if i % 5 == 0:  # deciding if going to add an asterisk (using modulus)
            bar = bar + "*"
    print(bar, i)  # print the bar
    bar = "" # reset bar to empty string to begin collecting the next set of *'s
print("============================")

    





##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript12-1.py
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




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript13-1.py
# File: pyScript13.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - List comprehensions

## List comprehensions
# Are essentially short-cuts for for-loops

# Let's say I have a list of numbers (grades) and I want to curve those grades
# Traditional way to do it would be to use a for-loop as follows:

grades = [71, 81, 77, 84]
print(grades)
print("Using a for-loop:")
for i in range(len(grades)):  # range(4) means indicies 0 through 3
   grades[i] = grades[i] + 5  # add 5 to each grade
print(grades)

print("--------------")

# The idea of list comprehensions is to take the two-line for-loop and
# shorten/simplify it - using ideas of for-loops and iterators
# (Almost doing a for-loop backwards)
grades = [71, 81, 77, 84]
print(grades)
print("Using list comprehension:")
grades = [grade + 5 for grade in grades]
#           -2-         -1-

# 1: for each grade in grades
# 2: add 5 to it  [the action on each element]
# Once done, take the result of doing this for all elements and
# assign it back to the variable (list) grades
print(grades)

print("===========================================")

# -- List comprehension using a list of words
words = ["CONVERTING", "TO", "LOWERCASE", "LETTERS"]
print(words)
words = [word.lower() for word in words]  # using lower() function
print(words)  # after processing, should be all lower case

print("===========================================")

# -- List comprehensions with files

# This example demonstrates how list comprehensions can save a lot of time
# The list of grades are stored as strings (since stored in txt file)
# Each grade has a new line character attached to it 
#  ['90\n', '77\n', '85\n', '65\n', '100\n']
# Need to strip the new line characters off

# Traditional way:
print("Traditional way:")
file = open('w2filegrades.txt')
grades = file.readlines()
print(grades)
for i in range(len(grades)):
   grades[i] = grades[i].rstrip()
print(grades)

print("--------------")

print("Using list comprehensions:")
grades = [grade.rstrip() for grade in open('w2filegrades.txt')]
print(grades)

print("===========================================")

# -- Practical examples of list comprehensions
# Find all the even numbers in a range
print("Finding all even numbers:")
N = range(1,101)
EN = [x for x in N if x % 2 == 0]  # Can use an if-statement
print(EN)

# pull out x, for x in N, if x mod 2 == 0 (even)
# Can use the if-statement what will return x if this condition is met

print("===========================================")

##################
# -- EXERCISE -- #
##################

# Create a long sentence of words [assume NO punctuation]
# Put the words into a list (hint, how are the words separated?)
#        (separating the words can be done before the list comprehension)
# Use a list comprehension to return the word along with the length of it
# Use this -->  (word, len(word))   in your list comprehension
# [finally, print out the words along with its length ] - at the end

print("===========================================")
  


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript_mod1_combined.py



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript01.py
# File: pyScript01.py
# CS 5010
# Learning Python (Python version: 3)

# Simplest (complete) program: "Hello World"
# Use print() function
print("Hello, World!")


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript02.py
# File: pyScript02.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Basic printing; in-line and multi-line comments

# Printing basics
print("This is a simple print statement")

# Printing using special characters
# Tab character ( \t )
print("Hello,\tWorld! (With a tab character)")

# Inserting a new line (line feed) character ( \n )
print("Line one\nLine two, with newline character")

# Concatenation in strings: 
# Use plus sign ( + ) to concatenate the parts of the string
print("Concatenation," + "\t" + "in strings with tab in middle")

# If you wanted to print special characters
# Printing quotes
print('Printing "quotes" within a string') # mixing single and double quotes

# What if you needed to print special characters like (\) or (') or (")
print('If I want to print \'single quotes\' in a string, use backslash!')
print("If I want to print \"double quotes\" in a string, use backslash!")
print('If I want to print \\the backslash\\ in a string, also use backslash!')

# \\     Backslash (\)
# \'     Single quote (')
# \"     Double quote (")
# \n     ASCII Linefeed

#============================================================================

# COMMENTS -- have already been using. This is single-line comment.

'''
This is an
example of
a multi-line
comment: single quotes
'''

"""
Here is another
example of
a multi-line
comment: double quotes
"""


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript02B.py
# File: pyScript02B.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Data types, Expressions, Statements, Variables

"""
*** Using the Interactive Shell ***

### Basic expression: single data item (datum)
##
##  An expression that evaluates to itself. It's a literal datum
### ------------------------------------------------------------------

1



### More complicated expression (e.g. arithmetic expression)
##
##  Will evaluate to whatever the result is when applying the
##  arithmetic operator to the values
### ------------------------------------------------------------------

1 + 2
1 + 2 * 3 / 2



### Kinds of quotes don't matter in printing strings; and concatenation
##
### ------------------------------------------------------------------

'hello' + ' world!'             --> 'hello world!'
"hello" + " wordl!"             --> 'hello world!'



### More complicated expression (e.g. Boolean expression)
##
### ------------------------------------------------------------------

100 > 200
500 == 500



### Assignment statements and use of variable
##
##  Assign values to variables
##  You do NOT have to provide a DATA TYPE with the variable
##  Python automatically assigns data types based on the values that are
##   assigned to the variables
### ------------------------------------------------------------------

num = 100     # variable num assigned the value 100
num = "one"   # can do this, too. Now num holds the string "one"
              # variables are VERY flexible



### Use variables in expressions
##
##  Interpretor will look up their value, and evaluate it accordingly
### ------------------------------------------------------------------

num = 100
num1 = 200
num2 = num + num1
num2                # num=100; num1=200; the result (300) in variable num2

"""

# Summary:

## Expressions: numeric, string, Boolean (most common), There are others
## Variables, via Assignment statement,  and how they apply in experssions
## Upcoming, more on Numeric Data Types




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript03.py
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




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript04.py
# File: pyScript04.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Advanced printing techniques (including 'format string')

## Basic usagae of the str.zfill() method
## (pads a numeric string on the left with zeros)
## It understands about plus and minus signs

print('12'.zfill(5))       # Output: 00012
print('-3.14'.zfill(7))    # Output: -003.14
print('3.141592'.zfill(5)) # Output: 3.141592
#------------------------------------------------------------

## Basic usage of the str.format() method:
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# The brackets and characters within them (called format fields)
# are replaced with the objects passed into the str.format() method.
# A number in the brackets refers to the position of the object 
# passed into the str.format() method

print('{0} and {1}'.format('bits', 'bytes')) # Output: bits and bytes
print('{1} and {0}'.format('bits', 'bytes')) # Output: bytes and bits

# .........................

# If keyword arguments are used in the str.format() method, 
# their values are referred to by using the name of the argument.
print('On {day} it was {weather}.'.format(day='Friday', weather='sunny'))
# Output: On Friday it was sunny.

day = 'Wednesday'
weather = 'snowing'
print('On {0} it was {1}.'.format(day, weather)) # Using variables
# Output: On Wednesday it was snowing.
print("==================================")
#------------------------------------------------------------

## Format String
# If we have data like -
#   name = 'Mary'
#   grade = 81.7691
# and you want to display this data in one string, one way you can do this
# is to create a "format string" - telling Python how to display the data
name = 'Mary'
grade = 81.7691

record = '%s: %.2f' % (name, grade)
print(record)

# More examples (note how single or double quotes do not matter)
print('%.2f' % (182.7691))
print("%04d" % (87))   # Output: 0087   zero-fill 4 spaces


#------------------------------------------------------------



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript05.py
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




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06.py
# File: pyScript06.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Redefining/redirecting standard out (stdout) to print to a file
#    - Redirecting standard out (stdout) back to printing to the screen
# ----------------------------------------
# - Writing to the file:  pyScript06.txt -
# ----------------------------------------

## Printing to a file rather than to the screen

import sys # import the sys library

# -- this is the usual way to print to the screen
# Use the standard out (stdout) object of the sys library. It has
# a function called write()
sys.stdout.write("Hello goes to the screen!\n")  # Output to screen
print("   Next: printing to the file!")

# Save the reference to sys.stdout (screen) so we can restore it later
original = sys.stdout

# Redirect stdout (by default it goes to the screen) to the file
sys.stdout = open('pyScript06.txt', 'a') # open file for appending ('a')

# Any print statement from now until the end of the session (or until stdout
# is redirected back) will print to the file (instead of to the screen)
print(">>> Hello! This should go to the file!")
print(">>> Here's another line that should go to the file!")

x = 5
y = 10
z = x + y
# This output should also go to the file:
print(str(x) + " plus " + str(y) + " is: " + str(z))

# * Open the file in your working directory, to see text printed to the file *

# Restore stdout back to it's original form (to the screen)
sys.stdout = original

# Now any print statement will show on the screen (and not go to the file) 
print("\n>> Exercise is done! Open file 'pyScript06.txt' <<")

# # For more information, read the "sys" module documentation.

# If you run into any trouble, you can restart the Kernel on Spyder 
# to restore settings. For any problem file, you may wish to do this 
# both before and after running the file. [Not necessary for this file]


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06B.py
# File: pyScript06B.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Print to a file using f.write("..")
# ---------------------------------------------
# - Writing to the file:  pyScript06BFILE.txt -
# ---------------------------------------------


## Printing to a file rather than to the screen

# -- this is the usual way to print to the screen
print("Hello, this text should go to the screen!")

# -- redirect print to write to a file
# Create a file object (let's call it 'f')
f = open('pyScript06BFILE.txt', 'a') # open a file for appending ('a')

# print to that file by redirecting (use of '>>') Doesn't work in v.3
# so keep the following one line commented:
#print >> f, 'This should go to the file, not the screen!'

f.write('%%% This should go to the file, not the screen! %%%') # Another way
f.write('\n') # Just adding a new line character - optional

# You will not see changes made to the file until you close the file
f.close()

# Open the file now (pyScript06BFILE.txt) and you will see the text there.

print(">>> Exercise is done! This should now be printed to SCREEN.")

# The file looks like this:
print("-----\n>>> Printing the contents of pyScript06BFILE.txt file: \n-----")
print(open('pyScript06BFILE.txt').read())



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06C.py
# File: pyScript06C.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Another example of how to print to a file using "with open as"
# ---------------------------------------------
# - Writing to the file:  pyScript06CFILE.txt -
# ---------------------------------------------

print("To screen")

with open('pyScript06CFILE.txt', 'w') as f:
   f.write("line one to file\n")
   f.write('line two to file\n')
   
print(">> File 'pyScript06CFILE.txt' is ready for viewing! <<")


# The file looks like this:
print("-----\n>>> Printing the contents of pyScript06CFILE.txt file: \n-----")
print(open('pyScript06CFILE.txt').read())


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06D.py
# File: pyScript06D.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Reading from a file
# -------------------------------------------
# - Requires the file:  pyScript06D_READ.txt -
# -------------------------------------------


## Simple example to demonstrate how to read from a file (and print contents)
# -- make sure you are in the correct working directory (where the file is)

print("** Reading from file pyScript06D_READ.txt....")

with open("pyScript06D_READ.txt") as f:
    data = f.read() # Read from the file and store contents into 'data'
                    # At this point you can do what you want with 'data'
    print(data)     # Print data
    
# Output to screen:
# Hello I'm line one
# Hello I'm line two


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript06E.py
# File: pyScript06E.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Final example for redirecting standard output
# -----------------------------------------
# - Writing to the file:  pyScript06E.txt -
# -----------------------------------------

import sys
 
## Handy function to write to a file
def redirect_to_file(text):  
    # Save reference to sys.stdout (screen)
    original = sys.stdout
    
    # Redirect stdout to a file
    sys.stdout = open('pyScript06E.txt', 'w')
    
    # Print to the file
    print('This is your redirected text:')
    print(text) # Writes the text from the parameter to the file
    
    # Restores stdout back to the screen
    sys.stdout = original
    
    # This output goes to stdout, NOT the file!
    print('>>> DONE! <<<')
 
if __name__ == '__main__': 
    redirect_to_file('Python rocks!')  # Gets written to the file
    
    # The file looks like this:
    print("-----\n>>> Printing the contents of pyScript06E.txt file: \n")
    print(open('pyScript06E.txt').read())


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript07.py
# File: pyScript07.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Getting input from the user
#    - If-statement // if-else statement // if-else-if statement


## Getting input from the user 

name = input("What is the name of the gift giver? ")
present = input("What did they give you? ")
age = int(input("How old are you? "))  # remember int() function!
myname = input("What is your name? ")
print("")

print("Dear " + name + ", ")
print("")
print("Thank you so much for the " + present + "!")
print("It was so nice. I can't belive I am " + str(age))
print("years old. Doesn't seem any different than when ")
print("I was " + str(age-1) + "!")
print("")
print("Sincerely, " + myname)

print("=====================================================")

## If-statement
# Comparisons are made using relational operators (returns a Boolean result)
# (True or False) Will combine relational expressions using logical operators.

# -- logical operators, examples: and, or, and not
hoursWorked = 39
salary = 39000
print((hoursWorked > 40) and (salary <= 50000)) # False

password = 'GUEST'
print((password == 'guest') or (password == 'GUEST')) # True

print(not(100 == 100)) # False
print(not(100 < 1)) # True

print("=====================================================")

# if-statement

# format:

# if relationalexpression:
#       statements

# if RE1 and RE2:       # using logical operator, like 'and'
#       statements

# -- simple if
hoursWorked = int(input("Enter hours worked: "))
rate = 25.00 # Amount per hour
if hoursWorked > 40:
    grossPay = (40 * rate) + ((hoursWorked - 40) * (rate * 1.5))
if hoursWorked <= 40:
    grossPay = hoursWorked * rate
print("Gross pay: " + str(grossPay))

# Second if-statement really isn't needed...

# if-else statement

# Format:
# if RE:
#   statementsA
# else:
#   statementsB

# RE is evaluated, if it is True, then execute statementsA, otherwise
# execute statementsB (RE was evaluated to be False)
# Therefore, one set of statements are executed

# -- if-else statement
hoursworked2 = int(input("Enter hours worked: "))
rate = 25.00 # Amount per hour
if hoursworked2 > 40:
    grossPay = (40 * rate) + ((hoursworked2 - 40) * (rate * 1.5))
else:     # No need for second if statement!
    grossPay = hoursworked2 * rate
print("Gross pay: " + str(grossPay))

# if-else-if statement

# Format:
# if RE1:
#   statementsA
# elif RE2:
#   statementsB
# elif RE3:
#   statementsC
# else:             # Optional else section
#   statementsD     

# elif stands for "else if"
# Order is very important here

# -- if-else-if statement
grade = int(input("Enter a numeric grade: "))
letterGrade = ""
if grade >= 90:
    letterGrade = "A"
elif grade >= 80:
    letterGrade = "B"
elif grade >= 70:
    letterGrade = "C"
elif grade >= 60:
    letterGrade = "D"
elif grade <= 59:
    letterGrade = "F"
else:
    print("Did not recognize input!")
    
print("Your letter grade is: " + letterGrade)


print("=====================================================")





##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript08.py
# File: pyScript08.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Guessing game example using if-else statements
#   - While loops
#   - "continue" / "break"



## Guessing game using multiple if-else statements
# A better way to do this is to write a program using a loop
# At this time we've not covered loops yet, we will soon!

answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
# response = input()
response = input()
if response == answer:
   print("That is right!")
else:
   response = input("Sorry. Guess again: ")
   if response == answer:
      print("That is right!")
   else:
      response = input("Sorry. One more guess: ")
      if response == answer:
         print("That is right!")
      else:
         print("Sorry. No more guesses. The answer is " + answer + ".")

print("=============================================")                  

## While loops

# Format:

# while relationalExpression:   # while value of RE is true...
#   statements                  # elecute the statements inside the body

# There are two kinds of while loops:
#   - count-controlled
#   - event-controlled

# -- count-controlled while loop
number = 1
while number <= 10:
    print(number)
    number = number + 1     # Important!
print("----------")    
# Last line is important. Must be some statement that will eventually
# cause the relational expression to become FALSE (else infinite loop!)
# Eventually number will become 11, RE would be false --> end looping

# Few more examples:

# Sum of the numbers
sum = 0
number = 1
while number <= 10:
   sum = sum + number
   number = number + 1
print("The sum is " + str(sum))
print("----------")

# How much would the balance increase growing at a simple interest
# of 2% per year for 10 years
balance = 5000
rate = 1.02
year = 1
while year <= 10:
   balance = balance * rate
   print("Year: " + str(year) + ": " + str(balance))
   year = year + 1
print("----------")   

# -- event-controlled while loop

# Looks for some occurrence / some event to occur to make the loop stop

# Sentinel value: 
#    a value that carries special meaning in the program, if entered
#   it will be the event that stops the while-loop

# Sentinel value in the following example is (-1)

average = 0.0
total = 0
count = 0
print("Enter a grade (-1 to quit): ")
grade = int(input())
while grade != -1:
   total = total + grade
   count = count + 1
   print("Enter a grade (-1 to quit): ")
   grade = int(input())
average = total / count
print("Average grade: " + str(average))


print("=============================================")

## Use of continue and break in loops

# -- continue statement
# Using continue causes the loop to to stop in the middle of executing
# the body and continue with the next iteration of the loop - 
# meaning, back to the top and testing the RE, then continuing back
# into the body of the loop (if appropriate)

# Format:

# while RE:
#   statements
#   continue
#   statements

# Generally there is a check to make before continue is issued
# if RE:
#   continue  # remaining statements do NOT get executed

# continue example
# take numerator and denominator and display the quotient
# n/d (only if d != 0)
numer = 0
denom = 0
while denom != -1:
    numer = float(input("Enter a numerator: "))
    denom = float(input("Enter a denominator (-1 to end): "))
    if denom == 0:
       continue     # We do not want to calculate the rest of the stmts!
    print(numer / denom)
print("----------")

# -- break statement

# The break statement is used to immediately exit a loop (prematurely)
# when a certain condition occurs
# Then transfers control to the statement AFTER the loop

# Format:

# while RE:
#   statements
#   if RE:
#       break
#   statements
# <-- break transfers control to here (after the loop)

# break example
# Averaging some numbers
number = 0
total = 0
average = 0.0
count = 0
while True:
    number = float(input("Enter a number (-1 to break): "))
    if number == -1:
       break
    total = total + number
    count = count + 1
average = total / count
print("Average: " + str(average))

### NOTE: This is probably NOT the best way to write this program
###         It would be better to write it like the example to average
###         the grades using a sentinel value
###         This example was written for demonstration purposes only.


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript09.py
# File: pyScript09.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - While loops and files
#     *** w2file.txt needs to be created ahead of time! ***

# Learn how to write data to a text file, and then read data from the text file

# -- writing data to a file

outFile = open('w2file.txt', 'w')
outFile.write('This is line 1 in w2file\n')
outFile.write('This is line 2 in w2file\n')
outFile.close()
print("Done! Look at file: 'w2file.txt' in working directory")



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript09B.py
# File: pyScript09B.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - While loops and files

# Learn how to write data to a text file, and then read data from the text file

# -- writing data to a file - another example
# Asking for grades and writing to file
# Data input as strings

outFile = open('w2filegrades.txt', 'w')
grade = 0
print("Enter a grade (q to quit): ") # initial prompt
grade = input()
while (grade != 'q'):  # While the user did not enter 'q' (for quit) ...
    outFile.write(grade + '\n')
    print("Enter a grade (q to quit): ")
    grade = input()

print("\n Done! Look at file w2filegrades.txt in dir")
outFile.close()  # It's very important to remember to close the file after opening it for writing!


##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript09C.py
# File: pyScript09C.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - While loops and files

# Learn how to write data to a text file, and then read data from the text file

# ***************************************************************
# * Make sure to run pyScript09B.py first                       *
# * Ensure file: 'w2filegrades.txt' is in the working directory *
# ***************************************************************


# Read data from the file

count = 0
total = 0
inFile = open('w2filegrades.txt', 'r')
grade = inFile.readline()  # Read one line of the file
while (grade):  # While there are still lines in the file to read... 
    print(grade)
    count = count + 1
    total = total + int(grade)
    grade = inFile.readline() # Continue reading from the file... 

average = total / count
print("Average: " + str(average))



##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript10.py
# File: pyScript10.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - For-loops, using a range, an index
#   - For-loops with tuples
#   - For-loops with dictionaries


## For-loops
# Like while-loops, the for-loop is another way to iterate over
# a set of statements

# The for-loop has some advantages over the while-loop, when working
# with data structures, including even files

# Format:

# for <target> in <collection>:  # target variable in some collection of data
#   statements

# Simple example:
for i in [1,2,3,4]:
    print(i)        # will display all of the numbers 1,2,3,4 in the list
print("")

# An iterator (an internal pointer) works its way through the list,
# taking each item out of the list and placing it in the target
# (e.g. the variable "i" above). Often times called the loop control variable

# Another example:
numbers = [1,2,3]
for x in numbers:  # Can use a variable representing a list
    print(x)       # prints out each element in the list like before
print("")

# Another example:
numbers = [1,2,3,4,5]
sum = 0
for x in numbers:
    sum = sum + x  # calculate the sum of the numbers in the list
print("The sum is: " + str(sum)+ "\n")

# Often a for-loop is used to extract values out of a data structure
# so that tasks can be performed on these items
# ** The for-loop is used to retrieve all the values in the structure **
# In the case above, the for-loop will iterate through all the 
# items in the list and stops when there are no more items in the list

print("=================================================")

# Using a for-loop to process characters in a string
# Remember a string is a sequence of data, just like a list, or any
# other structure. The string is a sequence of characters
word = "hello"
for letter in word:
    print(letter)	# should print h-e-l-l-o each on a new line
print("")    

# Count the number of vowels in a longer string (sentence)
sentence = "are you suggesting coconuts migrate"
count = 0   # keep track of the vowels found
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' \
            or letter == 'o' or letter == 'u':
        count = count + 1 # if letter is a vowel, increment the counter
print("\"" + sentence + "\"")
print("The number of vowels in the above sentence is " + str(count)) # print the result


# You are able to use the CONTINUE statement or the BREAK statement
# to modify the flow of control, but a for-loop is often used when
# we want to access all of the elements in the sequence

# Notes:
# While-loops are open-ended loops whereas for-loops are not since
# we can tell the range of the for-loop by looking at the code
# When processing a file, however, a while-loop is better suited since
# we do not know how many iterations are required (we may not know how
# many lines there are in the file to process)

print("=================================================")

# Processing a list with a for-loop
# Can use the for-loop with an index
numbers = [1,2,3,4,5,6,7,8]
for i in range(0,len(numbers)):
    print(numbers[i])  # print numbers sub i
print("")    
# Will print each number, one per line. Same if used "for number in numbers:"

# To access some partial set of the complete list
# Add one more argument to the range function, to indicate the increment
# Example of printing odd numbers
thenumbers = [1,2,3,4,5,6,7,8,9,10]
print("Printing odd numbers:")
for i in range(0, len(thenumbers), 2):
    print(thenumbers[i])
print("")


# As can be seen, even though the primary use of a for-loop is to 
# access each element in a sequence, it's not necessary to do so.
# All that is needed is to specify some type of range and an index 
# into the sequence to access the elements in that range

print("=================================================")

## For-loops with Tuples
# Tuples are like lists

print("Computing the sum:")
numbers = (1,2,3,4,5) # create a tuple of 5 numbers. Note the ()'s, not []'s
sum = 0
for num in numbers:
    sum = sum + num  # compute the sum
    print(sum)       # print each number
print("The sum is " + str(sum))
print("")

# Example using strings
words = ("data","science","is","fun") # A tuple of words
for word in words:
    print(word)    # display the words
print("")
    
# Figure out which word is the longest (using indexing into the tuple)
words = ("data","science","is","fun") # A tuple of words
max = 0  # assign max to index position 0
         # assume the first word in the tuple is the longest word
for i in range(1, len(words)):  # range starting at 1 to the end
    if len(words[i]) > len(words[max]):
        max = i  # change the index to point to current max word
                 # otherwise max doesn't change
print("The longest word is: " + words[max])

# Each iteration replaces the value of max with the index of the longest word
# so far. If the current word is shorter in length than the current max
# then max doesn't change, otherwise max is updated to record the current
# index representing the longest word so far. At the end of the loop
# max will point to the largest word. (In this case: "science". max: 1)


print("=================================================")

## For-loops with Dictionaries

# Example phone book - use a for-loop to display the dictionary
numbers = {'Michael':'4496', 'Angela':'2982', 'Sage':'7771'}
print(numbers.keys())  # display all keys in the dictionary (a list)
print(numbers.values())  # same for the values (a list)
for key in numbers.keys():  # Returns a list of keys (becomes the sequence)
    print(key + " extension is: " + numbers[key])
    # Should print out each name (key) with extensions (numbers[key])
print("")




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript11-1.py
# File: pyScript11.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - For-loops with files 
#   - Example using nested for-loops with files

## Using for-loops to process a file

# Reading a file line by line using readline():
#inFile = open('text.txt', 'r') # open file for reading
#line = inFile.readline() # read a line
#while(line):  # while there is data to read
#    print(line)
#    line = inFile.readline() # read another line
    
# Another example
#for line in open('text.txt'):
#    print(line)
    
# Reading grades file ("w2filegrades.txt") and calculating the average            
sum = 0
count = 0
for grade in open('w2filegrades.txt'):
    print(grade)
    sum = sum + int(grade)
    count = count + 1
average = sum / count
print("Average: " + str(average))
print("=============================================")

# Example using nested for-loops to build a histogram of the set of grades
# Will represent 5 points by one asterisk (*)

# File:  (Edit file to illustrate Histogram below)
# 90
# 77
# 85
# 65
# 100

print("\n\nHISTOGRAM:")
print("============================")
bar = ""  # variable to hold the asterisks
for grade in open('w2filegrades.txt'):  # loop through grades file
    for i in range(1, int(grade)+1):    # loop over range 1-(GR+1)
                    # to be inclusive of the actual number
        if i % 5 == 0:  # deciding if going to add an asterisk (using modulus)
            bar = bar + "*"
    print(bar, i)  # print the bar
    bar = "" # reset bar to empty string to begin collecting the next set of *'s
print("============================")

    





##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript12-1.py
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




##----------D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\pyScript13-1.py
# File: pyScript13.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - List comprehensions

## List comprehensions
# Are essentially short-cuts for for-loops

# Let's say I have a list of numbers (grades) and I want to curve those grades
# Traditional way to do it would be to use a for-loop as follows:

grades = [71, 81, 77, 84]
print(grades)
print("Using a for-loop:")
for i in range(len(grades)):  # range(4) means indicies 0 through 3
   grades[i] = grades[i] + 5  # add 5 to each grade
print(grades)

print("--------------")

# The idea of list comprehensions is to take the two-line for-loop and
# shorten/simplify it - using ideas of for-loops and iterators
# (Almost doing a for-loop backwards)
grades = [71, 81, 77, 84]
print(grades)
print("Using list comprehension:")
grades = [grade + 5 for grade in grades]
#           -2-         -1-

# 1: for each grade in grades
# 2: add 5 to it  [the action on each element]
# Once done, take the result of doing this for all elements and
# assign it back to the variable (list) grades
print(grades)

print("===========================================")

# -- List comprehension using a list of words
words = ["CONVERTING", "TO", "LOWERCASE", "LETTERS"]
print(words)
words = [word.lower() for word in words]  # using lower() function
print(words)  # after processing, should be all lower case

print("===========================================")

# -- List comprehensions with files

# This example demonstrates how list comprehensions can save a lot of time
# The list of grades are stored as strings (since stored in txt file)
# Each grade has a new line character attached to it 
#  ['90\n', '77\n', '85\n', '65\n', '100\n']
# Need to strip the new line characters off

# Traditional way:
print("Traditional way:")
file = open('w2filegrades.txt')
grades = file.readlines()
print(grades)
for i in range(len(grades)):
   grades[i] = grades[i].rstrip()
print(grades)

print("--------------")

print("Using list comprehensions:")
grades = [grade.rstrip() for grade in open('w2filegrades.txt')]
print(grades)

print("===========================================")

# -- Practical examples of list comprehensions
# Find all the even numbers in a range
print("Finding all even numbers:")
N = range(1,101)
EN = [x for x in N if x % 2 == 0]  # Can use an if-statement
print(EN)

# pull out x, for x in N, if x mod 2 == 0 (even)
# Can use the if-statement what will return x if this condition is met

print("===========================================")

##################
# -- EXERCISE -- #
##################

# Create a long sentence of words [assume NO punctuation]
# Put the words into a list (hint, how are the words separated?)
#        (separating the words can be done before the list comprehension)
# Use a list comprehension to return the word along with the length of it
# Use this -->  (word, len(word))   in your list comprehension
# [finally, print out the words along with its length ] - at the end

print("===========================================")
  