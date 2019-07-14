import pandas as pd
import json


with open('FinalResult2.json','r') as load_f:
    load_dict = json.load(load_f)
with open('FinalWordList2.json','r') as load_f:
    load_list = json.load(load_f)
print(len(load_dict))
sum=0
try:
    for word in load_list:
        #print(word)
        tag_list=load_list[word]
        #print(tag_list)
        new_dict={}
        new_list=[]
        for son_word in tag_list:
            dict=load_dict[son_word][0]
            #print(dict)
            new_list.append(dict)
            #print(dict['phonetic'])
        #print(new_list)
        chang_new = []
        for i in range(len(new_list)):
            for j in range(i+1,len(new_list)):
                if new_list[i]['phonetic']==new_list[j]['phonetic'] or new_list[j]['phonetic']==None:
                    new_list[i]['tag']=new_list[i]['tag']+new_list[j]['tag']
        print(new_list[i])
        for i in range(len(new_list)):
            #print(new_list[i])
            if new_list[i]['phonetic'] not in chang_new:
                chang_new.append(new_list[i]['phonetic'])
            else:
                #new_list.pop(i)
                print()

        #print(chang_new)
        print(word,new_list)
        #break
        sum=sum+1
        if sum==18953:
            break

except:
      print()