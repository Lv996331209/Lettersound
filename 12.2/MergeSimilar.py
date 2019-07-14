import json

with open('FinalResult2.json', 'r', encoding='utf-8') as f:
    WordResult = json.load(f)

with open('FinalWordList2.json', 'r', encoding='utf-8') as f:
    WordList = json.load(f)

result = {}
words = WordList.keys()
for word in words:
    contents = WordList[word]
    tempResult = []
    breakstamp = 0
    for result_element in contents:
        try:
            tempResult.extend(WordResult[result_element])
        except Exception as e:
            print(e)
            breakstamp = 1
            break
    if breakstamp:
        continue
    saveIdent = []
    saveStamp = 0
    for index in range(len(tempResult)):
        if len(tempResult) != 1:
            if tempResult[index]['sound'] == tempResult[(index + 1) % (len(tempResult))]['sound'] or tempResult[index][
                'phonetic'] is None:
                for saveIdent_element in saveIdent:
                    if index - 1 in saveIdent_element:
                        saveIdent_element.append(index)
                        saveStamp = 1
                if saveStamp == 0:
                    saveIdent.append([index])
            else:
                saveIdent.append([index])
        else:
            saveIdent.append([index])
    mergeResult = []
    for saveident in saveIdent:
        newtags = []
        for index in saveident:
            for tag_element in tempResult[index]['tag']:
                if tag_element not in newtags:
                    newtags.append(tag_element)
        temp = {'tag': newtags, 'phonetic': tempResult[saveident[0]]['phonetic'],
                'sound': tempResult[saveident[0]]['sound'], 'syllable': tempResult[saveident[0]]['syllable']}
        mergeResult.append(temp)
    result[word] = mergeResult

with open('MergeResult.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
