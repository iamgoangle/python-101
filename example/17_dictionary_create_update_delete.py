#!usr/bin/python

dictA = {
    'firstname': 'teerapong', 
    'lastname': 'singthong'
}

# add dictionary
dictA['age'] = 20

# update dictionary
dictA['age'] = 22
print dictA

# remove value
del dictA['age']

# clear dictionary
dictA.clear()

# printable string
dictB = {
    'firstname': 'teerapong', 
    'lastname': 'singthong'
}
print str(dictB)
print type(dictB)


print dictA