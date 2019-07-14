import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


def getMedia(word,aTag=None):
    url = "http://www.learnersdictionary.com/definition/" + word
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    def generateUrl(element):
        head = 'http://media.merriam-webster.com/audio/prons/en/us/mp3/'
        temp1 = element.get('data-dir')
        temp2 = element.get('data-file')
        finalUrl = head + temp1 + '/' + temp2 + '.mp3'
        return finalUrl

    tempResults, tempTypes = [], []
    content = soup.find_all(attrs={'data-dir': True, 'data-file': True, 'data-word': word})
    if len(content) == 0:
        content = soup.find_all(attrs={'data-dir': True, 'data-file': True, 'data-word': 'or British'})
    for element in content:
        tempUrl = generateUrl(element)
        if tempUrl not in tempResults:
            tempResults.append(tempUrl)
    if len(tempResults)==0:
        return None
    elif len(tempResults)==1:
        return tempResults[0]
    types = soup.find_all(attrs={'class': 'fl'})
    for element in types:
        temptype = element.text
        temptype = re.sub("[^A-Za-z]","",temptype)
        if temptype not in tempTypes:
            tempTypes.append(temptype)
    print(tempTypes)
    results = list(zip(tempResults, tempTypes))
    for url,tag in results:
        if aTag==tag:
            return url
    return tempResults[0]


if __name__ == "__main__":
    urlList = getMedia('picture')
    print(urlList)
