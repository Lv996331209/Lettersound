# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:24:49 2018

@author: Qing0228
"""

import re
import pandas as pd

text=open('dictionaryLondman.txt','r',encoding='utf-8').read()
print(type(text))


#[\’\s]?[a-z·]+  y’all
#temp=re.findall(r'[1-9’A-Za-z·\'\-]+[1-9]?\s\/[\S]+[\s]?[\S]+\/',text)
#temp=re.findall(r'\s(.*?)\s\/(.*?)\/\s(.*?)\.',text)
temp=re.findall(r'\s([^\s]+)\s\/(.*?)\/[\s]+(.*?)\s',text)

print(len(temp))
print('temp---------')
for i in temp:

     print(i)

#print(temp)
words=[]
pron=[]
for i in temp:
    j=re.sub('[\t]+\/','\\/',i)
    k=re.sub(' \\/','\\/',j)
    r=k.split('\\')
    print(r)
    if len(r)==2:
        #word1=re.sub('[1-9]','',r[0])
        word=re.sub('\[\-','\[',r[0])
        if len(word)>=2 :
            words.append(word)
            pron.append(r[1])
#print(words)
#print(pron)
pron1=[]
for i in pron:
    a=re.sub('A','a',i)
    b=re.sub('S','ʃ',a)
    c=re.sub('O','ɔ',b)
    d=re.sub('Z','ʒ',c)
    e=re.sub('U','ʊ',d)
    f=re.sub('ø','ɚ',e)
    g=re.sub('I','ɪ',f)
    h=re.sub('E','ɛ',g)
    j=re.sub('§','',h)
    k=re.sub('D','ð',j)
    l=re.sub('T','θ',k)
    m=re.sub('"',"ˌ",l)
    n=re.sub('X','',m)
    o=re.sub("'",'ˈ',n)
    pron1.append(o)




dataframe=pd.DataFrame({'words':words[:-401],'pron':pron1[:-401]})
dataframe.to_csv('dictionaryLongman4.0.csv',index=True,sep=',',encoding='Utf-8')

# #
# new_word=list(dataframe['words'])
# # upper_list=[]
# # with open('upper_list.txt', 'w', encoding='utf-8') as f:
# #  for i in new_word:
# #     if i.isupper():
# #         print(i)
# #         upper_list.append(i)
# #         f.write(str(i)+'\n')
#
# # #print(dataframe)
# # tag_list=[]
# # tag_index=[]
# # index=0
# # for i in new_word:
# #     if '’' in i:
# #         tag_list.append(i)
# #         tag_index.append(index)
# #     index = index+1
# # print(len(tag_list))
# # print((tag_index))
# # #for i in range(len(tag_list)):
# # #    print(tag_index(i),tag_list(i))
# # #with open('tag_list.txt', 'w', encoding='utf-8') as f:
# # #    f.write(str(tag_list))
# # #print(new_word)
#
