# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:18:33 2018

@author: XuTingDeng
"""

import jieba
import re
import logging

question_text = open('stc_weibo_train_post_zh.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
answer_text = open('stc_weibo_train_response_zh.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
cut_question_text = open('stc_quesion_cut','w',encoding = 'utf-8')
cut_answer_text = open('stc_answer_cut','w',encoding = 'utf-8')


def clean_text(text):
    rule = re.compile("[^\u4e00-\u9fa5]")
    text = rule.sub('',text)
    return text
clean_q = []
for question in question_text:
    clean_q.append(clean_text(question))
 
# Cleaning the answers
clean_a = []
for answer in answer_text:
    clean_a.append(clean_text(answer))
 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
jieba.set_dictionary('jieba_dict/dict.txt.big')
stopword_set = set()
with open('jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))

for texts_num, line in enumerate(clean_q):
    
    words = jieba.cut(line, cut_all=False)
    for word in words:
        if word not in stopword_set:
            cut_question_text.write(word + ' ')
    cut_question_text.write('\n') 
    if (texts_num + 1) % 10000 == 0:
        logging.info("已完成前問句 %d 行的斷詞" % (texts_num + 1))
      
        
for texts_num, line in enumerate(clean_a):
    
    words = jieba.cut(line, cut_all=False)
    for word in words:
        if word not in stopword_set:
            cut_answer_text.write(word + ' ')
    cut_answer_text.write('\n')            
    if (texts_num + 1) % 10000 == 0:
        logging.info("已完成前答句 %d 行的斷詞" % (texts_num + 1))
cut_question_text.close()
cut_answer_text.close()