# File: newtontest2.py
# CS 5010
# Learning Python (Python version: 3)

from newton import average, square  # interested in these 2 methods

num1 = 199
num2 = 78
#print("The average is " + str(average(num1, num2)))
#print(sqrt(9))
avg = average(num1, num2)
print("The average is " + str(avg))
print("The square of the average " + str(square(avg)))