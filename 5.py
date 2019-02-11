#!/usr/bin/env python

print 'Enter any 10 numbers:'
l=[]
i=1
while (len(l)!=10):
	a=input('Number '+str(i)+':')
	i+=1
	l.append(a)
print 'List1 :'+str(l)

even=[]
odd=[]
for i in l:
	if i%2==0:
		even.append(i)
	elif i%2!=0:
		odd.append(i)

print 'even:'+str(even)
print 'odd:'+str(odd)
print 'even_sum='+str(sum(even))
print 'odd_sum='+str(sum(odd))