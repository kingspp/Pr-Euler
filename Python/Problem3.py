'''
Created on Aug 15, 2014

@author: Prathyush
'''
import math
from main import test

print 'Largest Prime Factor'
start=test.Time()
def is_prime(n):
    if n == 2:
        return 2
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return n

NUM=600851475143
root=int(math.sqrt(NUM))
for j in xrange(2,root):
    pr=is_prime(j)
    if pr!=False:
        if NUM%pr==0:
            fin=pr

print fin

end=test.Time()

print 'test elapsed is: '+str(end-start)+'s'