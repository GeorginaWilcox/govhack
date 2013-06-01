#!/usr/local/bin/python3

import urllib.request
import urllib.parse
import sys
import json
import re

STRIP_HTML = re.compile("<[^>]*>")


def sample_year(year, num_samples):
    params = {
        "key": "5m4qenopv01a7nsl",
        "q": 'have date:[%d TO %d]' % (year, year + 1),
        "encoding": "json",
        "include": "articletext",
        "l-title": "35",
        "zone": "newspaper",
        "sortby": "relevance",
        "n": 100,
    }
    count = 0
    articles = {}
    while count < num_samples:
        params["s"] = count
        url = "http://api.trove.nla.gov.au/result?" + urllib.parse.urlencode(params)
        
        r = urllib.request.Request(url)

        response = urllib.request.urlopen(r)
        str_response = response.readall().decode('utf-8')
        data = json.loads(str_response)
        newspapers = data['response']['zone'][0]['records']
        num_results = int(newspapers['n'])
        count += num_results

        for article in newspapers['article']:
            text = STRIP_HTML.sub("",article['articleText'])
            article_id = article['id']
            articles[article_id] = text
    return articles


###newspapers = data['response']['zone'][0]
###print("Total records: ", newspapers['records']['total'])
###num_results = newspapers['records']['n']
###for article in newspapers['records']['article']:
###    text = STRIP_HTML.sub("",article['articleText'])
###    article_id = article['id']
###    
###    print(article_id, ": ", text[:70])
if __name__ == '__main__':
    import pickle
    articles = sample_year(1914,200)
    w = open('samples_1914','wb')
    pickle.dump(articles,w)
