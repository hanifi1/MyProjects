#######################################################################
###  https://ca.indeed.com/jobs?q=finance+analyst&l=Montr%C3%A9al%2C+QC###########
#######################################################################

import requests
import bs4
import pandas as pd
#%%

add_1 = 'https://en.wikipedia.org/wiki/Lists_of_writers'
#page = requests.get('https://www.newswire.ca/news/air-canada?page=1&pagesize=100')
add_2 = 'https://www.newswire.ca/news/air-canada?page=1&pagesize=100'
add_3 = 'https://www.cision.ca/resources/'
page = requests.get(add_2)





#soup = bs4.BeautifulSoup(page)

soup = bs4.BeautifulSoup(page.content, 'html.parser')
names = soup.findAll('a')
#%%
BaseURL = 'https://www.newswire.ca'

Titr = []
URL = []

for i in range(1, 11):
    add = 'https://www.newswire.ca/news/air-canada?page=' + str(i) + '&pagesize=100'
    page = requests.get(add)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    names = soup.findAll('a')
    print(add)
    for name in names:
        try: 
            if name.string.find('Air Canada') >= 0:
                Titr.append(name.string[:30])
                URL.append(BaseURL + name.get('href'))
        except AttributeError:
            pass
#%%



#%%

df = pd.DataFrame(data={'Titr': Titr, 'URL': URL})
df.to_csv('df.csv')
#%%


# News Text
df['text'] = ''

for i in range(0, 10):
    Link  = df.loc[i, 'URL']
    print(Link)
    link_page = requests.get(Link)
    link_soup = bs4.BeautifulSoup(link_page.content, 'html.parser')
    df.loc[i,'text'] = link_soup.get_text()
    print(i)

df.to_csv('df_air_canada_100_test.csv')

#%%

#for text in texts:
 #   print(text.string)

# print(texts)

#%%
# import io

# with  open('my_text.txt', 'w', encoding="utf-8") as f:
#     f.write(df.loc[1, 'text'])


#for line in df.loc[1, 'text']:
 #   textF.write(line)
  #  textF.write("\n")
#textF.close()





















