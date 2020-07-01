import random
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from mybot.messenger_api import *
from mybot.fb_setting import *
from getData.weather import getWeather
from getData.runAIML import runAIML
from getData.data import getSite,getStock,getStocNum
import re
from getData.stock2 import getfixstock
from getData.oilPrice import getOilPrice
from getData.golden import getGolden
from getData.Currency import getCurrency
def post_facebook_message(fbid, recevied_message):
    # user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    # user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    # user_details = requests.get(user_details_url, user_details_params).json()

    fb = FbMessageApi(fbid)
    query=recevied_message
    if (re.search('天氣', query) != None):
        regex = re.compile('(台北|新北|台中|高雄|台南|桃園|基隆|新竹|雲林|南投|嘉義|苗栗|彰化|花蓮|台東|澎湖|宜蘭)')
        query = regex.search(query)
        content = getWeather(query.group(1), 2)
        fb.text_message(content)
    elif (re.search(getStock(), query) != None):
        stock = getStocNum()
        regex = re.compile(getStock())
        stockname = regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)', query) != None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select = {'市': 1, '買': 2, '賣': 3, '成交': 4, '收': 5, '開': 6, '高': 7, '低': 8}
            stockCode = regex.search(query)
            content= getfixstock(stock[stockname.group(0)], select[stockCode.group(0)])
        else:
             content = getfixstock(stock[stockname.group(0)], 0)
        fb.text_message(content)
    elif (re.search('\d', query) != None):
        regex = re.compile('\d+')
        stocknum = regex.search(query)
        if (re.search('(市|買|賣|成交|收|開|高|低)', query) != None):
            regex = re.compile('(市|買|賣|成交|收|開|高|低)')
            select = {'市': 1, '買': 2, '賣': 3, '成交': 4, '收': 5, '開': 6, '高': 7, '低': 8}
            stockCode = regex.search(query)
            content = getfixstock(stocknum.group(), select[stockCode.group(0)])
        else:
            content= getfixstock(stocknum.group(), 0)
        fb.text_message(content)
    elif (re.search('天氣', query) != None):
        regex = re.compile('(台北|新北|台中|高雄|台南|桃園|基隆|新竹|雲林|南投|嘉義|苗栗|彰化|花蓮|台東|澎湖|宜蘭)')
        query = regex.search(query)
        content = getWeather(query.group(1), 2)
        fb.text_message(content)
    elif '油價' in query:
        content = getOilPrice()
        fb.text_message(content)
    elif '黃金價' in query:
        content = getGolden()
        fb.text_message(content)
    elif '匯率' in query:
        query=re.split('匯率',query)
        c=query[0]
        content = getCurrency(c)
        fb.text_message(content)
    else:
        response = runAIML(recevied_message)
        if response != "":
            content = response
        else:
            content = "我不知道你在說什麼"
        fb.text_message(content)
        return  0

class MyBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    # pprint(message)
                    print('message')
                    try:
                        post_facebook_message(message['sender']['id'], message['message']['text'])
                    except:
                        return HttpResponse()
                if 'postback' in message:
                    # pprint(message)
                    print('postback')
                    try:
                        post_facebook_message(message['sender']['id'], message['postback']['payload'])
                    except:
                        return HttpResponse()

        return HttpResponse()
