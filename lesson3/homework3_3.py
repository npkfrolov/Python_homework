# coding=utf-8
"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

var1 = int(input("Введите число_1: "))
var2 = int(input("Введите число_2: "))
var3 = int(input("Введите число 3: "))


def my_func():
    my_list = [var1, var2, var3]
    my_list.sort()
    number1 = my_list[1]    # находит предпоследнее в сортированном списке число
    number2 = my_list [2]   # находит последнее в сортированном списке число
    return number1 + number2


print(my_func())

