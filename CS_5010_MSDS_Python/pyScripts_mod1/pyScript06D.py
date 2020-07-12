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