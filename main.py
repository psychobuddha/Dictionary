import json
from difflib import get_close_matches
data = json.load(open('/home/ninja/Desktop/DictionaryProject/Dictionary/data.json'))

phrase = input('Enter word: ')

def translate(word):
    word = word.lower()
    diff_catcher = get_close_matches(phrase, data.keys())

    if word in data:
        return data[word]
    elif len(diff_catcher) > 0:
        ys = input(f'Did you mean "{diff_catcher[0]} instead"? Enter Y/N\n')
        if ys == 'Y':
            return data[diff_catcher[0]]
        else:
            return f'{phrase} not in dictionary'
    else:   
        return 'Word not in dictionary'


output = translate(phrase)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)