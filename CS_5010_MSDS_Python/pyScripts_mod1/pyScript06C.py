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