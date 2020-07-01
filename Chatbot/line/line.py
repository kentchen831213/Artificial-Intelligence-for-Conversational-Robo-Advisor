from flask import Flask, send_file, send_from_directory, request, jsonify, render_template, abort
from getData.weather import getWeather
from getData.runAIML import runAIML
from getData.stock2 import getfixstock
from getData.oilPrice import getOilPrice
from getData.golden import getGolden
from getData.Currency import getCurrency
from getData.data import getSite,getStock,getStocNum
from getData.law import get_Civil, get_constitution,get_criminal,get_Sexual
import re
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from getData.wiki import wiki_search




application = Flask(__name__, static_url_path='', template_folder='templates')

line_bot_api = LineBotApi('qdLjteAVKJ6iSgHoK9tNFbtt70EZZiDL46zzeYe/oOtYcKVAnpCYdxE0rDJ9qkX2LaXoaJUwI60jdNmPuEE+icH2a3w/vZIoploibUU/e1PVRVP3++KRP5CNknJyuRe0kv8Fy67V3a9ConpTCn9CNwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('47966f59dc72d9968a9f5c1723a42a7c')


@application.route("/")
def index():
    return render_template('1C.html')

@application.route("/en")
def index_eng():
    return render_template('1E.html')
@application.route("/chat")
def chat():
    return render_template('index.html')
@application.route("/chat_en")
def chat_eng():
    return render_template('index_en.html')
@application.route("/portfolio")
def portfolio():
    return render_template('2C_1.html')
@application.route("/portfolio_en")
def portfolio_eng():
    return render_template('2E_1.html')

@application.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@application.route('/statics/<path:path>')
def send_statics(path):
    return send_from_directory('statics', path)

@application.route('/_add_numbers')
def add_numbers():
    query = request.args.get('query')
    query = query.upper()
    query = re.sub('臺','台',query)
    reply = '很抱歉，無法替您解決此問題，建議點選上方Facebook圖示直接與我們聯絡'
    
    try:
        if(re.search('氣溫',query)!=None):
            regex = re.compile(getSite())
            query = regex.search(query)
            reply=getWeather(query.group(1),0)
        elif(re.search('(我姓|我叫|我是)',query)!=None):
            reply=query[2]+'先生(女士)您好!歡迎使用Aiwsifin智慧客服，請問需要哪些幫助呢?'
        elif(re.search('(先生|小姐)',query)!=None):
            reply=query[0]+'先生(女士)您好!歡迎使用Aiwsifin智慧客服，請問需要哪些幫助呢?'
        elif(re.search('投資組合',query)!=None):
            reply='請直接點選上方的「投資組合」選項，完成問卷後即可得知您專屬的投資組合建議'
        elif(re.search('ETF',query)!=None):
            reply ='是一種在證券交易所交易，提供投資人參與指數表現的指數基金。ETF將指數證券化，投資人不以傳統方式直接進行一籃子證券之投資，而是透過持有表彰指數標的證券權益的受益憑證來間接投資。'
        elif(re.search('證明',query)!=None):
            reply='<img src="https://cdn.discordapp.com/attachments/461176037397626880/489404601863503912/unknown.png" alt="https://cdn.discordapp.com/attachments/461176037397626880/489404601863503912/unknown.png" title="圖表">由圖表可顯示我們預測的價格與實際的價格相當接近'
            
        elif(re.search('民法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_Civil(query.group())
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
        elif(re.search('刑法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_criminal(query.group())
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
        elif(re.search('憲法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_constitution(query.group())
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
           
        elif(re.search('天氣',query)!=None):
            regex = re.compile(getSite())
            query = regex.search(query)
            reply=getWeather(query.group(1),2)
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
        elif(re.search('油價',query)!=None):
            reply = getOilPrice()
    
        elif(re.search('黃金',query)!=None):
            reply = getGolden()
        elif(re.search('(美金|日圓|日元|人民幣|英鎊|歐元)',query)!=None):
            regex = re.compile('(美金|日圓|日元|人民幣|英鎊|歐元)')
            query = regex.search(query)
            reply = getCurrency(query.group(1))
            
        else:
            if wiki_search(query)!=None:
                reply = wiki_search(query)
            else:
                query = query.upper()
                response = runAIML(query)
                if response != '':
                    reply = response
                else:
                    raise Exception
            
            
        
    except Exception as e:
        print(e)
        pass
    return jsonify(result=reply)
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
    
    elif(re.search('民法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_Civil(query.group())
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('刑法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_criminal(query.group())
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('憲法',query)!=None):
            try:
                regex = re.compile('\d+')
                query = regex.search(query)
                reply=get_constitution(query.group())
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            except Exception as e:
                reply = ('請輸入阿拉伯數字法律編號')
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
    elif(re.search('性侵',query)!=None):
        reply = TemplateSendMessage(
            alt_text='性侵害相關條文',
            template=ButtonsTemplate(
                title='常見觸犯條文',
                text='點擊查看詳細條文內容',
                thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                actions=[
                    MessageTemplateAction(
                        label='刑法:第 227 條',
                        text='刑法:第 227 條 （未成年人性侵害）'
                    ),
                    MessageTemplateAction(
                        label='刑法:第 228 條',
                        text='刑法:第 228 條 （利用權勢性交或猥褻罪）'
                    ),
                    MessageTemplateAction(
                        label='刑法:第 332 條',
                        text='刑法:第 332 條 （強盜結合強制性交罪）'
                    ),
                    MessageTemplateAction(
                        label='刑法:第 348 條',
                        text='刑法:第 348 條 （擄人勒贖結合強制性交罪）'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, reply)
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
            if wiki_search(query)!=None:
                reply = wiki_search(query)
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply))
         
          
if __name__ == "__main__":
    application.run(
        port=5555)
