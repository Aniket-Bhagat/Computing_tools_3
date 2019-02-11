#!/usr/bin/env python

l1 = ['a','b','c','d','e']
l2 = [1,2,3,4,5]
l3 = []
print 'List1: '+str(l1)
print 'List2: '+str(l2)

i=0;j=0
while (i<len(l1) and j<len(l2)):
	l3.append(l1[i])
	i+=1
	l3.append(l2[j])
	j+=1
print 'Merged List: '+str(l3)

c=dict(zip(l1,l2))
print 'Dict1: '+str(c)