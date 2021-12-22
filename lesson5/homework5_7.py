"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{‘firm_1’: 5000, ‘firm_2’: 3000, ‘firm_3’: 1000}, {‘average_profit’: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""

with open("homework7.txt") as roll:
    dict1 = {}
    i = 0
    accum_profits = 0
    for line in roll:
        i += 1
        array = line.split(", ")
        profit = int(array[2]) - int(array[3])
        if profit >= 0:
            accum_profits = accum_profits + profit
        else:
            i -= 1      # скорректировал - если убытки, надо не просто их исключить, но и вычесть организацию из частного
        dict1.update({array[0]: profit})
    average_profit = accum_profits // i
    enterprises = [dict1, {'average_profit': average_profit}]
    print(enterprises)

import json

with open("enterprises.json", 'w', encoding='utf-8') as jsonfile:
    json.dump(enterprises, jsonfile)

