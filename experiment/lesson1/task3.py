# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

mylist = ['attribute', 'класс', 'функция', 'type']

for i in mylist:
    try:
        ordered = [ord(j) for j in i]
        print(bytes(ordered))
    except ValueError:
        print(f'Cтрока "{i}" не может быть записана в байтовом типе')
