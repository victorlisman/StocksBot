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


batchSize = 8
inputSize = len(X_train[0])
hiddenSize = 8
outputSize = len(tags)
learningRate = 0.001
numEpochs = 1000

#print(inputSize, len(allWords))
#print(outputSize, tags)


class StockBotDataset(Dataset):
    def __init__(self):
        self.numSamples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.numSamples

dataset = StockBotDataset()
trainLoader = DataLoader(dataset=dataset, batch_size=batchSize, shuffle=True, num_workers=2)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(inputSize, hiddenSize, outputSize).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)


def main():
    for epoch in range(numEpochs):
        for (words, labels) in trainLoader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)

            outputs = model(words)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'epoch {epoch + 1} / {numEpochs}, loss = {loss.item():.4f}')

    print(f'final loss, loss = {loss.item():.4f}')

data = {
    'model_state': model.state_dict(),
    'input_size': inputSize,
    'hidden_size': hiddenSize,
    'output_size': outputSize,
    'all_words': allWords,
    'tags': tags
}

FILE = data.pth
torch.save(data, FILE)

#write chat implementation in bot.py


if __name__ == '__main__':
    main()