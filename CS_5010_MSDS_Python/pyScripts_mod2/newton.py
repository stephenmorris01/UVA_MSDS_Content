# File: newton.py
# CS 5010
# Learning Python (Python version: 3)

#   Used with: newtontest.py and newtontest2.py

import math

def average(x, y):  
# average of two numbers
    return (x + y) / 2

def square(number):  
# square a number
    return number * number

def sqrt(number): 
# Newton's way to approximate the square root of a number
    def closeEnough(guess):
       # math.fabs: returns the absolute value of the parameter
       # the math import: to use the method "fabs" from the math library
       return (math.fabs((square(guess)) - number) < 0.001)
    def improve(guess):
        return average(guess, (number / guess))
    def sqrtHelper(guess):
        if (closeEnough(guess)):
            return guess
        else:
            return sqrtHelper(improve(guess))
    return sqrtHelper(1.0)  