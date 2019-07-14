import json
with open('../static/json/library/' + 'Colins' + '_summary.json', 'r') as f:
    dictionary = json.load(f)
    print(dictionary)
    print(len(set(dictionary)))