'''
Created on Aug 17, 2014

@author: Prathyush
'''
import time

print 'Sum of 20 milliion primenumbers'

start=time.time()


def sieve(n):
    res=0
    multiples=set()
    for i in range (2,n+1):
        if i not in multiples:
            res+=i
            multiples.update(range(i*i,n+1,i))
    print res
    
    

sieve(2000000)
end=time.time()
print 'The time elapsed is: ' +str(end-start)+ 's'