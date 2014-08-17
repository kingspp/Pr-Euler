'''
Created on Aug 17, 2014

@author: Prathyush
'''
from main import test

start = test.Time()
print "Palindrome -  Highest Triplets"


a=999
b=999
resf=0

def pal(num):
    if num[::-1] == num:
       return True
    else:
       return False
	   

while a>900:
	while b>900:	
		res=a*b
		res=str(res)
		if pal(res)==True:
			if res>resf:
				resf=res
				print 'The product of ' + str(a) + '*' + str(b)+ ' is ' +str(resf)
				
			
		b=b-1
	b=999	
	a=a-1

end= test.Time()

print 'The test elapsed is: ' +str(end-start)+ 's'

