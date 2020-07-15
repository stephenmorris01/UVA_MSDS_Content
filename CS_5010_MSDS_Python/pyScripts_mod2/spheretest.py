# File: spheretest.py
# CS 5010
# Learning Python (Python version: 3)

#from sphere import *
import sphere

radius = int(input("Enter the radius of the sphere: "))

# No need for including module name when using   from sphere import *
#print("The area is " + str(area(radius)))
#print("The volume is " + str(volume(radius)))

# Using fully qualified name when using:   import sphere
print("The area is " + str(sphere.area(radius)))
print("The volume is " + str(sphere.volume(radius)))