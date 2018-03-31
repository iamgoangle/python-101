#!/usr/bin/python

import json
from pprint import pprint

# open json file
file = open("./example.json", "r")
data = json.load(file)

pprint(data)

file.close()