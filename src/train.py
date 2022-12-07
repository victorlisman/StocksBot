import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from utils import tokenize, stemming, bagOfWords
from model import NeuralNet

with open('./intents.json', 'r') as f:
    intents = json.load(f)

allWords = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        allWords.extend(w)
        xy.append((w, tag))

ignoreWords = ['?', '!', '.', ',', ';']
allWords = [stemming(w) for w in allWords if w not in ignoreWords]
allWords = sorted(set(allWords))
tags = sorted(set(tags))

X_train = []
y_train = []

for (patternSentence, tag) in xy:
    bag = bagOfWords(patternSentence, allWords)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

class StockBotDataset(Dataset):
    def __init__(self):
        self.numSamples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.numSamples

batchSize = 8
inputSize = len(X_train[0])
hiddenSize = 8
outputSize = len(tags)

print(input, len(allWords))
print(outputSize, tags)

dataset = StockBotDataset()
trainLoader = DataLoader(dataset=dataset, batch_size=batchSize, shuffle=True, num_workers=2)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(inputSize, hiddenSize, outputSize).to(device)

#de facut learning rate si optimizer