# coding=utf-8
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_string = raw_input("Enter several words devided by spaces\n(words that are longer than 10 symbols will be trimmed): ")

words = user_string.split()
for ind, el in enumerate(words, 1):
    if len(el) > 10:
        print(ind, el[0:10])
    else: print(ind, el)
