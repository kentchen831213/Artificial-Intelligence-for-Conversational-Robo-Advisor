import requests
from bs4 import BeautifulSoup

def getCurrency(c):
    res = requests.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
    soup = BeautifulSoup(res.text,'html.parser')
    Currency = soup.find_all(class_='hidden-phone print_show')
    Rate = soup.find_all(class_='rate-content-cash text-right print_hide')
    if c=='美金':
        return (str('美金買入價格為:'+Rate[0].text.strip()+',賣出價格為:'+Rate[1].text.strip()))
    elif c=='日元':
        return (str('日元買入價格為:'+Rate[14].text.strip()+',賣出價格為:'+Rate[15].text.strip()))
    elif c=='人民幣':
        return (str('人民幣買入價格為:'+Rate[36].text.strip()+',賣出價格為:'+Rate[37].text.strip()))
    elif c=='歐元':
         return (str('歐元買入價格為:'+Rate[28].text.strip()+',賣出價格為:'+Rate[29].text.strip()))
    elif c=='英鎊':
         return (str('英鎊買入價格為:'+Rate[4].text.strip()+',賣出價格為:'+Rate[5].text.strip()))
    else:
        return '請輸入美金，日元，人民幣，歐元，英鎊'
     
        

         

        

    
    
   


