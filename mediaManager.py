import random
import os

quotes = []

def setupQuotes():
    f = open('quotes.txt', 'r')
    for x in f:
        quotes.append(x)
    f.close()

def getImage():
    return "img/" + random.choice(os.listdir("img/"))

def getQuote():
    return random.choice(quotes)

def setup():
    setupQuotes()
    print(quotes)
