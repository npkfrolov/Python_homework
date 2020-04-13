# coding=utf-8
"""Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень."""


def my_func():
    try:
        x = float(input("Введите действительное положительное число: "))
        y = int(input("Введите целое отрицательное число: "))   # как проконтролировать то: что значение отрицательное?
    except ValueError:
        return
    y = abs(y)
    i = 1  # счетчик числа операций
    m = x  # промежуточный результат умножения
    while i < y:
        i += 1
        m = m * x
    return m


print(my_func())

