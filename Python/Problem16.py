"""
@Created on: 25/08/16,
@author: Prathyush SP

"""
import time
start = time.time()

str_pow = str(2**1000)
print(sum([int(digit) for digit in str_pow]))

end = time.time()
print('Elapsed test: ' + str(end - start) + 's')
