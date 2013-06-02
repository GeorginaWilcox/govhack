#!/usr/bin/python3
import pickle
import re
from collections import defaultdict
import json

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ -_'.?!"

def edits1(word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def get_countries():
    c = defaultdict(set)
    with open('countries.txt', 'r') as f:
        for line in f:
            country = line.strip()
            aliases = country.split('\t')
            for alias in aliases:
                c[country].add(alias.upper())
                if len(alias) > 4:
                    c[country].update(edits1(country.upper()))
    return c


            


if __name__ == '__main__':
    countries = get_countries()
    articles = pickle.load(open('samples_1914','rb'))
    
    freq = defaultdict(int)
    for k, text in articles.items():
        text = text.upper()
###        print("Searching article ",k)
        for country, missspellings in countries.items():
            for miss in missspellings:
                if miss in text:
                    freq[country] += 1
                    break
    data = [['Country', 'Number of mentions']]
    for country in freq:
        data.append([country, freq[country]])

    print(json.dumps(data))        

