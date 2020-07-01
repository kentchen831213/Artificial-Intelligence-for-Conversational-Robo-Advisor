from bs4 import BeautifulSoup
import requests


def getGolden():
    res = requests.get('https://www.goldlegend.com/')
    soup = BeautifulSoup(res.text,"html.parser")
    tables = soup.find_all('table')
    buy = tables[0].find_all('td')[2]
    sell = tables[0].find_all('td')[4]

    return (str('買進的黃金價格為' + buy.text.strip() + '賣出的黃金價格為 ' + sell.text.strip()))

