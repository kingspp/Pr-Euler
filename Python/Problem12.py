"""
@Created on: 25/08/16,
@author: Prathyush SP

"""
import time
import math

start = time.time()


def triangular_number():
    tri_number = None
    for i in range(2, 100000):
        yield tri_number
        tri_number = sum(list(range(1, i)))


num = triangular_number()
next(num)

for i in range(10000000):
    append = True
    t_num = next(num)
    divs = [1]
    [divs.extend([i, int(t_num / i)]) for i in range(2, int(math.sqrt(t_num)) + 1) if t_num % i == 0]
    if len(set(divs)) > 500:
        print(t_num)
        break

end = time.time()
print('Elapsed test: ' + str(end - start) + 's')
