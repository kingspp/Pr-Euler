'''
Created on Aug 15, 2014

@author: Prathyush
'''
from main import test

print "Fibonacci Series"

start = test.Time()

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
end = test.Time()


print 'Elapsed test: '+str(end-start)+'s'


    
        
        
          