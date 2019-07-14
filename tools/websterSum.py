import pprint
import json
import re
from filterdata import getWord,root_dir
import pandas as pd


def getProns():
    with open(root_dir()+'/../pronLib.json', 'r') as f:
        dictionary = json.load(f)
    return dictionary

def getDetail(word):
    dict1 = getProns()
    if word not in dict1.keys():
        print("we can't find the word ",word)
        return None
    return dict1[word]

def getPronList():
    dict1 = getProns()
    # print(len(dict1))
    pronDict = {}
    for word,val in dict1.items():
        for item in val:
            for alpha,pron in item[0]:
                if pron!='' and pron[-1].isdigit():
                    pron = pron[:-1]
                # if alpha=='eau' and 'ː' in pron:
                #     print(word,item)
                if alpha not in pronDict.keys():
                    pronDict[alpha] = [pron]
                else:
                    if pron not in pronDict[alpha]:
                        pronDict[alpha].append(pron)
    return pronDict

def listWords1(aPron):
    dict1 = getProns()
    lst = []
    for word, val in dict1.items():
        for item in val:
            for alpha, pron in item[0]:
                if pron!='' and pron[-1].isdigit():
                    pron = pron[:-1]
                if aPron==pron:
                    lst.append(word)
    return lst
def listWords2(aAlpha,aPron):
    dict1 = getProns()
    lst = []
    for word, val in dict1.items():
        for item in val:

            for i,(alpha, pron) in enumerate(item[0]):
                if pron!='' and pron[-1].isdigit():
                    pron = pron[:-1]
                if alpha==aAlpha and aPron==pron:
                    lst.append([word,item,i,i])
    return lst

def listCom2(com,aPron):
    '''

    :param com:
    :param aPron: None means all words contained substring 'com'
    :return:
    '''
    dict1 = getProns()
    lst = []
    for word, val in dict1.items():
        # if word=='metallurgy':
        #     print(word)
        if com not in word:
            continue
        index = word.index(com)
        for item in val:
            start = 0
            bCom = ''
            bPron = ''
            for i,(alpha, pron) in enumerate(item[0]):
                if start<index:
                    if '_' in alpha:
                        start += 1
                    else:
                        start += len(alpha)
                    continue
                elif start>index:
                    break
                if len(bCom)<len(com):
                    if bCom=='':
                        i0=i
                    if '_' in alpha:
                        bCom += alpha[0]
                    else:
                        bCom += alpha
                    bPron += pron
                    if bCom==com:
                        i1=i
                        cPron = re.sub('\d', '', bPron)
                        if aPron is None:
                            lst.append([word,item,i0,i1])
                        elif cPron == aPron:
                            lst.append([word,item,i0,i1])
                        break
                    else:
                        continue
                else:
                    break
    return lst
def sumCom2(com,aPron):
    '''

    :param com:
    :param aPron: None means all words contained substring 'com'
    :return:
    '''
    dict1 = getProns()
    lst = {}
    for word, val in dict1.items():
        # if word=='metallurgy':
        #     print(word)
        if com not in word:
            continue
        index = word.index(com)
        for item in val:
            start = 0
            bCom = ''
            bPron = ''
            for alpha, pron in item[0]:
                if start<index:
                    if '_' in alpha:
                        start += 1
                    else:
                        start += len(alpha)
                    continue
                elif start>index:
                    break
                if len(bCom)<len(com):
                    if '_' in alpha:
                        bCom += alpha[0]
                    else:
                        bCom += alpha
                    bPron += pron
                    if bCom==com:
                        cPron = re.sub('\d', '', bPron)
                        if bCom == com :
                            if aPron is None:
                                if cPron in lst.keys():
                                    lst[cPron] += 1
                                else:
                                    lst[cPron] = 1
                            elif cPron == aPron:
                                if cPron in lst.keys():
                                    lst[cPron] += 1
                                else:
                                    lst[cPron] = 1
                        break
                    else:
                        continue
                else:
                    break
    return lst
def pre(com, aPron,words):
    # dict1 = getProns()
    letterDict = {}
    soundDict = {}
    for word, val,_,_ in words:
        # if word=='metallurgy':
        #     print(word)
        if com not in word:
            continue
        index = word.index(com)
        start = 0
        startindex=0
        bCom = ''
        bPron = ''
        for i,(alpha, pron) in enumerate(val[0]):
            if start<index:
                if '_' in alpha:
                    start += 1
                else:
                    start += len(alpha)
                startindex+=1
                continue
            elif start>index:
                break
            if len(bCom)<len(com):
                if '_' in alpha:
                    bCom += alpha[0]
                else:
                    bCom += alpha
                bPron += pron
                if bCom==com:
                    cPron = re.sub('\d', '', bPron)
                    if bCom == com and cPron == aPron:
                        if startindex==0:#this is the first sound
                            if '^' in soundDict.keys():
                                soundDict['^'] += 1
                            else:
                                soundDict['^'] = 1
                            if '^' in letterDict.keys():
                                letterDict['^'] += 1
                            else:
                                letterDict['^'] = 1
                        else:
                            preLetter = val[0][startindex-1][0]
                            if preLetter in letterDict.keys():
                                letterDict[preLetter] += 1
                            else:
                                letterDict[preLetter] = 1
                            while startindex>0:
                                presound = re.sub('\d','',val[0][startindex-1][1])
                                if presound == '':
                                    startindex-=1
                                    continue
                                if presound in soundDict.keys():
                                    soundDict[presound] += 1
                                else:
                                    soundDict[presound] = 1
                                break
                    break
                else:
                    continue
            else:
                break
    return letterDict, soundDict
def next(com,aPron,words):
    letterDict = {}
    soundDict = {}
    for word, val,_,_ in words:
        # if word=='metallurgy':
        #     print(word)
        if com not in word:
            continue
        index = word.index(com)
        start = 0
        bCom = ''
        bPron = ''
        for i,(alpha, pron) in enumerate(val[0]):
            if start<index:
                if '_' in alpha:
                    start += 1
                else:
                    start += len(alpha)
                continue
            elif start>index:
                break
            if len(bCom)<len(com):
                if '_' in alpha:
                    bCom += alpha[0]
                else:
                    bCom += alpha
                bPron += pron
                if bCom==com:
                    cPron = re.sub('\d', '', bPron)
                    if bCom == com and cPron == aPron:
                        if i==len(val[0])-1:#this is the first sound
                            if '$' in soundDict.keys():
                                soundDict['$'] += 1
                            else:
                                soundDict['$'] = 1
                            if '$' in letterDict.keys():
                                letterDict['$'] += 1
                            else:
                                letterDict['$'] = 1
                        else:
                            preLetter = val[0][i+1][0]
                            if preLetter in letterDict.keys():
                                letterDict[preLetter] += 1
                            else:
                                letterDict[preLetter] = 1
                            while i<len(val[0])-1:
                                presound = re.sub('\d','',val[0][i+1][1])
                                if presound == '':
                                    i+=1
                                    continue
                                if presound in soundDict.keys():
                                    soundDict[presound] += 1
                                else:
                                    soundDict[presound] = 1
                                break
                            if i==len(val[0])-1:
                                if '$' in soundDict.keys():
                                    soundDict['$'] += 1
                                else:
                                    soundDict['$'] = 1
                    break
                else:
                    continue
            else:
                break
    return letterDict, soundDict
def alphaPronSum(dictname=None):
    if dictname is not None:
        with open('../static/json/library/'+dictname+'_summary.json', 'r') as f:
            dictionary = json.load(f)
            print('length of '+dictname+'is :',len(set(dictionary)))
    dict1 = getProns()
    print('length of all is :', len(dict1))
    pronDict = {}
    for word, val in dict1.items():
        if dictname is not None and word not in dictionary:
            continue
        for item in val:
            for alpha, pron in item[0]:
                if pron!='' and pron[-1].isdigit():
                    pron = pron[:-1]
                key = alpha+'#'+pron
                if key not in pronDict.keys():
                    pronDict[key] = 1
                else:
                    pronDict[key] += 1
    return pronDict

def vowelPronSum(dictname=None):
    if dictname is not None:
        with open('../static/json/library/'+dictname+'_summary.json', 'r') as f:
            dictionary = json.load(f)
            print('length of '+dictname+'is :',len(set(dictionary)))
    dict1 = getProns()
    pronDict = {}
    #vowels = set('aeiouæɑəɚɛɪʊʌ')
    vowels = set('aeiouæɑəɚɛɪʊʌɔ')
    V=set('aeiouy')
    for word, val in dict1.items():
        if dictname is not None and word not in dictionary:
            continue
        for item in val:
            for alpha, pron in item[0]:
                if len(set(alpha)&V)>0:
                    if pron != '' and pron[-1].isdigit():
                        pron = pron[:-1]
                    if pron=='' or len(set(pron)&vowels)>0:
                        key = alpha+'#'+pron
                        if key not in pronDict.keys():
                            pronDict[key] = 1
                        else:
                            pronDict[key] += 1
    del pronDict['y#']
    return pronDict
def getNoStress(lst):
    result = []
    for item in lst:
        if len(item[1])>0 and item[1][-1].isdigit():
            result.append([item[0],item[1][:-1]])
        else:
            result.append(item)
    return result
def revise():
    dict1 = getProns()
    dict1['mulch']=[[[['m', 'm'], ['u', 'ʌ1'], ['l', 'l'], ['ch', 'tʃ']], ['noun']], [[['m', 'm'], ['u', 'ʌ1'], ['l', 'l'], ['ch', 'tʃ']], ['verb']]]
    dict1['legislation']=[[[['l', 'l'], ['e', 'ɛ2'], ['g', 'ʤ'], ['i', 'ə0'], ['s', 's'], ['l', 'l'], ['a', 'eɪ1'], ['t', 'ʃ'], ['io', 'ə0'], ['n', 'n']], ['noun']]]
    dict1['goggle']=[[[['g', 'g'], ['o', 'ɑː1'], ['g', 'g'], ['g', ''], ['l', 'əl0'], ['e', '']], ['verb']]]
    dict1['crawl']=[[[['c', 'k'], ['r', 'r'], ['aw', 'ɑː1'], ['l', 'l']], ['verb']], [[['c', 'k'], ['r', 'r'], ['aw', 'ɑː1'], ['l', 'l']], ['noun']]]
    dict1['devil']=[[[['d', 'd'], ['e', 'ɛ1'], ['v', 'v'], ['i', 'ə0'], ['l', 'l']], ['noun']]]
    dict1['artificial']=[[[['ar', 'ɑɚ2'], ['t', 't'], ['i', 'ə0'], ['f', 'f'], ['i', 'ɪ1'], ['ci', 'ʃ'], ['a', 'ə0'], ['l', 'l']], ['adjective']]]
    dict1['chuckle']=[[[['ch', 'tʃ'], ['u', 'ʌ1'], ['ck', 'k'], ['l', 'əl0'], ['e', '0']], ['verb']]]
    dict1['chisel']=[[[['ch', 'tʃ'], ['i', 'ɪ1'], ['s', 'z'], ['e', 'ə0'], ['l', 'l']], ['noun', 'verb']]]
    dict1['chicken']=[[[['ch', 'tʃ'], ['i', 'ɪ1'], ['ck', 'k'], ['e', 'ə0'], ['n', 'n']], ['noun']]]
    dict1['governor']=[[[['g', 'g'], ['o', 'ʌ1'], ['v', 'v'], ['er', 'ə0'], ['n', 'n'], ['or', 'ɚ0']], ['noun']]]
    dict1['fission']=[[[['f', 'f'], ['i', 'ɪ1'], ['s', 'ʃ'], ['s', ''], ['io', 'ə0'], ['n', 'n']], ['noun']]]
    dict1['abolition']=[[[['a', 'æ2'], ['b', 'b'], ['o', 'ə0'], ['l', 'l'], ['i', 'ɪ1'], ['t', 'ʃ'], ['io', 'ə0'], ['n', 'n']], ['noun']]]
    ####################################################################
    dict1['guarantee']=[[[['g', 'g'], ['u', ''], ['a', 'e2'], ['r', 'r'], ['a', 'ə0'], ['n', 'n'], ['t', 't'], ['ee', 'iː1']], ['noun']]]
    dict1['guarantor']=[[[['g', 'g'], ['u', ''], ['a', 'e2'], ['r', 'r'], ['a', 'ə0'], ['n', 'n'], ['t', 't'], ['or', 'oɚ1']], ['noun']]]
    dict1['vengeance']=[[[['v', 'v'], ['e', 'ɛ1'], ['n', 'n'], ['g', 'ʤ'], ['e', ''], ['a', 'ə0'], ['n', 'n'], ['c', 's'], ['e', '']], ['noun']]]
    dict1['knowledgeable']=[[[['kn', 'n'], ['ow', 'ɑː1'], ['l', 'l'], ['e', 'ɪ0'], ['dg', 'ʤ'], ['e', ''], ['a', 'ə0'], ['b', 'b'], ['l', 'əl0'], [ 'e', '']], ['adjective']]]
    dict1['isle'] =[[[['i', 'ajə1'], ['s', ''], ['l', 'l'], ['e', '']], ['noun']]]
    dict1['whereabouts'] =[[[['wh', 'w'], ['e', 'e1'], ['r', 'r'], ['e', ''], ['a', 'ə0'], ['b', 'b'], ['ou', 'aʊ2'], ['t', 't'], ['s', 's']], ['adverb', 'noun']]]
    dict1['whereupon'] = [[[['wh', 'w'], ['e', 'e1'], ['r', 'r'], ['e', ''], ['u', 'ə0'], ['p', 'p'], ['o', 'ɑː2'], ['n', 'n']], ['conjunction']]]
    dict1['February'] =[[[['f', 'f'], ['e', 'ɛ1'], ['b', 'b'], ['r', ''], ['u', 'jəw0'], ['a', 'e2'], ['r', 'r'], ['y', 'i0']], ['noun']]]
    dict1['paranoia'] =[[[['p', 'p'], ['a', 'e2'], ['r', 'r'], ['a', 'ə0'], ['n', 'n'], ['oi', 'oj1'], ['a', 'ə0']], ['noun']]]
    for word, val in dict1.items():
        for item in val:
            nostress = getNoStress(item[0])
            if ['ct','kt'] in item[0]:
                index  = item[0].index(['ct','kt'])
                del item[0][index]
                item[0].insert(index,['c','k'])
                item[0].insert(index+1,['t','t'])
                print(word,item[0],index)
            if ['ct','t'] in item[0]:
                index  = item[0].index(['ct','t'])
                del item[0][index]
                item[0].insert(index,['c',''])
                item[0].insert(index+1,['t','t'])
                print(word,item[0],index)
            if ['mn','m'] in item[0]:
                index  = item[0].index(['mn','m'])
                del item[0][index]
                item[0].insert(index,['m','m'])
                item[0].insert(index+1,['n',''])
                print(word,item[0],index)
            if ['sch', 's'] in item[0]:
                index = item[0].index(['sch', 's'])
                del item[0][index]
                item[0].insert(index, ['s', 's'])
                item[0].insert(index + 1, ['ch', ''])
                print(word, item[0], index)
            if ['sch', 'sk'] in item[0]:
                index = item[0].index(['sch', 'sk'])
                del item[0][index]
                item[0].insert(index, ['s', 's'])
                item[0].insert(index + 1, ['ch', 'k'])
                print(word, item[0], index)
            if ['sc', 'sk'] in item[0]:
                index = item[0].index(['sc', 'sk'])
                del item[0][index]
                item[0].insert(index, ['s', 's'])
                item[0].insert(index + 1, ['c', 'k'])
                print(word, item[0], index)
            if ['sw', 'sw'] in item[0]:
                index = item[0].index(['sw', 'sw'])
                del item[0][index]
                item[0].insert(index, ['s', 's'])
                item[0].insert(index + 1, ['w', 'w'])
                print(word, item[0], index)
            if ['sw', 's'] in item[0]:
                index = item[0].index(['sw', 's'])
                del item[0][index]
                item[0].insert(index, ['s', 's'])
                item[0].insert(index + 1, ['w', ''])
                print(word, item[0], index)
            # if ['gu', 'gw'] in item[0]:
            #     index = item[0].index(['gu', 'gw'])
            #     del item[0][index]
            #     item[0].insert(index, ['g', 'g'])
            #     item[0].insert(index + 1, ['u', 'w'])
            #     print(word, item[0], index)
            # if ['gu', 'g'] in item[0]:
            #     index = item[0].index(['gu', 'g'])
            #     del item[0][index]
            #     item[0].insert(index, ['g', 'g'])
            #     item[0].insert(index + 1, ['u', ''])
            #     print(word, item[0], index)
            # if ['ti', 'ʃi'] in item[0]:
            #     index = item[0].index(['ti', 'ʃi'])
            #     del item[0][index]
            #     item[0].insert(index, ['t', 'ʃ'])
            #     item[0].insert(index + 1, ['i', 'i'])
            #     print(word, item[0], index)
            # if ['ci', 'ʃi'] in item[0]:
            #     index = item[0].index(['ci', 'ʃi'])
            #     del item[0][index]
            #     item[0].insert(index, ['c', 'ʃ'])
            #     item[0].insert(index + 1, ['i', 'i'])
            #     print(word, item[0], index)
            if ['tw', 'tw'] in item[0]:
                index = item[0].index(['tw', 'tw'])
                del item[0][index]
                item[0].insert(index, ['t', 't'])
                item[0].insert(index + 1, ['w', 'w'])
                print(word, item[0], index)
            if ['tw', 't'] in item[0]:
                index = item[0].index(['tw', 't'])
                del item[0][index]
                item[0].insert(index, ['t', 't'])
                item[0].insert(index + 1, ['w', ''])
                print(word, item[0], index)
            if ['wr', 'r'] in item[0]:
                index = item[0].index(['wr', 'r'])
                del item[0][index]
                item[0].insert(index, ['w', ''])
                item[0].insert(index + 1, ['r', 'r'])
                print(word, item[0], index)
            if ['l','l̟'] in item[0]:
                index = item[0].index(['l','l̟'])
                if len(item[0][index-1][1])==0 or not item[0][index-1][1][-1].isdigit():
                    item[0][index][1] += '0'
                    print(word, item[0])
            if item[0][-1][1]=='0':
                item[0][-1][1] = ''
                if item[0][-2][1]=='0':
                    item[0][-2][1] = ''
                    print(word, item[0])
            if word[-2:]=='ed' and item[0][-2]==['e','0']:
                item[0][-2] = ['e', '']
                print(word, item[0])
            if word[-2:]=='es' and item[0][-2]==['e','0']:
                item[0][-2] = ['e', '']
                print(word, item[0])
            if len(nostress)>1 and ['u', ''] in nostress :
                index = nostress.index(['u', ''])
                stress = item[0][index][1]
                if stress.isdigit():
                    i = 1
                    next = item[0][index+i][1]
                    # if len(next)==0:
                    #     item[0][index + 1][1] += stress
                    # else:
                    while not next[-1].isdigit():
                        i+=1
                        next = item[0][index+i][1]

                    item[0][index+i][1] = next[:-1]+stress
                    item[0][index][1] = ''
                    print(word, item[0])
            if ['l','l̟'] in item[0]:
                index = item[0].index(['l','l̟'])
                if len(item[0][index-1][1])==0 or not item[0][index-1][1][-1].isdigit():
                    item[0][index][1] += '0'
                    print(word, item[0])
            if ['i','aj'] in nostress:
                index = nostress.index(['i','aj'])
                if nostress[index+1]==['l','əl']:
                    item[0][index][1] = item[0][index][1][:-1]+'ə'+item[0][index][1][-1]
                    item[0][index+1][1]='l'
                    print(word, item[0])
            # if ['e','ə'] in nostress:
            #     index = nostress.index(['e', 'ə'])
            #     if index<len(nostress)-1 and nostress[index + 1][1] == '' and nostress[index + 1][0][0] in 'aeioyu':
            #         print(word, item[0])
            if ['e','1'] in item[0]:
                index = item[0].index(['e','1'])
                item[0][index][1] = ''
                for i,(letter,sound) in enumerate(item[0][index+1:]):
                    if len(sound)==0:
                        continue
                    if sound[-1].isdigit():
                        item[0][index+i+1][1] = sound[:-1]+'1'
                        print(word, item[0])
                        break
            if ['e','2'] in item[0]:
                index = item[0].index(['e','2'])
                item[0][index][1] = ''
                for i,(letter,sound) in enumerate(item[0][index+1:]):
                    if len(sound)==0:
                        continue
                    if sound[-1].isdigit():
                        item[0][index+i+1][1] = sound[:-1]+'2'
                        print(word, item[0])
                        break

    with open('../static/json/library/pronLib.json', 'w') as f:
        json.dump(dict1, f)
def doubleVowelCheck():
    dict1 = getProns()
    for word, val in dict1.items():
        for item in val:
            for i, (letter, sound) in enumerate(item[0]):
                if i < len(item[0]) - 1:
                    if sound == '0':
                        # if item[0][i+1][-1].isdigit():
                        if len(item[0][i + 1][1]) > 0 and item[0][i + 1][1][-1].isdigit():
                            print(word, item[0])
                if i > 0:
                    if sound == '0':
                        if len(item[0][i - 1][1]) > 0 and item[0][i - 1][1][-1].isdigit():
                            print(word, item[0])

def syllablesCheck():
    dict1 = getProns()
    with open('../static/json/library/originAll.json', 'r') as f:
        dict0 = json.load(f)
    for item in dict0:
        word = getWord(item[0])
        val = dict1[word]
        num0 = len(item[1].split('-'))
        for pair in val:
            # print(word)
            num1 = len([a for a in pair[0] if len(a[1])>0 and a[1][-1].isdigit()])
            if num0<num1:#adjust silient 'e'
                if ['e','0'] in pair[0]:
                    index = pair[0].index(['e','0'])
                    pair[0][index] = ['e','']
                    print(word,dict1[word])
            if num0<num1:#adjust silient 'e'
                if ['i','0'] in pair[0]:
                    index = pair[0].index(['i','0'])
                    pair[0][index] = ['i','']
                    print(word,dict1[word])
            if num0!=num1:
                print(word,num0,num1,pair[1])
    with open('../static/json/library/pronLib.json', 'w') as f:
        json.dump(dict1, f)
if __name__=="__main__":
    name=None
    lst1 = vowelPronSum(name)
    print('元音'+str(len(lst1)))
    lst2 = alphaPronSum(name)
    print('全部'+str(len(lst2)))
    #pprint.pprint(lst1)
    with open('./vowel.json','w') as f:
        json.dump(lst1,f)
    with open('vowel.json','w') as f:
        json.dump(lst2,f)
    #tag=[]
    #for i in lst:
      #print(lst[i])
      #tag.append(lst[i])
    #data = pd.DataFrame(columns=['R'],data=tag)
    #print(data)
    #data.to_csv('../data2/'+'all'+'.csv')

