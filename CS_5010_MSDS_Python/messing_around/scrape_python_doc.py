from bs4 import BeautifulSoup
import requests 
import pandas as pd 

url = r"https://docs.python.org/3/library/functions.html"

page = requests.get(url).text
soup = BeautifulSoup(page, "lxml")
linkrefs = soup.find('div' , id='built-in-functions').findAll('dl') #attrs={'class':'winery-list__item'})
refs = []

for link in linkrefs:
    head = link.find('dt')
    body = link.find('p')
    def_funct = {'funcname': head.text[1:-2]}
    def_funct['bod'] = body.text.split('. ')[0]
    def_funct['bod_long'] = body.text
    refs.append(def_funct)
pd.DataFrame(refs).to_csv(r"D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\default_functions.csv", encoding='latin1')