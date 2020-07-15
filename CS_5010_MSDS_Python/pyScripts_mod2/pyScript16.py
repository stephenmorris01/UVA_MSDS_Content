# File: pyScript16.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Modules and importing modules


# A user defined module is just a Python program that we
# import into another program, so that we can use the code
# that was defined in the module

# Example: Files newton.py, newtontest.py, and newtowntest2.py
# newton.py has nothing more than function definitions

# You use the key word "from" to import a module that is user-defined
# Format:
# from moduleName import *   (or function names comma separated)
# e.g.  from newton import *

# ===> Review files newton.py, newtontest.py, and newtontest2.py

# =================================================================

# Another way to import a module is simply to use the key word import

# Example:
# import newton

# You must be careful when importing your own modules. You cannot
# simply call a function even though we know it is defined in the file and
# we're importing that module (e.g. import newton)

# Need to QUALIFY the name of the function  by naming the module first
# Example:
import newton

print(newton.sqrt(9))

# HOWEVER, if you use   from newton import *
# you DON'T have to qualify the function names with the module name

#====================================================================

# ===> Review files sphere.py and spheretest.py
