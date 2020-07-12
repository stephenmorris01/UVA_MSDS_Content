# File: pyScript06E.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Final example for redirecting standard output
# -----------------------------------------
# - Writing to the file:  pyScript06E.txt -
# -----------------------------------------

import sys
 
## Handy function to write to a file
def redirect_to_file(text):  
    # Save reference to sys.stdout (screen)
    original = sys.stdout
    
    # Redirect stdout to a file
    sys.stdout = open('pyScript06E.txt', 'w')
    
    # Print to the file
    print('This is your redirected text:')
    print(text) # Writes the text from the parameter to the file
    
    # Restores stdout back to the screen
    sys.stdout = original
    
    # This output goes to stdout, NOT the file!
    print('>>> DONE! <<<')
 
if __name__ == '__main__': 
    redirect_to_file('Python rocks!')  # Gets written to the file
    
    # The file looks like this:
    print("-----\n>>> Printing the contents of pyScript06E.txt file: \n")
    print(open('pyScript06E.txt').read())