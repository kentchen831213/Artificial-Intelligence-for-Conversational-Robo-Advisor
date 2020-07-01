
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re


# In[129]:


def get_Civil(no):
    r = requests.get('https://law.moj.gov.tw/LawClass/LawSingle.aspx?Pcode=B0000001&FLNO='+no)
    soup = BeautifulSoup(r.text,'html.parser')
    row = soup.find_all('table')[0].find_all('tr')[6].find_all('td')[2].find_all('pre')[0]
    regex = re.compile(r'</?[^>]+>')
    clean = regex.sub('',str(row))
    return clean
def get_constitution(no):
    r = requests.get('https://law.moj.gov.tw/LawClass/LawSingle.aspx?Pcode=A0000001&FLNO='+no)
    soup = BeautifulSoup(r.text,'html.parser')
    row = soup.find_all('table')[0].find_all('tr')[5].find_all('td')[2].find_all('pre')[0]
    regex = re.compile(r'</?[^>]+>')
    clean = regex.sub('',str(row))
    return clean
def get_criminal(no):
    r = requests.get('https://law.moj.gov.tw/LawClass/LawSingle.aspx?Pcode=C0000001&FLNO='+no)
    soup = BeautifulSoup(r.text,'html.parser')
    row = soup.find_all('table')[0].find_all('tr')[5].find_all('td')[2].find_all('pre')[0]
    regex = re.compile(r'</?[^>]+>')
    clean = regex.sub('',str(row))
    return clean

def get_Sexual():
    return("刑法:\n 第 227 條 （未成年人性侵害）\n第 227-1 條 （減刑或免刑）\n第 228 條 （利用權勢性交或猥褻罪）\n第 229 條 （詐術性交罪）\n第 229-1 條 （告訴乃論）\n第 332 條 （強盜結合強制性交罪）\n第 334 條 （海盜結合強制性交罪）\n第 348 條 （擄人勒贖結合強制性交罪）")

# In[130]:


print(get_Civil('1'))

