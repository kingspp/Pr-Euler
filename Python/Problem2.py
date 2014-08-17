'''
Created on Aug 15, 2014

@author: Prathyush
'''
import time

print "Fibonacci Series"

start = time.time()

def Fib(MIN,MAX):
    fib=0
    even=0
    a,b=MIN,MIN+1
    for i in xrange (MAX):
        a,b=b,a+b
        if b>MAX:
            break
        if b%2==0:
            even+=b
        #print b
    return even
    

print Fib(0,4000000)   
end = time.time()


print 'Elapsed test: '+str(end-start)+'s'


    
        
        
          