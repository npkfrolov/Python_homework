# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

q = int(input('Введите число предприятий: '))
i = 1
enterpr_inc = {}

while i <= q:
    name = input(f'Введите название {i}-го предприятия: ')
    year = 0
    for j in range(1, 5):
        quart_inc = int(input(f'Введите размер прибыли предприятия {name} за {j}-й квартал: '))
        year += quart_inc
        enterpr_inc.update([(name, year)])
    i += 1
c = sum(values for values in enterpr_inc.values()) / q
winners = defaultdict(list)
for key, value in enterpr_inc.items():
    if value > c:
        winners[value].append(key)
loosers = defaultdict(list)
for key, value in enterpr_inc.items():
    if value < c:
        loosers[value].append(key)

print(f'Средний годовой доход составляет {c}')
print(f'Предприятия с прибылью ниже среднего значения:\n {loosers}\n; Предприятия с прибылью выше среднего значения:\n {winners}:\n')