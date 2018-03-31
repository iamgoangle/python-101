#!usr/bin/python

def printMe(str):
    "print the string output"
    print str
    return

print('Teerapong Singthong')

# pass by reference
def changeList(lists, v):
    "pass by reference function"

    lists.append(v)
    return lists

listA = [1, 2, 3]
print listA
changeList(listA, 4)
print listA