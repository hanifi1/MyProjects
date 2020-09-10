# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 00:00:33 2020
#https://realpython.com/python-web-scraping-practical-introduction/
#https://realpython.com/beautiful-soup-web-scraper-python/
#https://www.datacamp.com/community/tutorials/web-scraping-using-python
@author: hanif
"""

import requests
import pandas as pd

import re
clean = re.compile('<.*?>')

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

df = pd.read_csv('D:/Machine Learnaing/Web_Scrapping/df.csv')
# print(df)
#%%

def read_link(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    BeautifulSoup(html, 'lxml')
    return soup

def read_title(soup): 
    ti = soup.title
    clean_ti = str(ti)[7:-8]
    return clean_ti


def texts_list(soup):
    texts = soup.find_all('p')
    text_list = []
    for text in texts:
        clean_text = (re.sub(clean, '',str(text)))
        text_list.append(clean_text)
    return text_list

def text_date(List):
    return List[6]

# def main_text(List):
#     main = List[8:-12]
#     d = text_date(List)
#     f = open( d + '.txt', 'w')
#     for t in main:
#         f.write(t + '\n')
#     f.close()
    
        
#%%

df['title'] = ''
df['Date'] = ''


for i in range(10):
    link = df.loc[i, 'URL']
    print(link)
    soup = read_link(link)
    df.loc[i, 'title'] = read_title(soup)
    List = texts_list(soup)
    Date = text_date(List)
    df.loc[i, 'Date'] = Date
    print(Date)         # test progres
    main = List[8:-12]
    f = open(Date + '.txt', 'w')
    for t in main:
        f.write(t + '\n')
    f.close()
#%%%

df.to_csv('df_update.csv')



#%%
link = df.loc[2, 'URL']
print(link)

su = read_link(link)



#%%

list = texts_list(su)

d = text_date(list)

main_text(list)
