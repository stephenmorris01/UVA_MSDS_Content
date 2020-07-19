# -*- coding: utf-8 -*-
"""
In-Class Assignment 3: Map, Filter, Reduce
Filter Function Examples

Authors:
    Patrick Corbett- pjc8c1
    Benjamin Cosgro: bcc5d
    Haizhu Hong: hh3cy
    Luke Moles: lmm8fb
    Joseph Manderfield: jtm4qx
    Annamaria Landi: aol4h
    Amanda West: acw9gs
    Usheng Jiang: yj3tp
    Nikhil Daga: nd9hq
    Michael Kolonay: mhk9c
    Pantea Ferdosian Najafabadi: pf5aq

"""
#%%
def show_examples(explanation, function, input):
    """Instead of repeating the same text demonstrating the parts of the script, repeat it here."""
    print(explanation)
    print("Function: ", function)
    print(f"Before filtering: {input}")
    function = "print('After filtering: ',"+function+")"
    exec(function)
    print('\n')

show_examples("Example 1: Filter out blank list entries", "list(filter(None, input))", ["Dog","Cat","Pig","","Platypus","","Kangaroo"])
show_examples("Example 2: Keep only string length greater than 7", "list(filter(lambda word: len(word) > 7, input))", ["jump","zoom","sesquipedalophobia", "banana","thunderstorm"])
show_examples("Example 3: Filter out even numbers", "list(filter(lambda x: x % 2 == 1, input))", [2, 5, 13, 2338, 5633, 782])
show_examples("Example 4: Filter to only those that contain 'a'", "list(filter(lambda x: 'a' in x, input))", ["Dog","Cat","Pig","","Platypus","","Kangaroo"])

#%%Example 1: Filter out blank list entries
#Create a list with some blank entries to be filtered
myList = ["Dog","Cat","Pig","","Platypus","","Kangaroo"]
#Filter out blank entries
filter_result_myList = list(filter(None, myList))
print("Before filtering: {}".format(str(myList)))
print("After filtering: {}".format(str(filter_result_myList)))
'''
Before filtering: ['Dog', 'Cat', 'Pig', '', 'Platypus', '', 'Kangaroo']
After filtering: ['Dog', 'Cat', 'Pig', 'Platypus', 'Kangaroo']
'''

#%%Example 2: Keep only string length greater than 7
myList2 = ["jump","zoom","sesquipedalophobia", "banana","thunderstorm"]
filter_result_myList2 = list(filter(lambda word: len(word) > 7, myList2))
print("Before filtering: {}".format(str(myList2)))
print("After filtering: {}".format(str(filter_result_myList2)))
'''
Before filtering: ['jump', 'zoom', 'sesquipedalophobia', 'banana', 'thunderstorm']
After filtering: ['sesquipedalophobia', 'thunderstorm']
'''

#%%Example 3: Filter out even numbers
myList3 = [2, 5, 13, 2338, 5633, 782]
filter_result_myList3 = list(filter(lambda x: x % 2 == 1, myList3))
print("Before filtering: {}".format(str(myList3)))
print("After filtering: {}".format(str(filter_result_myList3)))
'''
Before filtering: [2, 5, 13, 2338, 5633, 782]
After filtering: [5, 13, 5633]
'''

#%%Example 4: Filter to only those that contain "a"

myList4 = myList
filter_result_myList4 = list(filter(lambda x: "a" in x, myList4))
print("Before filtering: {}".format(str(myList4)))
print("After filtering: {}".format(str(filter_result_myList4)))
'''
Before filtering: ['Dog', 'Cat', 'Pig', '', 'Platypus', '', 'Kangaroo']
After filtering: ['Cat', 'Platypus', 'Kangaroo']
'''
