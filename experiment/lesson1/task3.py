# Определить, какие из слов «attribute», «класс», «функция», «action_type» невозможно записать в байтовом типе.

mylist = ['attribute', 'класс', 'функция', 'action_type']

for i in mylist:
    try:
        ordered = [ord(j) for j in i]
        print(bytes(ordered))
    except ValueError:
        print(f'Cтрока "{i}" не может быть записана в байтовом типе')