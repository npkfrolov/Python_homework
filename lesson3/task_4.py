# Определить, какое число в массиве встречается чаще всего.
import random

array = [random.randint(1, 10000) for i in range(5000)]
maxim = 0
index = 0

for j in array:
    q = array.count(j)
    if q > maxim:
        maxim = q
        index = j
print(f'чаще всего в массиве встречается число {array[index]}, ({maxim} раз)')