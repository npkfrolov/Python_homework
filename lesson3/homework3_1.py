# coding=utf-8
"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

user1 = input("Введите число 1: ")
user2 = input("Введите число 2: ")

def my_func(var1, var2):
    try:
        var1 = float(var1)
        var2 = float(var2)
        result = var1 / var2
    except ZeroDivisionError:
        print("Ошибка деления на ноль")
        return
    except ValueError:
        print("Вы ввели не число")
        return
    return result


print(my_func(user1, user2))
