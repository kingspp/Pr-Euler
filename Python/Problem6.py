'''
Created on Aug 16, 2014

@author: Prathyush
'''

import math
import time

print "Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum"
SUM1=0
SUM2=0
start=time.time()

for i in xrange(1,100+1):
    SUM1+=i
    SUM2+=i**2
SUM1=SUM1**2




print SUM1-SUM2


end=time.time()

print 'The test elapsed is: ' +str(end-start)+ 's'

