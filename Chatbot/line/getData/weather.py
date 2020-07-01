#coding:utf-8
import requests

from bs4 import BeautifulSoup

def getWeather(city,question):
    
   
    site={'台北':'Taipei','新北':'New_Taipei','桃園':'Taoyuan','台中':'Taichung',
          '台南':'Tainan','高雄':'Kaohsiung','基隆':'Keelung','嘉義':'Chiayi',
          '新竹':'Hsinchu','苗栗':'Miaoli','彰化':'Changhua','南投':'Nantou',
          '雲林':'Yunlin','屏東':'Pingtung','宜蘭':'Yilan','花蓮':'Hualien',
          '台東':'Taitung','澎湖':'Penghu'}
    
    if city=='台北' or city=='台北'or city== '新北' or city== '桃園' or city== '台中'or city=='台南'or city== '高雄'or city== '基隆':
        r=requests.get("https://www.cwb.gov.tw/V7/forecast/taiwan/"+site[city]+"_City.htm")
    else:
        r=requests.get("https://www.cwb.gov.tw/V7/forecast/taiwan/"+site[city]+"_County.htm")
        
        
    
    
        
        
     
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text,'html.parser')
    tables = soup.find_all('table')
    tr = tables[0].find_all('tr')
    td = tr[1].find_all('td')


    temperature = td[0].text.strip()
    weather = td[2].text.strip()
    
    #氣溫
    if question==0:
        return ("氣溫:"+temperature+"°C")
    #天氣如何
    elif question==1:
        return (weather)
    else:
        return("氣溫:"+temperature+'°C'+'\n'+weather)


