#!/usr/bin/python3
import os
import pickle
import json

years = {}
for filename in os.listdir("json_data"):
    year = filename.split('_')[1]
    freq = pickle.load(open("json_data/" + filename,'rb'))
    years[year] = [['Country', 'Mentions']]
    for country, count in freq.items():
        years[year].append([country, count])

print(json.dumps(years))


