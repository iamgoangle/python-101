#!/usr/bin/python

lists = ['go', 'python', 'java', 'javascript']

# Print
print lists[0]
print lists[:2] # length
print lists[0:3] # start and slice

# update
lists[0] = 'typescript'
print lists

# delete
del lists[3]
print lists

# length
print len(lists)

# merge
listA = [1, 2, 3]
listB = [4, 5, 6]

listC = listA + listB
print listC

# Find in list
print 10 in [True, False, 11, 9+1]

# compare
listA = [1, 2, 3]
listB = [4, 5, 6]

print cmp(listA, listB)

# append list
listA = ['teerapong', 'singthong']
listA.append('software engineer')
print listA

# find usage count in list
listA = [1, 1, 2, 3, 4]
print listA.count(1)

# insert list
listA = [1, 2, 3, 4, 5, 6]
listA.insert(4, True)
print listA

# remove value in list
listA = [1, 2, 3, 4, 1]
listA.remove(1)
print listA