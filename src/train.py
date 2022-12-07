import json
from utils import tokenize, stemming, bagOfWords

with open('./intents.json', 'r') as f:
    intents = json.load(f)

allWords = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intents['patterns']:
        w = tokenize(pattern)
        allWords.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',', ';']

print(allWords)