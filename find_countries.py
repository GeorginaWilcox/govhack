#!/usr/bin/python3
import pickle
from collections import defaultdict

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ -_'.?!"

def edits1(word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def get_countries():
    c = {}
    with open('countries.txt', 'r') as f:
        for line in f:
            country = line.strip()
            c[country.upper()] = country 
            for miss in edits1(country.upper()):
                c[miss] = country
    return c


            


if __name__ == '__main__':
    countries = get_countries()
    articles = pickle.load(open('samples_1914','rb'))
    freq = defaultdict(int)
    for k, text in articles.items():
        for country in countries.keys():
            if country in text.upper():
                freq[country] += 1
        

