# File: pyScript07.py
# CS 5010
# Learning Python (Python version: 3)
# Topics: 
#    - Getting input from the user
#    - If-statement // if-else statement // if-else-if statement


## Getting input from the user 

name = input("What is the name of the gift giver? ")
present = input("What did they give you? ")
age = int(input("How old are you? "))  # remember int() function!
myname = input("What is your name? ")
print("")

print("Dear " + name + ", ")
print("")
print("Thank you so much for the " + present + "!")
print("It was so nice. I can't belive I am " + str(age))
print("years old. Doesn't seem any different than when ")
print("I was " + str(age-1) + "!")
print("")
print("Sincerely, " + myname)

print("=====================================================")

## If-statement
# Comparisons are made using relational operators (returns a Boolean result)
# (True or False) Will combine relational expressions using logical operators.

# -- logical operators, examples: and, or, and not
hoursWorked = 39
salary = 39000
print((hoursWorked > 40) and (salary <= 50000)) # False

password = 'GUEST'
print((password == 'guest') or (password == 'GUEST')) # True

print(not(100 == 100)) # False
print(not(100 < 1)) # True

print("=====================================================")

# if-statement

# format:

# if relationalexpression:
#       statements

# if RE1 and RE2:       # using logical operator, like 'and'
#       statements

# -- simple if
hoursWorked = int(input("Enter hours worked: "))
rate = 25.00 # Amount per hour
if hoursWorked > 40:
    grossPay = (40 * rate) + ((hoursWorked - 40) * (rate * 1.5))
if hoursWorked <= 40:
    grossPay = hoursWorked * rate
print("Gross pay: " + str(grossPay))

# Second if-statement really isn't needed...

# if-else statement

# Format:
# if RE:
#   statementsA
# else:
#   statementsB

# RE is evaluated, if it is True, then execute statementsA, otherwise
# execute statementsB (RE was evaluated to be False)
# Therefore, one set of statements are executed

# -- if-else statement
hoursworked2 = int(input("Enter hours worked: "))
rate = 25.00 # Amount per hour
if hoursworked2 > 40:
    grossPay = (40 * rate) + ((hoursworked2 - 40) * (rate * 1.5))
else:     # No need for second if statement!
    grossPay = hoursworked2 * rate
print("Gross pay: " + str(grossPay))

# if-else-if statement

# Format:
# if RE1:
#   statementsA
# elif RE2:
#   statementsB
# elif RE3:
#   statementsC
# else:             # Optional else section
#   statementsD     

# elif stands for "else if"
# Order is very important here

# -- if-else-if statement
grade = int(input("Enter a numeric grade: "))
letterGrade = ""
if grade >= 90:
    letterGrade = "A"
elif grade >= 80:
    letterGrade = "B"
elif grade >= 70:
    letterGrade = "C"
elif grade >= 60:
    letterGrade = "D"
elif grade <= 59:
    letterGrade = "F"
else:
    print("Did not recognize input!")
    
print("Your letter grade is: " + letterGrade)


print("=====================================================")


