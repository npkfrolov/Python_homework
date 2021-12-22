# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
# элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from itertools import zip_longest

a = list(input('Введите первое шестнадцатеричное число: '))
b = list(input('Введите второе шестнадцатеричное число: '))
mydict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a':10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
new_a = []
new_b = []

for i in a:
    new_a.append(mydict.get(i)) #перевод в десятичные числа

for j in b:
    new_b.append(mydict.get(j)) #перевод в десятичные числа

new_a = deque(new_a)
new_b = deque(new_b)

new_a.reverse() # разворот чисел, чтобы их можно было суммировать, начиная с единиц
new_b.reverse() # разворот чисел, чтобы их можно было суммировать, начиная с единиц
summ = [x + y for x, y in zip_longest(new_a, new_b, fillvalue=0)]   # суммирование десятичных чисел
res1 = []
res2 = [0] * (len(summ)+1)

for index, k in enumerate(summ): #преобразование в 16-ричные числа через деление на 16
    if k < 16:
            res1.append(k)
    else:
        res1.append(k % 16)
        spam = index+1
        res2[spam] = (k // 16)  # перенос целочисленной части результата деления в следующий разряд
summ2 = [x + y for x, y in zip_longest(res1, res2, fillvalue=0)]   # суммирование 16-ричных чисел в десятичном представлении
res3 = [0] * (len(summ2))

for index, m in enumerate(summ2): #проверка результата суммирования, поиск результата = 16
    if m == 16:
        summ2[index] = 0
        eggs = index+1
        res3[eggs] = 1  # перенос целочисленной части результата деления в следующий разряд
summ3 = [x + y for x, y in zip_longest(summ2, res3, fillvalue=0)]   # суммирование 16-ричных чисел в десятичном представлении

if summ3[len(summ3)-1] == 0:   # удаление лишнего 0 при его наличии в конце списка
    summ3.pop()

summ3.reverse() # обратный разворот чисел

res4 = []
inv_mydict = {value: key for key, value in mydict.items()}  # меняем местами ключи и значения для обратной конверсии в 16-ричные числа

for p in summ3:     # объединяем отдельный цифры в число
    res4.append(inv_mydict.get(p))
result = ''.join(res4)

print(summ)
print(res1)
print(res2)
print(summ2)
print(summ3)
print(res4)
print(f'Сумма указанных чисел равна {result}')




