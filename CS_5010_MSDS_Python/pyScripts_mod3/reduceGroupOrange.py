#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:56:10 2020

@author: Ashley
"""
#%%
#In-Class Assignment 3: Map, Filter, Reduce
#Reduce examples
#ams5zx, hk5kp, js2yp, ph3bz, bgd5de, 
#rz3jr,ss8ch, cx2rx, egl6a, cm2rh

#%%
#Example 1
from functools import reduce

#Calculate Factorial
def factorial(num):
    data = list(range(1,num+1))
    fact = reduce(lambda x,y:x*y, data)
    return fact
print(factorial(5))

#%%
#Example 2
#Make Acronym
def first_up(word):
    return word[0].upper()
def acronym(words):
    acro = ''
    acro = list(map(first_up,words))
    acro = reduce(lambda x,y: x+y, acro)
    return acro
words = ['international','soil', 'moisture', 'Network']
print(acronym(words))

#%%
#Example 3
#Make One Sentence
data = ['convert','this','list','to','one','sentence']
one_list = (reduce(lambda x,y:x + ' ' + y,data))
print((one_list))

#%%
#Example 4
#Find the largest value in a list
lis = [1,4,2,6,8,7]
mx = reduce(lambda a,b : a if a > b else b, lis)
print(mx)