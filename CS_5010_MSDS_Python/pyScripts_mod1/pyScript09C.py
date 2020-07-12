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
