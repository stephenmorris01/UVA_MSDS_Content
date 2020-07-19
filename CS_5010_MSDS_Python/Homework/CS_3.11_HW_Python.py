###Homework: Python###
## Kip McCharen (cam7cu)

print("=============================================")   
#%%
# Q1: Dictionary basics: (2 pts)
import pandas as pd 
import re 

## I have opted to start with a list of dictionaries of Monty Python's filmography!
## Each item in the list is a dictionary of what type, the title, and what year it was released. 
## Due to the depth of content, I am counting each season of Flying Circus as 1 entry. 
monty_python_screen_projects = [{"Type": "TV", "Title": "Monty Python's Flying Circus Series 1", "Year": 1969}, {"Type": "TV", "Title": "Monty Python's Flying Circus Series 2", "Year": 1970}, {"Type": "TV", "Title": "Monty Python's Flying Circus Series 3", "Year": 1972}, {"Type": "TV", "Title": "Monty Python's Flying Circus Series 4", "Year": 1974}, {"Type": "TV", "Title": "Monty Python's Fliegender Zirkus", "Year": 1972}, {"Type": "TV", "Title": "Parrot Sketch Not Included – 20 Years of Monty Python", "Year": 1989}, {"Type": "TV", "Title": "Monty Python Live at Aspen", "Year": 1998}, {"Type": "TV", "Title": "Python Night – 30 Years of Monty Python", "Year": 1999}, {"Type": "TV", "Title": "Monty Python's Personal Best", "Year": 2006}, {"Type": "Film", "Title": "And Now for Something Completely Different", "Year": 1971}, {"Type": "Film", "Title": "Monty Python and the Holy Grail", "Year": 1975}, {"Type": "Film", "Title": "Monty Python's Life of Brian", "Year": 1979}, {"Type": "Film", "Title": "Monty Python Live at the Hollywood Bowl", "Year": 1982}, {"Type": "Film", "Title": "Monty Python's The Meaning of Life", "Year": 1983}, {"Type": "Film", "Title": "Monty Python Live, (Mostly)", "Year": 2014}]
print(f"{len(monty_python_screen_projects)} entries of Monty Python film projects\n")

## A list of dictionaries is easily accepted by pandas to create a dataframe!
## Dataframes are much easier to query in complex ways than dictionaries. 
df = pd.DataFrame(monty_python_screen_projects)
print(df.head())
print('\n\n')

## I'd like to know some statistics based on the type.
by_type = df.groupby(['Type']).describe()
print(by_type)
##It looks like the average year for films is 1984, and 1983 for films. Not very different. 
print('\n\n')

## Let's extract some more data. I want to know which items have "Live" in 
## the title, and I want to categorize the films by decade instead of year. 
df['Live'] = df['Title'].apply(lambda x: bool(re.search('Live', x))) #use regex to search for "Live"
df['Decade'] = df['Year'].apply(lambda x: str(x)[:3]+'0s') #"hack" the year string to grab decade
ct = pd.crosstab([df['Live'],df['Type']], df['Decade'])
## viewed as a crosstab, we can see almost a plot of live vs not films and tv across decades. 
## They made only the occasional live thing through the middle and tail end of their careers.
print(ct)

print("=============================================")   

#%%
# Q2: Getting user input: (2 pts)
def ask_multiply_2_nums():
    """Request 2 numbers from a user and multiply them. Ensure 2 integers. """
    u = input("Hi there, what's your name?  ->   ") #always be nice to make friends
    print(f"Great! Nice to meet you {u}.\nI want to multiply two numbers. " + 
        "Pretty please enter two numeral digits for me to multiply:  " + 
        "(put a space between the two numbers.)")
    numlist = [] #initialize a place to store numbers and check for validity
    while len(numlist) != 2: #the only acceptable endpoint is a list of 2 integers
        try:
            nums = input("Enter the numbers here ->  ")
            #attempt to force the response into integers in a list
            numlist = [int(x.strip()) for x in nums.split(" ")]
        except: #if brute forcing the response doesn't work, try again!
            pass
        finally: 
            if len(numlist) != 2: #always give error message if insufficient answer
                print("Hey, that didn't look quite right, please try again.")
    mult = float(numlist[0] * numlist[1]) #do multiplication and convert to float
    print(f"Hey good news {u}! It worked, if we multiply {numlist[0]} x {numlist[1]} we get: {mult}")

ask_multiply_2_nums()

print("=============================================")   

#%%
# Q3: Converting code to use a while loop: (3 pts)
## literally copied most of the code from previous example, as requested
answer = "Watson"
max_guesses = 4 ##initialize how many guesses allowed

print("Here is a guessing game. You get three tries.")
response = input("What is the name of the computer that played on Jeopardy?")
print(f"you guessed {response}") ##always show user what they did
while response != answer and max_guesses > 0: #conditions on guess limit and correctness
    max_guesses -= 1 #always decrement the guess count
    if max_guesses == 1: 
        msg = "Sorry. One more guess: " #special message for 1 message left
    else:
        msg = "Sorry. Guess again: " 
    response = input(msg) 
    print(f"you guessed {response}") #always show the user what they did
if response == answer: #in case of success
    print("That is right!") 
else: #in case of total failure
    print("Sorry. No more guesses. The answer is " + answer + ".")

print("=============================================")   

#%%
# Q4: Counting each of the vowels: (3 pts)
vowels = ["a","e","i","o","u"] #list of vowels
sentence = "are you suggesting coconuts migrate" #starting sentence
vowelcounts = {x: 0 for x in vowels} #convert to dictionary with counters
for letter in sentence: #check each letter of the sentence (nice how a string self iterates as characters)
    if letter in vowels: #if the letter is in the vowels list, we can act
        vowelcounts[letter] += 1 #increment dictionary value by 1
print("The number of vowels in the sentence:")
print(vowelcounts) #print out values
print('\n'.join(["\n",sentence,"Not at all, they could be carried."])) #answer the question

print("=============================================")   

#%%
# Q5: Length of all the words in a sentence (based on exercise in pyScript13.py) (3 pts)
import re #I do love regex
sentence = "Listen. Strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony." #quality political science analysis
sentence = re.sub(r"(\.|,|')", "", sentence) #substitute zero length for all extra characters
sentence = sentence.lower().split(" ") #make all words lowercase, split sentence on spaces
sentence = [(x, len(x)) for x in sentence] #create tuples for each word and its length
sentence.sort(key= lambda x: x[1]) #use lambda to define key for sorting the list
print(sentence)

print("=============================================")   

#%%
# Q6: Map-Filter-Reduce examples: (3 pts)
##we don't need Map/Filter/Reduce. We also don't need those functions!
numbers = [1,2,3]
numberssq = [x**2 for x in numbers] #list comprehension will work fine
print(numberssq) # output: [1, 4, 9]

numbers = list(range(1,11)) # numbers 1-10 in a list 
evens = [x for x in numbers if x% 2 == 0] #we can use "if" in a list comprehension too
print(evens) # output: [2, 4, 6, 8, 10]

numbers = list(range(1,11)) # numbers 1-10 in a list
vsum = sum(numbers,0) #sometimes there's even a native function to accomplish the goal
print(f"The sum of the range is {vsum}") # 55

print("=============================================")   

#%%
# Q7: Classes and Inheritance: (4 pts)
##Thank you for the walkthrough! Mostly I followed the directions exactly, 
##but I added a few safeguards in to avoid someone hacking their account. 

class ACCOUNT:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
    def __str__(self):
        return f"Account number {self.accountNumber}\nBalance: ${self.balance:.2f}"

class CHECKING(ACCOUNT):
    def __init__(self, accountNumber, balance, fee):
        ACCOUNT.__init__(self, accountNumber, balance)
        if fee < 0: #we'll be subtracting the fee, so ensure it's positive
            fee = fee * -1 
        self.fee = fee
    def __str__(self):
        retStr = ACCOUNT.__str__(self)
        retStr += "\nAccount type: Checking\n" #I like adding spaces to read better
        return retStr
    def getFee(self):
        return self.fee
    def deposit(self, amount):
        if amount <= 0: 
            #We shouldn't allow anyone to drop someone's account using the deposit function. 
            #Also an amount of 0 is not a deposit. 
            print("You may not deposit a negative or zero amount.\n")
        else:
            self.balance += amount
            #always show a user what they did
            print(f"You have deposited ${amount:.2f}, your new balance " + 
                "is ${self.balance:.2f}\n")
    def withdraw(self, amount):
        if amount < 0: #if amt is negative, just turn it positive for math
            amount = amount * -1 
        elif amount > self.balance:
            print("Insufficient funds!") 
        elif amount == 0:
            print("A withdrawal of $0 has no effect.")#if withdraw is 0, just do nothing
        else:
            self.balance -= amount
            self.balance -= self.fee
            #always show a user what they did
            print(f"You have withdrawn ${amount:.2f}, your new balance is ${self.balance:.2f}\n")

#testing time, per instructions!
check1 = CHECKING("1234", 500, 0.50)
print(check1)
check1.withdraw(100)
print(check1)
check1.deposit(200)
print(check1)

print("=============================================")   