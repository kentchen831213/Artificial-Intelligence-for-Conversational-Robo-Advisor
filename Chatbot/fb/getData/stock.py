#coding:utf-8
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from tabulate import tabulate

def getStock(code, query):
	reply = ''
	stock = [['Time','Market Price','Buy','Sell','Rise&Fall','Volume','Previous Close','Open','High','Low']]
	driver = webdriver.PhantomJS(executable_path = 'D:\\Anaconda3.6\\Scripts\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
	x = code
	r = driver.get('https://tw.stock.yahoo.com/q/q?s='+x)
	pageSource = driver.page_source
	soup = bs4(pageSource, 'html.parser')
	tables = soup.find_all('table')
	row = tables[5].find_all('td')[0].findAll('tr')[1].findAll('td')[1:-1]
	for item in row:
		row[row.index(item)] = item.text.strip()
	if query == '市價':
		reply = row[1]
	elif query == '買價':
		reply = row[2]
	elif query == '賣價':
		reply = row[3]
	elif query == '成交量':
		reply = row[5]
	elif query == '前一天收盤價':
		reply = row[6]
	elif '開盤' in query:
		reply = row[7]
	elif '最高' in query:
		reply = row[8]
	elif '買低' in query:
		reply = row[9]

	return (code + ' 的' + query + '是 ' + reply + 'ㄛ~~~~<3')
