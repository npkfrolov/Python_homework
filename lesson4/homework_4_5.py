# coding=utf-8
"""Реализовать формирование списка, используя функцию range() и возможности генератора.
 В список должны войти четные числа от 100 до 1000 (включая границы).
 Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce()"""

from functools import reduce
def my_function(el1, el2):
    return el1 * el2

my_list = list(el for el in range(100, 1001, 2))
print(reduce(my_function, my_list))

