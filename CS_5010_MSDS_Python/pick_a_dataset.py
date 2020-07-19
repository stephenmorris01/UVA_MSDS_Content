import pandas as pd 
import requests 
from bs4 import BeautifulSoup, Comment
import re

def getparentlist(savehere):
    parent_url = r"http://archive.ics.uci.edu/ml/datasets.php"
    page = requests.get(parent_url).text
    soup = BeautifulSoup(page, "lxml")
    tbl = soup.find('table' , attrs={'border':'1'})
    rows = tbl.findAll('tr')
    colnames = []
    rowdata = []
    for i,r in enumerate(rows):
        cols = r.findAll('td')
        currow = {}
        if i > 0:
            comment = soup.find(text=lambda text:isinstance(text, Comment))
            print(comment)
            quit()
        for ci, c in enumerate(cols):
            if i == 0:
                colnames.append(c.text)
            else:
                currow[str(ci)] = c.text
            if ci == 0:
                currow['URL'] = c.find('a')['href']
        rowdata.append(currow)
    print(colnames)
    df = pd.DataFrame(rowdata)
    df.to_csv(savehere)

def getchildpages(src, savehere):
    df = pd.read_csv(src, encoding="latin-1")
    urllist = list(set(df['URL'].to_list()))

    getpagedata = []
    for ul, real_url in enumerate(urllist):
        print(real_url)
        try:
            thispage = {'URL': real_url, 'ID': ul}
            page = requests.get(real_url).text
            soup = BeautifulSoup(page, "lxml").find('table' , attrs={'cellpadding':'2'}).find('td')
            thispage['header'] = soup.find('span', class_='heading').text
            datafsd = [x for x in soup.findAll("span",class_="normal") if 'Data Folder' in x.text][0]
            thispage['DataFolder'] = datafsd.find("a")['href']

            attrtbl = soup.find('table' , attrs={'cellpadding':'6'}).findAll("td")
            attrtbl = iter([x.text for x in attrtbl])
            attrtbl = {re.sub(r'(\xa0|:| |\?)', '',x, re.UNICODE): next(attrtbl) for x in attrtbl}
            thispage.update(attrtbl)
            
            for d in soup("table"):
                d.decompose()
            paragraphs = soup.findAll("p")
            paragraphs = iter([x.text for x in paragraphs])
            paragraphs = {re.sub(r'(\xa0|:| |\?)', '',x, re.UNICODE): next(paragraphs) for x in paragraphs}
            thispage.update(paragraphs)
            getpagedata.append(thispage)
            print("success")
        except:
            print("no luck")

    df2 = pd.DataFrame(getpagedata).set_index('ID')
    df2.to_csv(savehere)

if __name__ == '__main__':   
    dir1 = r"D:\Git\UVA_MSDS_Content\CS_5010_MSDS_Python\datasets.csv"
    dir2 = r"D:\Git\UVA_MSDS_Content\CS_5010_MSDS_Python\datasets2.csv"
    getparentlist(dir1)
    getchildpages(dir1, dir2)
