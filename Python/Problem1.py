'''
Created on Aug 16, 2014

@author: Prathyush
'''
<<<<<<< HEAD
import time
print "To find the multiples of 3 and 5"

start = time.time()
=======
from main import test
print "To find the multiples of 3 and 5"

start = test.Time()
>>>>>>> 71df3e73de1f7d326f1eeda65a9ba5fef9b87c38
num=0

for i in xrange (3,1000):
    if i%3==0:
        num+=i
    elif i%5==0:
        num+=i;
    

print num
<<<<<<< HEAD
end = time.time()
=======
end = test.Time()
>>>>>>> 71df3e73de1f7d326f1eeda65a9ba5fef9b87c38
print 'Elapsed test: '+str(end-start)+'s'

