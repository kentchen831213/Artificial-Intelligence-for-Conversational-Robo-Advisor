# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:52:32 2018

@author: XuTingDeng
"""

import re
import requests

s='你好臺北'
s = re.sub('臺','台',s)

regex = re.compile('(台北|新北|台中|高雄)')

w = regex.search(s)




r=requests.get("http://www.tej.com.tw/webtej/doc/uid.htm")
r.encoding='big5'
soup = BeautifulSoup(r.text,'html.parser')

string=soup.text.strip()
string