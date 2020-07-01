# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs4
from selenium import webdriver

def getPageSource():
	url = 'https://www2.moeaboe.gov.tw/oil102/oil1022010/A00/Oil_Price2.asp'
	driver = webdriver.PhantomJS(r'C:\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver.get(url)
	pageSource = driver.page_source
	soup = bs4(pageSource, 'html.parser')
	table = soup.findAll('table')[3]
	tr = table.findAll('tr')
	date = '2017/' + tr[0].findAll('td')[8].text.replace('2017','').replace('.','/')
	priceIWCON = tr[1].findAll('td')[7].text
	priceBREN = tr[2].findAll('td')[7].text
	priceDubai = tr[3].findAll('td')[7].text
	rates = tr[5].findAll('td')[7].text

	return '今天是' + date + '，西德州的原油價格為' + str(priceIWCON) + '元，北海布蘭特的原油價格為' + str(priceBREN) + '元，杜拜的原油價格為' + str(priceDubai) + '元，美金對台幣匯率為' +  str(rates)


if __name__ == '__main__':
	print(getPageSource())


# In[ ]:

