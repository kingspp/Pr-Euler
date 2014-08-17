'''
Created on Aug 16, 2014

@author: Prathyush
'''
import time
print "To find the multiples of 3 and 5"

start = time.time()
num=0

for i in xrange (3,1000):
    if i%3==0:
        num+=i
    elif i%5==0:
        num+=i;
    

print num
end = time.time()
print 'Elapsed test: '+str(end-start)+'s'

