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
