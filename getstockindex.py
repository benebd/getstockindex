import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = 'https://stock360.hkej.com/stockList/all/20220909?&p=1'

r = requests.get(url).text
bsObj = BeautifulSoup(r, 'html.parser')

page = bsObj.find('div',class_ = 'pagingWrap nopad')
num = int(page.findAll('span')[12].getText())
#print(num)
print(num , "page to crawl")
df = pd.DataFrame(columns=['stockid'])
for i in range(1,num+1):
    url1 = 'https://stock360.hkej.com/stockList/all/20220909?&p='+str(i)
    print("crawling page",i,url1)
    #print(i)
    r = requests.get(url1).text
    bsObj = BeautifulSoup(r, 'html.parser')
    #df = pd.DataFrame(columns=['stockid'])
    table = bsObj.find('table',class_= 'tbl_sl')
    #print(talbe)

    for row in table.findAll('tr'):
        columns = row.find_all('td')

        #print(columns)
        if(columns != []):
            stockid = columns[0].text.strip()
            df.loc[len(df.index)] = [stockid]
            #print(stockid)
print("finish crawling save csv file to home directory name hkstock_id.csv")

df.to_csv( '../hkstock_id.csv', index=False, header = True)
df = pd.read_csv('../hkstock_id.csv')
df.dropna(inplace = True)
df.to_csv( '../hkstock_id.csv', index=False, header = True)