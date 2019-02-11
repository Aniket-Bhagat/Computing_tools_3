#!/usr/bin/env python

s=raw_input("Enter any string of length 10 should contain at least two repeating elements:\n")
if len(s)>10:
	print "String length is greater than 10"
else:
	print 'Input String is: '+s
	print 'List: '+str(list(s))
	print 'Tuple: '+str(tuple(s))
	print 'set: '+str(set(s))+'\n'