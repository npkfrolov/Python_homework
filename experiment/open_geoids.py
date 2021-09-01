import json
from itertools import combinations
import csv

def inters(myset,  digit):  # функция принимает набор множеств и их количество, находит все пересечения
        mystr = 'list(set.intersection('  # поскольку число множеств меняется, формируем строку, которую затем исполняем
        # как код
        for inx, el in enumerate(myset):
                if inx != 0:
                        mystr += ', '
                mystr += f'set(myset[{inx}])'
                if inx == digit-1:
                        mystr += '))'
        res = eval(mystr)  # запуск строки как кода
        return res

with open(f'/home/alexey/Документы/Google_disk/Тексты/АбулФида_2021/array.json', 'r') as file:
        data = json.load(file)
        template = {}

        for key, value in data.items():  # переформатируем джейсон, чтобы можно было работать с множествами.
            # Возможно, это не оптимально, но работает
            tuples = list(map(tuple, value))
            mydict = {key: tuples}
            template.update(mydict)

        mylist = list(template.values())  # делаем список из всех кортежей с параметрами, сгруппированных по парам
        # городов
        mykeys = list(template.keys())  # чтобы понимать, откуда какие кортежи, делаем параллельно список
        # соответствующих пар городов
        with open(f'/home/alexey/Документы/Google_disk/Тексты/АбулФида_2021/sets.csv', 'w') as file2:
            csvwriter = csv.writer(file2, dialect = 'excel')  # полностью результат в терминал не влезает, так что пишем
            # в табличный файл
            # for digit in range(5, len(mylist)):  # для перебора всех сочетаний городов разной длины (не менее 2 пар,
                # чтобы можно было выявлять пересечение множеств) Временно отказался от этого цикла, чтобы сэкономить
            # мощности, значение digit пробую задавать вручную
            digit = 6
            mykeys_comb = list(combinations(mykeys, digit))  # выявляем все возможные комбинации пар городов
            # заданной длины
            combi = list(combinations(mylist, digit))  # собираем все соответствующие комбинации наборов кортежей
            z = 0

            for ind, myset in enumerate(combi):  # перебираем комбинации кортежей заданного числа множеств
                inter = list(inters(myset, digit))  # находим пересечение множеств для всех этих комбинаций
                # print(  (inter))

                if len(inter) > 0:  # печатаем, если нашелся хотя бы один кортеж, общий для всех множеств
                        z += 1  # увеличиваем счетчик, чтобы остановить цикл,  когда ни одна комбинация множеств их
                        # заданного числа не даст хотя бы одного пересечения
                        report = f'{mykeys_comb[ind]}; большая ось больше; {len([m for m in inter if m[0]>m[1]])}:малая ось больше:{len([m for m in inter if m[0] < m[1]])}:оси равны:{len([m for m in inter if m[0] == m[1]])}:всего:{len(inter)}'
                        csvwriter.writerow([digit, mykeys_comb[ind], len(inter), len([m for m in inter if m[0] > m[1]]), len([m for m in inter if m[0] < m[1]])])
                        print(report)
            if z == 0:
                print(f'Дальнейший перебор вариантов не имеет смысла, '
                      f'ни одна из комбинаций {digit} множеств не дала пересечений')
                # break
