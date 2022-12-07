import nltk
from nltk.stem.porter import PorterStemmer
#nltk.download('punkt')
stemmer = PorterStemmer()

def tokenize(input):
    return nltk.word_tokenize(input)

def stemming(word):
    return stemmer.stem(word.lower())

def bagOfWords(tokenizedSentence, words):
    pass

def main():
    cuv = ["Organize", "organized", "organizing"]
    s_cuv = [stemming(s) for s in cuv]
    print(s_cuv)

if __name__ == '__main__':
    main()




