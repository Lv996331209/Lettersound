import json
import os

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def getWord(word):
    if '(' in word:
        i = word.index('(')
        return word[:i]
    return word

def filterByNextLetter(words,nl):
    if nl is None:
        return words
    filterWords = []
    for word in words:
        if len(word[1][0]) - 1 == word[3]:
            if nl == '$':
                filterWords.append(word)
        else:
            if nl == word[1][0][word[3] + 1][0]:
                filterWords.append(word)
    return filterWords

def filterByNextSound(words,ns):
    if ns is None:
        return words
    filterWords = []
    for word in words:
        if len(word[1][0]) - 1 == word[3]:
            if ns == '$':
                filterWords.append(word)
        else:
            i = word[3] + 1
            sound = word[1][0][i][1]
            if len(sound)>0 and sound[-1].isdigit():
                sound=sound[:-1]
            while len(sound)==0 and i<len(word[1][0])-1:
                i = i+1
                sound = word[1][0][i][1]
                if len(sound) > 0 and sound[-1].isdigit():
                    sound = sound[:-1]
            if ns == sound:
                filterWords.append(word)
    return filterWords

def filterByPreLetter(words,pl):
    if pl is None:
        return words
    filterWords = []
    for word in words:
        if 0 == word[2]:
            if pl == '^':
                filterWords.append(word)
        else:
            if pl == word[1][0][word[2] - 1][0]:
                filterWords.append(word)
    return filterWords

def filterByPreSound(words,ps):
    if ps is None:
        return words
    filterWords = []
    for word in words:
        if 0 == word[2]:
            if ps == '^':
                filterWords.append(word)
        else:
            i = word[2] - 1
            sound = word[1][0][i][1]
            if len(sound) > 0 and sound[-1].isdigit():
                sound = sound[:-1]
            while len(sound)==0 and i>0:
                i = i-1
                sound = word[1][0][i][1]
                if len(sound) > 0 and sound[-1].isdigit():
                    sound = sound[:-1]
            if ps == sound:
                filterWords.append(word)

    return filterWords


def getOriginWords():
    with open('../static/json/library/originAll.json', 'r') as f:
        words = json.load(f)
    return words
def addStess2Sound(stress,sound):
    sounds = sound.split('-')
    for i,s in enumerate(sounds):
        if stress[i]=='1':
            sounds[i] = 'ˈ'+sounds[i]
        elif stress[i] == '2':
            sounds[i] = 'ˌ'+sounds[i]
    return '-'.join(sounds)


def transform(words):
    with open(root_dir()+'/../static/json/library/wordPlus.json', 'r') as f:
        syllables = json.load(f)
    lst = []
    for word,detail,start,end in words:
        word = getWord(word)
        syllable0 = syllables[word]["syllable"]
        syllable1 = ""
        pron = ""
        stress = ""
        tag = ','.join(detail[1])
        indexS = 0
        for i,(letter,sound) in enumerate(detail[0]):
            if indexS >= len(syllable0):
                print('error')
            if syllable0[indexS]=='-':
                indexS += 1
                syllable1+='-'
                pron += '-'
            if i==start:
                syllable1 += '{'
                pron += '{'
            if '_' in letter:
                letter = letter[0]
            syllable1 += letter
            if len(sound)>0 and sound[-1].isdigit():
                stress += sound[-1]
                sound = sound[:-1]
            pron += sound
            if i==end:
                syllable1 += '}'
                pron += '}'
            indexS += len(letter)
        pron = addStess2Sound(stress,pron)
        lst.append({"word":word,"syllable":syllable1,"pron":pron,"stress":stress,"tag":tag})
    return lst

def makePlus():
    lst = getOriginWords()
    words = {}
    for word,syllable,_,_ in lst:
        words[getWord(word)]={"syllable":syllable}
    print(len(words))
    with open('../static/json/library/wordPlus.json', 'w') as f:
        json.dump(words, f)
if __name__=="__main__":
    makePlus()
