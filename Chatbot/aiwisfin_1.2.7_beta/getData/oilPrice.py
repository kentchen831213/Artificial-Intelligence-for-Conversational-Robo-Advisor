# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:08:56 2018

@author: Deng
"""

from bs4 import BeautifulSoup as bs4
import requests
import re

def getOilPrice():
    r=requests.get('https://gas.goodlife.tw/')
    soup = bs4(r.text,'html.parser')
    now =soup.select('div#rate li')[0].text.strip()  
    rate = soup.select('div#rate li')[5].text.strip()
    b=soup.select('div#rate li')[7].text.strip()
    w=soup.select('div#rate li')[8].text.strip()    
    result = str(now)+'\n'+str(rate)+'\n'+str(b)+'\n'+str(w)
    result=re.sub(' ','',result)
    return result
                     
