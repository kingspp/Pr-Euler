'''
Created on Aug 17, 2014

@author: Prathyush
'''
import time



start=time.time()

def eratosthenes2(n):
    res=0
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:            
            res=res+i
            multiples.update(range(i*i, n+1, i))
    print res
    
eratosthenes2(2000000)

end=time.time()
print 'The time elapsed is: ' +str(end-start)+ 's'