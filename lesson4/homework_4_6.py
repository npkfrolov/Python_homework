# coding=utf-8
"""Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

from sys import argv

option = int(input("Какой из итераторов запустить (1|2)? "))
if option == 1:
    from itertools import count

    params = input("Укажите цифрами через пробел два параметра: начальное число и количество значений  ")
    params.split()
    param1 = int(params[0])
    param2 = int(params[2])  # по непонятной причине пробел здесь воспринимается как элемент списка
    for el in count(param1, 1):
        if el > param2:
            break
        else:
            print(el)
elif option == 2:
    from itertools import cycle

    param3 = int(input("Укажите цифрами число строк итератора:  "))
    my_list = ["зима", "весна", "лето", "осень"]
    i = 0
    for el in cycle(my_list):
        if i > param3:
            break
        print(el)
        i += 1
else:
    print("Ошибка выбора")
