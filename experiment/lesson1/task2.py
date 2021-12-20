#  Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
#  (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

mylist = ['class', 'function', 'method']
for i in mylist:
    ordered = [ord(j) for j in i]
    mybytes = bytes(ordered)
    print(f'тип: {type(mybytes)}')
    print(f'содержимое: {mybytes}')
    print(f'длина переменной: {len(mybytes)}')
