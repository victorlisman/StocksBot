import torch
import json
import random 
import yfinance
from model import NeuralNet
from utils import bagOfWords, tokenize, getCompanyName

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('./intents.json', 'r') as f:
    intents = json.load(f)


FILE = "data.pth"
data = torch.load(FILE)

inputSize = data["input_size"]
hiddenSize = data["hidden_size"]
outputSize = data["output_size"]
allWords = data["all_words"]
tags = data["tags"]
modelState = data["model_state"]


model = NeuralNet(inputSize, hiddenSize, outputSize).to(device)
model.load_state_dict(modelState)
model.eval()

botName = "Deff"
#print("Let's chat! Type quit to exit!")

def getResponse(msg):
        ignoreWords = ['?', '!', '.', ',', ';']
        sentence = tokenize(msg)
        sentence = [word.lower() for word in sentence if word not in ignoreWords]

        ticker = sentence.pop()
        X = bagOfWords(sentence, allWords)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)

        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        specialTags = ['stock_prices', 'stock_info', 'stock_news']

        if prob.item() > 0.750:
            for intent in intents['intents']:
                if tag == intent["tag"] and tag not in specialTags:
                    return random.choice(intent['responses'])
                
                elif tag == 'stock_prices':
                    try:
                        stock = yfinance.Ticker(ticker)
                        hist = stock.history(period="1d")
        
                        return f'The price of {getCompanyName(ticker)} is {hist["Close"][0]:.2f} USD'
                    
                    except:
                        return f'Could not find {ticker}'   
                    
                elif tag == 'stock_info':
                    try:
                        stock = yfinance.Ticker(ticker)
                        news = stock.info['longBusinessSummary']
                        return news
                    
                    except:
                        return f'Could not find {ticker}'        
                    
                elif tag == 'stock_news':
                    try:
                        stock = yfinance.Ticker(ticker)
                        news = stock.news()
                        return random.choice(intent['responses']) + news   
                    
                    except:
                        return f'Could not find {ticker}'
                    
        return "I don't understand..."

def main():
    while True:
        sentence = input("You: ")
        print(f'{getResponse(sentence)}')

if __name__ == '__main__':
    main()

    