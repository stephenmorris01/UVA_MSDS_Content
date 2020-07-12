# File: pyScript10.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - For-loops, using a range, an index
#   - For-loops with tuples
#   - For-loops with dictionaries


## For-loops
# Like while-loops, the for-loop is another way to iterate over
# a set of statements

# The for-loop has some advantages over the while-loop, when working
# with data structures, including even files

# Format:

# for <target> in <collection>:  # target variable in some collection of data
#   statements

# Simple example:
for i in [1,2,3,4]:
    print(i)        # will display all of the numbers 1,2,3,4 in the list
print("")

# An iterator (an internal pointer) works its way through the list,
# taking each item out of the list and placing it in the target
# (e.g. the variable "i" above). Often times called the loop control variable

# Another example:
numbers = [1,2,3]
for x in numbers:  # Can use a variable representing a list
    print(x)       # prints out each element in the list like before
print("")

# Another example:
numbers = [1,2,3,4,5]
sum = 0
for x in numbers:
    sum = sum + x  # calculate the sum of the numbers in the list
print("The sum is: " + str(sum)+ "\n")

# Often a for-loop is used to extract values out of a data structure
# so that tasks can be performed on these items
# ** The for-loop is used to retrieve all the values in the structure **
# In the case above, the for-loop will iterate through all the 
# items in the list and stops when there are no more items in the list

print("=================================================")

# Using a for-loop to process characters in a string
# Remember a string is a sequence of data, just like a list, or any
# other structure. The string is a sequence of characters
word = "hello"
for letter in word:
    print(letter)	# should print h-e-l-l-o each on a new line
print("")    

# Count the number of vowels in a longer string (sentence)
sentence = "are you suggesting coconuts migrate"
count = 0   # keep track of the vowels found
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' \
            or letter == 'o' or letter == 'u':
        count = count + 1 # if letter is a vowel, increment the counter
print("\"" + sentence + "\"")
print("The number of vowels in the above sentence is " + str(count)) # print the result


# You are able to use the CONTINUE statement or the BREAK statement
# to modify the flow of control, but a for-loop is often used when
# we want to access all of the elements in the sequence

# Notes:
# While-loops are open-ended loops whereas for-loops are not since
# we can tell the range of the for-loop by looking at the code
# When processing a file, however, a while-loop is better suited since
# we do not know how many iterations are required (we may not know how
# many lines there are in the file to process)

print("=================================================")

# Processing a list with a for-loop
# Can use the for-loop with an index
numbers = [1,2,3,4,5,6,7,8]
for i in range(0,len(numbers)):
    print(numbers[i])  # print numbers sub i
print("")    
# Will print each number, one per line. Same if used "for number in numbers:"

# To access some partial set of the complete list
# Add one more argument to the range function, to indicate the increment
# Example of printing odd numbers
thenumbers = [1,2,3,4,5,6,7,8,9,10]
print("Printing odd numbers:")
for i in range(0, len(thenumbers), 2):
    print(thenumbers[i])
print("")


# As can be seen, even though the primary use of a for-loop is to 
# access each element in a sequence, it's not necessary to do so.
# All that is needed is to specify some type of range and an index 
# into the sequence to access the elements in that range

print("=================================================")

## For-loops with Tuples
# Tuples are like lists

print("Computing the sum:")
numbers = (1,2,3,4,5) # create a tuple of 5 numbers. Note the ()'s, not []'s
sum = 0
for num in numbers:
    sum = sum + num  # compute the sum
    print(sum)       # print each number
print("The sum is " + str(sum))
print("")

# Example using strings
words = ("data","science","is","fun") # A tuple of words
for word in words:
    print(word)    # display the words
print("")
    
# Figure out which word is the longest (using indexing into the tuple)
words = ("data","science","is","fun") # A tuple of words
max = 0  # assign max to index position 0
         # assume the first word in the tuple is the longest word
for i in range(1, len(words)):  # range starting at 1 to the end
    if len(words[i]) > len(words[max]):
        max = i  # change the index to point to current max word
                 # otherwise max doesn't change
print("The longest word is: " + words[max])

# Each iteration replaces the value of max with the index of the longest word
# so far. If the current word is shorter in length than the current max
# then max doesn't change, otherwise max is updated to record the current
# index representing the longest word so far. At the end of the loop
# max will point to the largest word. (In this case: "science". max: 1)


print("=================================================")

## For-loops with Dictionaries

# Example phone book - use a for-loop to display the dictionary
numbers = {'Michael':'4496', 'Angela':'2982', 'Sage':'7771'}
print(numbers.keys())  # display all keys in the dictionary (a list)
print(numbers.values())  # same for the values (a list)
for key in numbers.keys():  # Returns a list of keys (becomes the sequence)
    print(key + " extension is: " + numbers[key])
    # Should print out each name (key) with extensions (numbers[key])
print("")

