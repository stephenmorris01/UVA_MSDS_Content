import pandas as pd 
import re 
import numpy as np

#these accept regex in pandas:
# Methods	    Description
# count()	    Count occurrences of pattern in each string of the Series/Index
# replace()	    Replace the search string or pattern with the given value
# contains()	Test if pattern or regex is contained within a string of a Series or Index. Calls re.search() and returns a boolean
# extract()	    Extract capture groups in the regex pat as columns in a DataFrame and returns the captured groups
# findall()	    Find all occurrences of pattern or regular expression in the Series/Index. Equivalent to applying re.findall() on all elements
# match()	    Determine if each string matches a regular expression. Calls re.match() and returns a boolean
# split()	    Equivalent to str.split() and Accepts String or regular expression to split on
# rsplit()	    Equivalent to str.rsplit() and Splits the string in the Series/Index from the end

df = pd.read_csv('./world-happiness-report-2019.csv')
df['first_five_Letter']=df['Country (region)'].str.extract(r'(^w{5})')
print(df.head())
S=pd.Series(['Finland','Colombia','Florida','Japan','Puerto Rico','Russia','france'])
print(S[S.str.count(r'(^F.*)')==1])
# Total items starting with F
print(S.str.count(r'(^F.*)').sum())
print(df[df['Country (region)'].str.count('^[pP].*')>0])

# Get countries starting with letter P
S=pd.Series(['Finland','Colombia','Florida','Japan','Puerto Rico','Russia','france'])
print(S[S.str.match(r'(^P.*)')==True])

print(df[df['Country (region)'].str.match('^P.*')== True])

# Remove the dash(-) followed by number from all countries in the Series
S=pd.Series(['Finland-1','Colombia-2','Florida-3','Japan-4','Puerto Rico-5','Russia-6','france-7'])
print(S.replace('(-d)','',regex=True, inplace = True))

S=pd.Series(['Finland','Colombia','Florida','Japan','Puerto Rico','Russia','france'])
print([itm[0] for itm in S.str.findall('^[Ff].*') if len(itm)>0])
print(df[df['Country (region)'].str.contains('^I.*')==True])

s = pd.Series(["StatueofLiberty built-on 28-Oct-1886"])
print(s.str.split(r"s", n=-1,expand=True))