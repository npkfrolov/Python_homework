"""Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import random
from itertools import cycle
from functools import reduce

my_list = [1231, 345, 567, 788]
#result = []

with open("homework5.txt", "w") as file:
    file.write(" ".join(map(str, my_list)))
with open("homework5.txt", "r") as filled_file:
    content = filled_file.read()   # пытался сделать все в одном with в режиме r+, но это не работало
    figures = content.split(" ")
    my_sum = 0
    for el in figures:
        my_sum = my_sum + int(el)
    print(f"Сумма всех чисел составляет {my_sum}")

