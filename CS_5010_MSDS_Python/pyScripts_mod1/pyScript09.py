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
