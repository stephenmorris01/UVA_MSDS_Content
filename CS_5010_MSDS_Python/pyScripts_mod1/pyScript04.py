# File: pyScript04.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: Advanced printing techniques (including 'format string')

## Basic usagae of the str.zfill() method
## (pads a numeric string on the left with zeros)
## It understands about plus and minus signs

print('12'.zfill(5))       # Output: 00012
print('-3.14'.zfill(7))    # Output: -003.14
print('3.141592'.zfill(5)) # Output: 3.141592
#------------------------------------------------------------

## Basic usage of the str.format() method:
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# The brackets and characters within them (called format fields)
# are replaced with the objects passed into the str.format() method.
# A number in the brackets refers to the position of the object 
# passed into the str.format() method

print('{0} and {1}'.format('bits', 'bytes')) # Output: bits and bytes
print('{1} and {0}'.format('bits', 'bytes')) # Output: bytes and bits

# .........................

# If keyword arguments are used in the str.format() method, 
# their values are referred to by using the name of the argument.
print('On {day} it was {weather}.'.format(day='Friday', weather='sunny'))
# Output: On Friday it was sunny.

day = 'Wednesday'
weather = 'snowing'
print('On {0} it was {1}.'.format(day, weather)) # Using variables
# Output: On Wednesday it was snowing.
print("==================================")
#------------------------------------------------------------

## Format String
# If we have data like -
#   name = 'Mary'
#   grade = 81.7691
# and you want to display this data in one string, one way you can do this
# is to create a "format string" - telling Python how to display the data
name = 'Mary'
grade = 81.7691

record = '%s: %.2f' % (name, grade)
print(record)

# More examples (note how single or double quotes do not matter)
print('%.2f' % (182.7691))
print("%04d" % (87))   # Output: 0087   zero-fill 4 spaces


#------------------------------------------------------------
