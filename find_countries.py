#!/usr/bin/python3
import pickle
import re
from collections import defaultdict
<<<<<<< HEAD
import json
=======
from datetime import datetime
>>>>>>> 3b810f683a0222a8dcd37fedbfedf7d28b8b5676

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
    prev = datetime.now()
    countries = get_countries()

    start_year = 1842
    end_year = 1954
    for year in range(start_year, end_year + 1,4):
        time_elasped = datetime.now() - prev
        prev = datetime.now()
        print(time_elasped)
        print("Searching ",year)

        articles = pickle.load(open('data1500/samples_'+str(year),'rb'))
        freq = defaultdict(int)
        for k, text in articles.items():
            text = text.upper()
    ###        print("Searching article ",k)
            for country, missspellings in countries.items():
                for miss in missspellings:
                    if miss in text:
                        freq[country] += 1
                        break
        pickle.dump(freq,open('data1500/countries_'+str(year),'wb'))

