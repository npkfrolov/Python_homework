# coding=utf-8
"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def personal():
    user_name = input("Введите имя: ")
    user_sec_name = input("Введите фамилию: ")
    try:
        user_birth = int(input("Введите год рождения: "))
    except ValueError:
        print("Нужно ввести цифры")     # Пока что не придумал, как отсюда вернуть на запрос даты
    user_place = input("Введите место проживания: ")
    user_email = input("Введите e-mail: ")
    user_phone = input("Введите телефонный номер: ")

    return user_name, user_sec_name, user_birth, user_place, user_email, user_phone

name, sec_name, birth, place, email, phone = personal()
print ("Your personal data: name - %s, sec_name - %s, birth - %s, place - %s, email - %s, phone - %s" % (name, sec_name, birth, place, email, phone))
