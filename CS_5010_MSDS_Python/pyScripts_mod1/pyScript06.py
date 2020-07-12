# File: pyScript06.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Redefining/redirecting standard out (stdout) to print to a file
#    - Redirecting standard out (stdout) back to printing to the screen
# ----------------------------------------
# - Writing to the file:  pyScript06.txt -
# ----------------------------------------

## Printing to a file rather than to the screen

import sys # import the sys library

# -- this is the usual way to print to the screen
# Use the standard out (stdout) object of the sys library. It has
# a function called write()
sys.stdout.write("Hello goes to the screen!\n")  # Output to screen
print("   Next: printing to the file!")

# Save the reference to sys.stdout (screen) so we can restore it later
original = sys.stdout

# Redirect stdout (by default it goes to the screen) to the file
sys.stdout = open('pyScript06.txt', 'a') # open file for appending ('a')

# Any print statement from now until the end of the session (or until stdout
# is redirected back) will print to the file (instead of to the screen)
print(">>> Hello! This should go to the file!")
print(">>> Here's another line that should go to the file!")

x = 5
y = 10
z = x + y
# This output should also go to the file:
print(str(x) + " plus " + str(y) + " is: " + str(z))

# * Open the file in your working directory, to see text printed to the file *

# Restore stdout back to it's original form (to the screen)
sys.stdout = original

# Now any print statement will show on the screen (and not go to the file) 
print("\n>> Exercise is done! Open file 'pyScript06.txt' <<")

# # For more information, read the "sys" module documentation.

# If you run into any trouble, you can restart the Kernel on Spyder 
# to restore settings. For any problem file, you may wish to do this 
# both before and after running the file. [Not necessary for this file]