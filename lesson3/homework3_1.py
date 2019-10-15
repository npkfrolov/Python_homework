# coding=utf-8
"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_func (var1, var2):
    return var1 / var2

user1 = int(raw_input("Enter number_1: "))
user2 = int(raw_input("Enter number_2: "))  # дополнить решение делением на 0

print (my_func( user1, user2))




