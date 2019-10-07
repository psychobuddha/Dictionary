import json
from difflib import get_close_matches
data = json.load(open('data.json'))

compare = get_close_matches(phrase, data.keys()

def translate(word):
    

    if word in data:
        return data[word]
    elif len(get_close_matches(phrase, data.keys())) > 0:
        ys = input(f'Did you mean "{get_close_matches(phrase, data.keys())[0]} instead"? Enter Y/N\n')
        if ys == 'Y' or ys == 'yes':
            return data[get_close_matches(phrase, data.keys())[0]]
        return 'Word not in dictionary'
    else:   
        return 'Word not in dictionary'

phrase = input('Enter word: ').lower()

print(translate(phrase))