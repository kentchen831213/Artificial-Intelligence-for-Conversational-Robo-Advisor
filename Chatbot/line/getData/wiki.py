import requests
import re

def wiki_search(query):
    try:
        r = requests.get('https://zh.wikipedia.org/w/api.php?action=opensearch&search='+query+'&utf8')
        r = r.text
        r = r.split('[')[3]
        r = r.split('。')[0]
        r = r.split('）',1)[1]
        r = re.sub('["，]',"",r,count=1)
        return r
    except Exception as e:
        return None

   
   