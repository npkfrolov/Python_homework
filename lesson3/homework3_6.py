# coding=utf-8
"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""

text = None


def int_func():
    return text.title()


user_word = input("Введите слово из маленьких латинских букв: ")
text = user_word
print(int_func())
user_string = input("Теперь введите латинскими буквами строку из слов в нижнем регистре, разделенных пробелом: ")
text = user_string
print(int_func())
