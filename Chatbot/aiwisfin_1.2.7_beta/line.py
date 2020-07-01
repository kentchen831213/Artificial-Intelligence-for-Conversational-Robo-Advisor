from flask import Flask, send_file, send_from_directory, request, jsonify, render_template, abort


from getData.weather import getWeather
from getData.runAIML import runAIML
from getData.stock2 import getfixstock
from getData.oilPrice import getOilPrice
from getData.golden import getGolden
from getData.Currency import getCurrency
from getData.data import getSite,getStock,getStocNum
import sqlite3 as lite
import re
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests
from bs4 import BeautifulSoup






application = Flask(__name__, static_url_path='', template_folder='templates')

line_bot_api = LineBotApi('qdLjteAVKJ6iSgHoK9tNFbtt70EZZiDL46zzeYe/oOtYcKVAnpCYdxE0rDJ9qkX2LaXoaJUwI60jdNmPuEE+icH2a3w/vZIoploibUU/e1PVRVP3++KRP5CNknJyuRe0kv8Fy67V3a9ConpTCn9CNwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('47966f59dc72d9968a9f5c1723a42a7c')
client_id = 'e2ea26870a49672'
client_secret = '70b5f459ee8ec821081e376718acb3083010d89f'
album_id = 's9O5n'
API_Get_Image = 'API_Get_Image'
image_id ='bxnjoaP'

con = lite.connect('mydatabase.sqlite')
cur = con.cursor()
sqlinset = 'insert into qa(question,answer)values(?,?)'


@application.route("/")
def index():
    return render_template('index.html')

@application.route("/get")
def get_bot_response():
    query =request.args.get('msg')
    reply = "抱歉，我聽不懂"
    if (request.args.get('msg')=="天氣如何"):
        return str("請問你要問何處的天氣呢?")
    elif(re.search('學習模式;',query)!=None):
        query = query.split(";")
        ret=query
        cur.execute(sqlinset,ret[1:])
        con.commit()
        return str("已經學習! 問題:"+query[1]+" 回答:"+query[2])
    elif(re.search('天氣',query)!=None):
        regex = re.compile('(台北|新北|台中|高雄|台南|桃園|基隆|新竹|雲林|南投|嘉義|苗栗|彰化|花蓮|台東|澎湖|宜蘭)')
        query = regex.search(query)
        reply=getWeather(query.group(1),2)
        return str(reply)
    elif(re.search(getStock(),query)!=None):
        stock = getStocNum()
        regex = re.compile(getStock())
        stockname = regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8} 
            stockCode =regex.search(query)
            reply =  getfixstock(stock[stockname.group(0)],select[stockCode.group(0)])
        else:
            reply = getfixstock(stock[stockname.group(0)],0)
        return str(reply)
    
    elif(re.search('油價',query)!=None):
        reply = getOilPrice()
        return str(reply)
    
    elif(re.search('黃金',query)!=None):
       reply = getGolden()
       return str(reply)
    elif(re.search('(美金|日圓|日元|人民幣|英鎊|歐元)',query)!=None):
        regex = re.compile('(美金|日圓|日元|人民幣|英鎊|歐元)')
        query = regex.search(query)
        reply = getCurrency(query.group(1))
        return str(reply)
    elif(re.search('\d',query)!=None):
        regex = re.compile('\d+')
        stocknum=regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8} 
            stockCode =regex.search(query)
            reply =  getfixstock(stocknum.group(),select[stockCode.group(0)])
        else:
            reply = getfixstock(stocknum.group(),0)
        return str(reply)
        
    else:
        cur.execute('select * from qa where question =? order by Random()',[query])
        ret = cur.fetchone()
        
        if ret != None:
            return (ret[1])
        elif(ret ==None):
            return str( runAIML(query))
        else:
            return str(reply)
   



@application.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    application.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = "我不知道你在說什麼"
    query = event.message.text
    query = query.upper()
    query = re.sub('臺','台',query)
    if(re.search('氣溫',query)!=None):
        regex = re.compile('(台北|新北|台中|高雄|台南|桃園|基隆|新竹|雲林|南投|嘉義|苗栗|彰化|花蓮|台東|澎湖|宜蘭)')
        query = regex.search(query)
        reply=getWeather(query.group(1),0)
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
    elif(re.search('天氣',query)!=None):
        regex = re.compile('(台北|新北|台中|高雄|台南|桃園|基隆|新竹|雲林|南投|嘉義|苗栗|彰化|花蓮|台東|澎湖|宜蘭)')
        query = regex.search(query)
        reply=getWeather(query.group(1),2)
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
    elif(re.search(getStock(),query)!=None):
        stock = getStocNum()
        regex = re.compile(getStock())
        stockname = regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8} 
            stockCode =regex.search(query)
            reply =  getfixstock(stock[stockname.group(0)],select[stockCode.group(0)])
        else:
            reply = getfixstock(stock[stockname.group(0)],0)
      
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
    
    elif(re.search('油價',query)!=None):
        reply = getOilPrice()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    
    elif(re.search('黃金',query)!=None):
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=getGolden()))
    elif(re.search('(美金|日圓|日元|人民幣|英鎊|歐元)',query)!=None):
        regex = re.compile('(美金|日圓|日元|人民幣|英鎊|歐元)')
        query = regex.search(query)
        reply = getCurrency(query.group(1))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('\d',query)!=None):
        regex = re.compile('\d+')
        stocknum=regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)',query)!=None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select ={'市':1,'買':2,'賣':3,'成交':4,'收':5,'開':6,'高':7,'低':8} 
            stockCode =regex.search(query)
            reply =  getfixstock(stocknum.group(),select[stockCode.group(0)])
        else:
            reply = getfixstock(stocknum.group(),0)
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))
    else:
        query = query.upper()
        response = runAIML(query)
        if response != '':
            reply = response
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))


if __name__ == "__main__":
    application.run()
