# coding=utf-8
"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def personal():
    user_name = raw_input("Enter your name: ")
    user_sec_name = raw_input("Enter your second name: ")
    user_birth = raw_input("Enter year of your birth: ")
    user_place = raw_input("Enter your living place: ")
    user_email = raw_input("Enter your e-mail: ")
    user_phone = raw_input("Enter your phone number: ")
    return user_name, user_sec_name, user_birth, user_place, user_email, user_phone

name, sec_name, birth, place, email, phone = personal()
print ("Your personal data: name - %s, sec_name - %s, birth - %s, place - %s, email - %s, phone - %s" % (name, sec_name, birth, place, email, phone))


# personal ( name = user_name, user_sec_name, user_birth, place, email, phone )
