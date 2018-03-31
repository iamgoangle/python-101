#!/usr/bin/python

import json
from pprint import pprint
try:
    file = open("./example.json", "r")
    data = json.load(file)
    pprint(data)
except IOError:
    print "Could not load file"
else:
    print "Open json file"
    file.close()      
