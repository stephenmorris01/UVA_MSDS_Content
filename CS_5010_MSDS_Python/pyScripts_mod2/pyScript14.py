# File: pyScript14.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Functions

## Functions
# Definition:
# A piece of source code, separate fom the larger program, that performs
# a specific task. This section of code is given a name and can be called
# from the main/larger program. It is called by using its given name

# -- Reasons to use functions:
#  1. reduce complex tasks into simpler tasks
#  2. eleiminate duplicate code (no need to re-write, reuse func as needed)
#  3. code reuse (once func is written, can reuse it in any other program)
#  4. distribute tasks to multiple programmers (each func written by someone)
#  5. hide implementation details - abstraction 
#       (increase readability, increase maintenance and quality)
#  6. improves debugging by improving traceability
#       (easier to follow - jump from function to function)

# ====================================================================

# -- Example of a function
# use the key word "def" - for "definition"

# Format:
# def functionName(parameters):
#   statements (indented) [return used]

def square(number):
    return number * number  # square a number
    
def addTen(number):
    return number + 10  # Add 10 to the number   
    
def numVowels(string):
    string = string.lower()  # convert user input to lowercase
    count = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or \
           string[i] == "i" or string[i] == "o" or \
           string[i] == "u":
           count += 1 # increment count
    return count
                 
    
# Usage:
num = int(input("Enter a number to square: "))
numSquared = square(num)  # calling the square function with num as parameter
plusten = addTen(num)  # calling the addTen function
print(str(num) + " squared is: " + str(numSquared))
print(str(num) + " plus 10 is: " + str(plusten))

strng = input("Enter a string: ")
print("There are " + str(numVowels(strng)) + " vowels in the string.")
    
print("===========================================")    

# Using a conversion program to convert *F to *C and vice versa
def ftoc(temp):  # *F to *C
    return (temp-32.0) * (5.0/9.0)
    
def ctof(temp):  # *C to *F
    return temp * (9.0/5.0) + 32.0
    
def convert(temp, toTemp):  # Two parameters
    # No problem to call another function in the body of a function
    if toTemp.lower() == "c":
        return ftoc(temp)  # function call to ftoc
    else:
        return ctof(temp)
        

temp = int(input("Enter a temperature: "))                
scale = input("Enter the scale to convert to: (c or f) ")
converted = convert(temp, scale)
print(temp, converted, scale)

print("===========================================")

# Predicate functions - often used as helper functions that return True or False

def isVowel(l):
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        return True  # if the letter is a vowel, return True
    else:
        return False # else, return False
        
def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):  # for each character
        if isVowel(string[i]):  # calling function above
            count += 1  # increment count
    return count
    
    
theStrng = input("Enter a string: ")
print("There are " + str(numVowels(theStrng)) + " vowels in the string.")

print("===========================================")

# Calculating tax on a given amount

# Writing two functions:
# 1. computes tax based on a gross amount
# 2. calculates a net pay using the tax function (written previously)

# 0-240:    0%
# 241-480: 15%
# 481-:    28% 

def tax(amount):
    if amount <= 240:
        return 0
    elif amount > 240 and amount <= 480:
        return amount * .15
    else:
        return amount * .28
        
def netpay(grosspay):
    return grosspay - tax(grosspay)
    

# Testing tax            
amount = int(input("Enter amount of money: "))                            
print("The tax is: " + str(tax(amount)))

# Testing netpay
gp = int(input("Enter gross pay: "))
print("Net pay is " + str(netpay(gp)))

print("===========================================")

