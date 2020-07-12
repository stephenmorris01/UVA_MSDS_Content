#1. In-Class Assignment 2: Python
#2. Kip McCharen
#3. cam7cu

import requests
from bs4 import BeautifulSoup
import re
import collections

url = r"http://www.montypython.net/scripts/petshop.php" #get the monty python petshop sketch script
soup = BeautifulSoup(requests.get(url).text, "lxml") #grab the page html
script = soup.find('div' , id="content").text #thanks beautifulsoup, get only the main text

se = ["Customer:", "LUMBERJACK!"] #start and end of the text i care about
se = [script.find(se[0]) + len(se[0]) + 1, script.find(se[1]) + len(se[1]) + 1] #transform those words to character indexes
script = script[se[0]:se[1]] #reduce text to what I care about

#remove text I don't care about from list
remove_list = ["pause", "The owner does not respond", "C", "O"]
for rl in remove_list: 
    script = script.replace(rl, "")

print("Finally, print out all the words (along with the word length).\n")
word_list = re.findall(r"[\w'\/\-\*]+",script) #grab all the words with characters I accept, re returns a list
word_lengths = [(word, len(word)) for word in word_list] #convert to tuples as instructed
print(word_lengths) 

print(('\n'*4)+'Print out the word-size tuples in sorted order by length (smallest to largest)\n')
word_lengths = sorted(word_lengths, key = lambda x: x[1]) #sort using lambda to capture value
print(word_lengths) #

print(('\n'*4)+'Done that, too?   Print out only unique words (i.e., no repetitions).\n')
word_instances = dict(collections.Counter(word_list)) #thank you Collections, just use Counter
used_once = dict(filter(lambda x: x[1] == 1, word_instances.items())) #using lambda to filter the dict
used_once = sorted(used_once, key = lambda x: x[0]) #sort using lambda to capture value
print(used_once)