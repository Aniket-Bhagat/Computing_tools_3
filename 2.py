#!/usr/bin/env python

a=raw_input("Enter a string = ")
print '1.Length : '+str(len(a))

b=a+'Ilovepython'
print '2.Str2:"'+b+'" Length:'+str(len(b))

c=input("Enter any number (0-9): ")
c=b+(str(c)*5)
print '3.Str3:"'+c+'"'

l1=[]
for i in range(len(c)):
	if i%2==0:
		l1.append(c[i])
print '4.l1: '+str(l1)

d=''.join(l1[::-1])
print '5.'+str(d)

e=''.join(["a" if char.isdigit() else char for char in d])
print '6.'+e

print '7.'+e.upper()