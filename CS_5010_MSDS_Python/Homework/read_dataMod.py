# File: read_dataMod.py
# CS 5010 Learning Python (Python version: 3)
# Kip McCharen (cam7cu)

# Demonstrating use of pandas using comScore Media Metrix data set
# ( Key_Measures_December_2013_Mod.csv )
#%% #BASIS PROVIDED BY PROF BASIT, THANKS!
from numpy import *
import pandas as pd

pd.set_option('display.max_columns', None)
beginningRows = list(range(7))
endingRows = list(range(6941,6979))
skips = beginningRows + endingRows
useTheseCols = list(range(0,13))
df = pd.read_csv('Key_Measures_December_2013_Mod.csv',skiprows=skips,usecols=useTheseCols,header=0,encoding = "ISO-8859-1")
df.rename(columns={'Unnamed: 0' : 'Webpage Reference'},inplace=True)
df.rename(columns={'Category' : 'CATEGORY'},inplace=True)

#%% #Gathering Spaces
# The Webpage Reference column provides the name of the entity described by the row.
# I notice that the hierarchy is defined by the use of spaces at the front. 
# If I remove the string remaining after stripping spaces before and after, 
# I can count how many spaces there are and extract the hierarchy. 
df['refSpaces'] = df['Webpage Reference'].apply(lambda x: x.replace(x.strip(), "").count(' ')) #add a new column counting the number of leading spaces, "refSpaces"
df.hist(column='refSpaces') #histogram showing the distribution of spaces

#%% #Descriptive statistics on the spaces defining hierarchy
print(df['refSpaces'].describe()) 
#It looks like the minimum # of spaces is 4, so that must be the top of the hierarchy.

# %% Top Level Companies
topref = df[df['refSpaces'] == 4] #make a new DF limited to only rows with 4 spaces
#Now finally trim away the extra spaces so we can more easily read the company names.
topref['EntityName'] = topref['Webpage Reference'].apply(lambda x: x.strip())
namelist = topref.EntityName.unique().tolist() #convert the column to a list
print(sorted(namelist)) #show the sorted list of companies

# %% Companies by % Reach
import plotly.express as px
#using plotly we can make an interactive graph of the % reach in descending order
topref = topref.sort_values(by=['% Reach'], ascending=False) #sort the df by reach
fig = px.bar(topref, x='EntityName', y='% Reach') #create simple bar graph
fig.show()
#Yahoo, Google, and Microsoft were leagues above everyone else in reach!

#topref.head(10)
# %% Comparing Reach with Minutes on the Site
# There's more to it than reach, how much time did people actually spend 
# on the sites being exposed to ads, thus generating revenue? 
# Using plotly again we can make a scatter plot of minutes x reach.
fig = px.scatter(topref, x='Total Minutes (MM)', y='% Reach', hover_data=['EntityName'], title="Dec 2013 Website Key Measures")
fig.show()
#Now it's easier to see just how completely Google outstripped everyone
