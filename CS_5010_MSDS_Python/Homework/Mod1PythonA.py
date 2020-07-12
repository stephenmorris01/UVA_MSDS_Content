#1. In-Class Assignment 1: Python
#2. Kip McCharen
#3. cam7cu

import json
import os

def ask_person():
    """Ask a person through command line their first name, last name, and age. Returns dict {last-first: age}. """
    qs = {'fname': "First name", 'lname': "Last name", 'age':"Age"} #list of Qs
    ret = {} #create dict to save results
    print("OK friend, I have some questions:")
    for q in qs: #iterate Qs
        ret[q] = input("{:<40}".format("Please enter your "+qs[q])).strip() #provide Q to user
    print("Wonderful, thank you!")
    print("")
    return {"{}-{}".format(ret['lname'],ret['fname']): ret['age']}  #Return dict {last-first: age}

def ask_how_many(count, outputdir):
    """Use the ask_person function on n persons at same terminal, and output file of their data to given dir. """
    peopledict = {} #create dict to save results

    for _ in range(count): #iterate n given times
        peopledict.update(ask_person()) #add each iteration's data to peopledict

    with open(outputdir, 'w') as f: #open new file to save in given dir
        f.write(json.dumps(peopledict)) #write json dump of dictionary for raw string

currdir = os.path.dirname(os.path.abspath(__file__)) #check exact location of this py file
ask_how_many(4, currdir + r"\myOutput.txt") #complete assignment