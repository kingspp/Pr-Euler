'''
Created on Aug 17, 2014

@author: Prathyush
'''

import time

print 'Pythogorean Triplets'

start=time.time()

N,M=0,0

for N in range(1001):
    for M in range(1001):    
        a= (N**2)-(M**2)
        b= 2*N*M
        c= (N**2)+(M**2)
        if a>0 and b>0 and c>0:
            if a+b+c==1000:
               
                break
    else:
        continue
    break
    N-=1
    M-=1



print str(a)+'+'+str(b)+'+'+str(c)+'= 1000'
print 'Product of Pythogorean triplets is: '+ str(a*b*c)
end=time.time()
print "test Elapsed is:" + str(end-start)+'s'