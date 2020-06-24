# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

import random

array = [random.randint(-100, 100) for i in range(50)]
index = -1
j = 0
number = 0

while j < len(array):
    if array[j] < 0 and index == -1:
         index = j
    elif array[j] < 0 and array[j] > array[index]:
        index = j
        number = array[j]
    j += 1

print(array)
print(f'Наибольшим из отрицательных чисел массива является число {number} с индексом {index}')