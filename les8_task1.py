# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib

str = input(f'Введите строку: ')
array = []

def func(str):
    n = len(str)
    for i in range(n):
        for j in range(n-i):
            spam = hashlib.sha1(str[i:i + j + 1].encode('utf-8')).hexdigest()
            array.append(spam)
            print(str[i:i + j + 1]) #для контроля, какие строки навыделял

func(str)
print(f'Уникальных подстрок в строке (не считая самой строки) {len(set(array)) - 1}')