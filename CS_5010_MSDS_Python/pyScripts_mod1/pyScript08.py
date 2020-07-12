# File: pyScript08.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Guessing game example using if-else statements
#   - While loops
#   - "continue" / "break"



## Guessing game using multiple if-else statements
# A better way to do this is to write a program using a loop
# At this time we've not covered loops yet, we will soon!

answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
# response = input()
response = input()
if response == answer:
   print("That is right!")
else:
   response = input("Sorry. Guess again: ")
   if response == answer:
      print("That is right!")
   else:
      response = input("Sorry. One more guess: ")
      if response == answer:
         print("That is right!")
      else:
         print("Sorry. No more guesses. The answer is " + answer + ".")

print("=============================================")                  

## While loops

# Format:

# while relationalExpression:   # while value of RE is true...
#   statements                  # elecute the statements inside the body

# There are two kinds of while loops:
#   - count-controlled
#   - event-controlled

# -- count-controlled while loop
number = 1
while number <= 10:
    print(number)
    number = number + 1     # Important!
print("----------")    
# Last line is important. Must be some statement that will eventually
# cause the relational expression to become FALSE (else infinite loop!)
# Eventually number will become 11, RE would be false --> end looping

# Few more examples:

# Sum of the numbers
sum = 0
number = 1
while number <= 10:
   sum = sum + number
   number = number + 1
print("The sum is " + str(sum))
print("----------")

# How much would the balance increase growing at a simple interest
# of 2% per year for 10 years
balance = 5000
rate = 1.02
year = 1
while year <= 10:
   balance = balance * rate
   print("Year: " + str(year) + ": " + str(balance))
   year = year + 1
print("----------")   

# -- event-controlled while loop

# Looks for some occurrence / some event to occur to make the loop stop

# Sentinel value: 
#    a value that carries special meaning in the program, if entered
#   it will be the event that stops the while-loop

# Sentinel value in the following example is (-1)

average = 0.0
total = 0
count = 0
print("Enter a grade (-1 to quit): ")
grade = int(input())
while grade != -1:
   total = total + grade
   count = count + 1
   print("Enter a grade (-1 to quit): ")
   grade = int(input())
average = total / count
print("Average grade: " + str(average))


print("=============================================")

## Use of continue and break in loops

# -- continue statement
# Using continue causes the loop to to stop in the middle of executing
# the body and continue with the next iteration of the loop - 
# meaning, back to the top and testing the RE, then continuing back
# into the body of the loop (if appropriate)

# Format:

# while RE:
#   statements
#   continue
#   statements

# Generally there is a check to make before continue is issued
# if RE:
#   continue  # remaining statements do NOT get executed

# continue example
# take numerator and denominator and display the quotient
# n/d (only if d != 0)
numer = 0
denom = 0
while denom != -1:
    numer = float(input("Enter a numerator: "))
    denom = float(input("Enter a denominator (-1 to end): "))
    if denom == 0:
       continue     # We do not want to calculate the rest of the stmts!
    print(numer / denom)
print("----------")

# -- break statement

# The break statement is used to immediately exit a loop (prematurely)
# when a certain condition occurs
# Then transfers control to the statement AFTER the loop

# Format:

# while RE:
#   statements
#   if RE:
#       break
#   statements
# <-- break transfers control to here (after the loop)

# break example
# Averaging some numbers
number = 0
total = 0
average = 0.0
count = 0
while True:
    number = float(input("Enter a number (-1 to break): "))
    if number == -1:
       break
    total = total + number
    count = count + 1
average = total / count
print("Average: " + str(average))

### NOTE: This is probably NOT the best way to write this program
###         It would be better to write it like the example to average
###         the grades using a sentinel value
###         This example was written for demonstration purposes only.