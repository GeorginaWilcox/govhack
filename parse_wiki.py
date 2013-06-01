#!/usr/bin/python3

import xml.etree.ElementTree as etree

tree = etree.parse('wiki.xml')
root = tree.getroot()

for child in root:
    if child.tag == "tr":
        country = child[0]
        for t in country:
            if t.tag == "a":
                print(t.text)
