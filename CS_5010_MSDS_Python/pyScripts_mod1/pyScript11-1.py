# File: pyScript11.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - For-loops with files 
#   - Example using nested for-loops with files

## Using for-loops to process a file

# Reading a file line by line using readline():
#inFile = open('text.txt', 'r') # open file for reading
#line = inFile.readline() # read a line
#while(line):  # while there is data to read
#    print(line)
#    line = inFile.readline() # read another line
    
# Another example
#for line in open('text.txt'):
#    print(line)
    
# Reading grades file ("w2filegrades.txt") and calculating the average            
sum = 0
count = 0
for grade in open('w2filegrades.txt'):
    print(grade)
    sum = sum + int(grade)
    count = count + 1
average = sum / count
print("Average: " + str(average))
print("=============================================")

# Example using nested for-loops to build a histogram of the set of grades
# Will represent 5 points by one asterisk (*)

# File:  (Edit file to illustrate Histogram below)
# 90
# 77
# 85
# 65
# 100

print("\n\nHISTOGRAM:")
print("============================")
bar = ""  # variable to hold the asterisks
for grade in open('w2filegrades.txt'):  # loop through grades file
    for i in range(1, int(grade)+1):    # loop over range 1-(GR+1)
                    # to be inclusive of the actual number
        if i % 5 == 0:  # deciding if going to add an asterisk (using modulus)
            bar = bar + "*"
    print(bar, i)  # print the bar
    bar = "" # reset bar to empty string to begin collecting the next set of *'s
print("============================")

    


