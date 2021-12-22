# Определить, какое число в массиве встречается чаще всего.
import random
import timeit
import cProfile

SIZE = 100000
MIN_ITEM = 0
MAX_ITEM = 100000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# решение 1
def func1():
    maxim = 1
    index = 0

    for pos, j in enumerate(array):
        q = array.count(j)
        if q > maxim:
            maxim = q
            index = pos
    return (f'Чаще всего в массиве встречается число {array[index]} ({maxim} раз(а))' if maxim > 1 else 'Все элементы уникальны')

# решение 2
def func2():
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    return(f'Число {num} встречается {frequency} раз(а)' if frequency > 1 else 'Все элементы уникальны')

# решение 3
def func3():
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return(f'Число {num} встречется {frequency} раз(а)')
    else:
        return('Все элементы уникальны')

# SIZE = 10, диапазон 100000
print(timeit.timeit('func1()', number=100, globals=globals()))   #0.0002473280001140665
print(timeit.timeit('func2()', number=100, globals=globals()))   #0.00038534600025741383
print(timeit.timeit('func3()', number=100, globals=globals()))   #7.950700000947108e-05
cProfile.run('func1()')     # 10    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
cProfile.run('func2()')     # 11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('func3()')     #всего 4 строки, все нули

# SIZE = 1000, диапазон 100000
# print(timeit.timeit('func1()', number=100, globals=globals()))   #1.0737237779994757
# print(timeit.timeit('func2()', number=100, globals=globals()))   #2.6159113710000383
# print(timeit.timeit('func3()', number=100, globals=globals()))   #0.008681058000547637
# cProfile.run('func1()')     # 1000    0.010    0.000    0.010    0.000 {method 'count' of 'list' objects}
# cProfile.run('func2()')     # 1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('func3()')     #всего 4 строки, все нули

# SIZE = 10000 (не удалось дождаться 100000), диапазон 100000
# print(timeit.timeit('func1()', number=100, globals=globals()))   #114.99433217300066
# print(timeit.timeit('func2()', number=100, globals=globals()))   #282.309134522
# print(timeit.timeit('func3()', number=100, globals=globals()))   #0.0987884780006425
# cProfile.run('func1()')     # 10000    1.099    0.000    1.099    0.000 {method 'count' of 'list' objects}
# cProfile.run('func2()')     # 10001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# cProfile.run('func3()')     #     1    0.001    0.001    0.001    0.001 les4_task_1.py:40(func3)

# Вывод: решения 1 и 2 оба квадратичной сложности: при увеличении размера массива на порядок время увеличивается на два порядка.
# Второе решение само по себе вдвое медленнее первого, вероятно, за счет того, что операция по измерению длины массива (решение 2)
# осуществляется дважды (в двух циклах), а операция подсчета числа включений в массив искомого значения выполняется один раз (решение 1).
# Решение 3 линейной сложности - время возрастает кратно увеличению размера массива. При наличии большой оперативной памяти очень быстрая.
# Отдельно для решения 3 протестировал на массиве 100000 записей. Время - 1.2417318890002207