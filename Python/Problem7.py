'''
Created on Aug 17, 2014

@author: Prathyush
'''
import math
from main import test

print '10001 Prime number'


start=test.Time()

i=0
num=0

def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

while num<=10000:
    if is_prime(i)==True:
        num+=1
    i=i+1
        

print 'The 10001st Prime: '+str(i-1)



end=test.Time()
print 'The test elapsed is: ' +str(end-start)+ 's'

