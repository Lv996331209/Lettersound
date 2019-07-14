import pandas as pd
import json
import os

filelist=[]
for name in os.listdir('词表/全部'):
     filelist.append(name)
#print(filelist)
for j in filelist:
    try:
        with open('词表/全部/'+j,'r') as load_f:
            load_dict = json.load(load_f)
        #print(j[:-5])
        #list_r=[]
        #list_f=[]
        print((load_dict))
        # sum=0
        #for i in load_dict:
             #list_r.append(i)
             #list_f.append(load_dict[i])
             #print(i,load_dict[i])
             #sum=sum+load_dict[i]
        #print(len(list_r))
        #print(sum)
        #
        #data={'f':list_f}
        #frame1 = pd.DataFrame(data)
        #print(frame1)
        #frame1.to_csv(j[:-5]+'.csv')

    except:
        print(j+'xxx')
# list_r=[]
# list_f=[]
# #print((load_dict))
# sum=0
# for i in load_dict:
#     list_r.append(i)
#     list_f.append(load_dict[i])
#     #print(i,load_dict[i])
#     sum=sum+load_dict[i]
# print(len(list_r))
# print(sum)

#data={'R':list_r,'F':list_f}
#frame1 = pd.DataFrame(data)
#print(frame1)
#frame1.to_csv('alpha.csv')
