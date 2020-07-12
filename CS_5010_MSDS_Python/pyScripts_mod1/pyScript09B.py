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