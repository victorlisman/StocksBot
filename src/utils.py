import nltk
import numpy as np
import yfinance
from nltk.stem.porter import PorterStemmer
#nltk.download('punkt')
stemmer = PorterStemmer()

def tokenize(input):
    return nltk.word_tokenize(input)

def stemming(word):
    return stemmer.stem(word.lower())

def bagOfWords(tokenizedSentence, words):
    tokenizedSentence = [stemming(w) for w in tokenizedSentence]
    bag = np.zeros(len(words), dtype=np.float32)

    for index, w in enumerate(words):
        if w in tokenizedSentence:
            bag[index] = 1.0

    return bag

def getCompanyName(ticker):
    try:
        stock = yfinance.Ticker(ticker)
        return stock.info['longName']
    except:
        return f'Could not find {ticker}'
    
def getTicker(companyName):
    try:
        stock = yfinance.Ticker(companyName)
        return stock.info['symbol']
    except:
        return f'Could not find {companyName}'

# tests
def main():
    cuv = ["Organize", "organized", "organizing"]
    s_cuv = [stemming(s) for s in cuv]
    print(s_cuv)

    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag = bagOfWords(sentence, words=words)
    print(bag)

if __name__ == '__main__':
    main()




