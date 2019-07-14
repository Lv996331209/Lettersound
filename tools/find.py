import json

with open('301.json','r') as f:
    dic= json.load(f)
sum=0
tag=0
for i in dic:
    if 'ə' in i:
     print(i)
     print(dic[i])
     tag=tag+1
    sum=sum+dic[i]
     #print()
#print(dic)

print('元音匹配对数目'+str(sum))
print('含有ə的匹配对数目'+str(tag))