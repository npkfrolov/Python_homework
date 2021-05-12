import cProfile
from threading import Thread
import itertools
import timeit
import operator

from numpy import float32, ix_, array, arange, argwhere, array_split, set_printoptions, unique

# выбор типа данных: с float16 элемент занимает в памяти всего 2 байта, но подсчеты неточны - при поиске искомого числа
# много ошибок. float32 и 64 дают либо такое же количество комбинаций, либо втрое меньше - их результат не отличается,
# но первый занимает места вдвое меньше второго (4 байта против 8). Кроме того, расчеты выполняются почему-то
# значительно быстрее, чем при float16.

rozh_price = 10
oves_price = 5
pshen_price = 14
yachmen_price = 7
look_for_match = 352  # float(input('Соответствие какой сумме мы ищем (в деньгах)?'))
obji_count = 10.5  # float(input('Сколько обеж у нас есть?'))
obj_step = 0.5
corob_step = 0.25
scope_na_obju = 4

norma_corob = arange(0, scope_na_obju + corob_step, corob_step, dtype=float32)  # это варианты нормы (в коробьях хлеба),
# по которой дается хлеб с одного варианта количества обеж
print(f'Для заданного обежного оклада используются следующие комбинации норм в коробьях: {norma_corob}')

list_obj = arange(obj_step, obji_count + obj_step, obj_step, dtype=float32)  # это варианты количества обеж, платящих хлебный
# оброк
combins_obj = []

for j in range(4):  # range(int(obji_count/2)+2):
    mylist = [i for i in list(itertools.combinations(list_obj, j)) if sum(i) == obji_count]  # делаем список всех
    # вариантов деления обеж на группы, в сумме дающих известное число обеж владения
    combins_obj.extend(mylist)

# combinations_count = 2  # int(input(f'Какое число групп обеж, дающих хлеб по одной норме, рассчитываем?
# От этого зависит, какие комбинации обежных групп будут рассчитаны. '))
# user_count_combinations = [i for i in combins_obj if len(i) == combinations_count]
# print(f'Все возможные комбинации заданного числа групп обеж (в сумме дают оклад владения): ')

print(f'Все возможные комбинации обеж (в сумме дают оклад владения): ')

for numb, i in enumerate(combins_obj):
    print(f'Номер {numb}: {i}')


def arrays_to_axis(arr):  # принимает набор одномерных массивов и дает им размерность, равную количеству входных
    # массивов, для последующих операций с массивами
    array_n_dims = []
    for ind, elem in enumerate(arr):
        list_of_table = [1] * len(arr)
        # print(list_of_table)
        list_of_table[ind] = len(elem)  # для транслирования одномерного массива в отдельное измерение создаем
        # описание мерности, где все измерения равны единице - кроме того, куда будем транслировать одномерный массив
        elem.shape = list_of_table  # приводим массив к форме, готовой для трансляции
        # print(f'{ind}: {arr_prod_prices}')
        array_n_dims.append(elem)
    return array_n_dims


def hleb_price(index, arr):   # транслирует список цен на одномерный массив с платежами хлебом
    prices = [rozh_price, oves_price, pshen_price, yachmen_price]
    sort = index // length  # делим без остатка порядковый номер одномерного массива на число массивов,
    # относящихся к одному сорту хлеба и определяем, на цену какого хлеба нужно множить элементы этого массива
    return arr * prices[sort]


def division_by_parts(row):     # создает генератор, который делает в списке срез заданной длины для дальнейшей
    # запаковки в кортеж и поиска кортежей индексов, одинаковых для разных сортов хлеба
    for elem in range(0, len(row), length):
        yield row[elem: elem + length]


def equal_norms(array_to_filter):   # фильтрует массив, отбирая из него записи, где нормы платежей хлебом
    # либо совпадают для всех сортов хлеба (len(in_tuples) == 1), либо совпадает часть. Пока не отстроил,
    # поэтому значение равно 4
    equal_list = []
    # print(array_to_filter)
    for m in array_to_filter:
        # print(m)
        in_tuples = set()
        myparts = division_by_parts(m)
        for o in myparts:
            temp = tuple(o)
            # print(temp)
            in_tuples.add(temp)
        # print(in_tuples)
        if len(in_tuples) == 4:
            equal_list.append(list(m))
    # print(equal_list)
    return equal_list


def money_summ(arr, rows):     # считаем суммы денежных платежей для набора одномерных массивов. Можно упростить -
    # часть функционала выполняется функцией arrays_to_axis
    long = len(arr)
    array_money_dims = []

    for ind, i in enumerate(arr):
        list_of_table = [1] * long
        # print(list_of_table)
        list_of_table[ind] = rows  # для транслирования одномерного массива в отдельное измерение создаем
        # описание мерности, где все измерения равны единице - кроме того, куда будем транслировать одномерный массив
        # print(f'{tupl}: {list_of_table}')
        arr_prod_prices = hleb_price(ind, i)  # умножаем элементы массива на цену соответствующего сорта хлеба
        arr_prod_prices.shape = list_of_table  # приводим массив к форме, готовой для трансляции
        # print(f'{ind}: {arr_prod_prices}')
        array_money_dims.append(arr_prod_prices)
    return array_money_dims


templates_all_combs = []
for tupl in combins_obj:     # перебираем кортежи, представляющие варианты группировки обеж исследуемого владения
    # print(len(combins_obj))
    combins_obj_arr = array(tupl, dtype=float32)  # создаем одномерный массив с комбинацией обеж, дающих в сумме оклад
    # владения
    # print(combins_obj_arr)
    norma_corob_ax, combins_obj_arr_ax = ix_(norma_corob, combins_obj_arr)  # создаем двумерный массив,
    # по одной оси - возможные нормы коробей, по другой - возможные комбинации обеж
    template = norma_corob_ax*combins_obj_arr_ax  # шаблон получаем, умножив поэлементно норму платежа на число обеж
    # в группе.
    # Теперь можно транслировать его на матрицы сортов хлеба и суммировать деньги
    columns_count = template.shape[1]  # число полей в шаблоне
    template_list = array_split(template, columns_count, axis=1)  # разрезаем шаблон по столбцам на матрицы с одним
    # столбцом, чтобы в дальнейшем собрать из них матрицу с соответствующим числом измерений
    # print(template)
    template_accum = []  # сюда будем собирать одномерные массивы
    for i in template_list:  # идем по списку с двухмерными матрицами, убираем лишнее измерение и делаем вектор
        flat_arr = i.flat
        template_accum.append(array(flat_arr, dtype=float32))
    # print(f'Набор одномерных массивов: {tupl} - {template_accum}')
    templates_all_combs.append(template_accum)
# print(f'Набор одномерных массивов: {len(templates_all_combs)}')


def vars_one_tuple(mytupl):
    # template_list = None
    template_accum_4items = [templates_all_combs[mytupl]]*4
    unnest_list = [*template_accum_4items]  # здесь избавляемся от первой вложенности
    unnest_corob_4items = list(itertools.chain.from_iterable(unnest_list))  # для каждой комбинации обежных групп
    # получаем
    # список из массивов, в котором первые массивы (по числу обежных групп) - будущие оси по ржи, следующие -по овсу итд
    # print(f'Распакованный список одномерных массивов: {unnest_corob_4items}')

    four_dim = sum(money_summ(unnest_corob_4items, rows_count))  # складываем все измерения и получаем многомерную
    # матрицу со всеми комбинациями платежей от разных групп обеж по всем сортам хлеба
    # unnest_corob_4items = None

    dengi = four_dim == look_for_match
    dengi_ind = argwhere(dengi)

    duplicates_away = []
    for i in dengi_ind:
        for j in i.reshape(-1, length):
            if len(i) == len(set(i)):
                duplicates_away.append(i)

    duplicates_cleared = unique(duplicates_away, axis=0)

    set_printoptions(edgeitems=100)
    # print(f'По группе обеж {tupl} выявлено {duplicates_cleared.size/(length*4)} комбинаций')
    # print(f'Кортеж {tupl}: {temp.reshape[[len(norma_corob)]*length*4]}')
    question1 = 2  # int(input(f'Оставить только варианты, где нормы сортов хлеба одинаковы для каждой группы обеж
    # (да - 1, нет - 2): '))
    if question1 == 1:
        # print(duplicates_cleared)
        answer1 = equal_norms(duplicates_cleared)
        # print(answer1)
        for k in answer1:
            print(f'Совпадения по сумме денег, группа обеж {tupl}: {k} "-->" рожь: {norma_corob[k][0]}, '
                  f'овес: {norma_corob[k][1]}, пшеница: {norma_corob[k][2]}, ячмень: {norma_corob[k][3]}')
            # здесь вместо индексов должны быть суммы по индексам одного сорта хлеба
            print(f'Всего комбинаций{len(answer1)}')
    # else:
    #     question2 = int(input(f'Выбрать комбинации норм, которые при выбранной комбинации обеж дают заданные объемы
    #     # хлеба (да - 1, нет - 2): '))
    #     if question2 == 1:


def search_corob(arr, sort):
    condition = arr == sort   # здесь ищем в массиве комбинаций платежей коробьями соответствия заданному объему хлеба
    answer = argwhere(condition)
    list_filtered = []
    for i in answer:    # подобно фильтрации индексов массивов для поиска денежной суммы, здесь отбрасываем все случаи,
        # когда индексы разных элементов группы совпадают, потому что фактически это означает принадлежность обеж двух
        # сравниваемых групп к одной группе - что является другим случаем.
        # print(i)
        if len(i) == len(set(i)):
            for num, j in enumerate(i):
                x = norma_corob[j]
                i = float32(i)
                i[num] = x
            list_filtered.append(i)
    return list(map(tuple, list_filtered))


def match_corob():  # подбирает все комбинации коробей разных групп, дающих в сумме заданное число коробей.
    # Не реализована генерация всех возможных сочетаний разных вариантов одного сорта хлеба с другими сортами
    # rozh_answers = []
    # oves_answers = []
    # pshen_answers = []
    # yachm_answers = []
    for num, i in enumerate(templates_all_combs):  # одна итерация - это вызов нескольких (по числу групп обеж)
        # одномерных массивов, представляющих нормы хлебных платежей безотносительно к сорту хлеба. Все итерации -
        # это все возможные комбинации групп обеж, дающие в сумме заданный обежный оклад
        # print(i)
        myarray = sum(arrays_to_axis(i))    # здесь мы суммируем коробьи по всем осям и получаем все комбинации,
        # среди которых можно искать заданный объем хлеба
        # print(myarray)
        rozh = 16.25  # float32(input(f'Число коробей ржи: '))
        oves = 21  # float32(input(f'Число коробей овса: '))
        pshen = 2.5  # float32(input(f'Число коробей пшеницы: '))
        yachm = 5.5  # float32(input(f'Число коробей ячменя: '))

        # костыль для проверки. здесь надо сделать цикл на ввод числа коробей,
        # ограничить его четырьмя значениями и на каждом шаге искать в массиве подходящее число
        rozh_ans = search_corob(myarray, rozh)
        oves_ans = search_corob(myarray, oves)
        pshen_ans = search_corob(myarray, pshen)
        yachm_ans = search_corob(myarray, yachm)
        # print(type(rozh_ans))
        # mylist_ans = [rozh_ans, oves_ans, pshen_ans, yachm_ans]
        print(f'Итерация {num}\n Нормы ржи: {rozh_ans}; Нормы овса: {oves_ans}; Нормы пшеницы: {pshen_ans}; Нормы ячменя: {yachm_ans}')
        # array_corobs = arrays_to_axis(mylist_ans)
        # print(array_corobs)
        # rozh_answers.append(rozh_ans)
        # oves_answers.append(oves_ans)
        # pshen_answers.append(pshen_ans)
        # yachm_answers.append(yachm_ans)
    # test = [oves_answers]
    # print(test)
    #     print(f'Все комбинации одной итерации: {mylist}')
        # print(f'Рожь одной итерации {rozh_answer}')


match_corob()

mytuple = int(input(f'С какой комбинацией обеж будем работать? Ввести номер от 0 до {len(combins_obj)-1}: '))
length = len(combins_obj[mytuple])
rows_count = len(norma_corob)

print(vars_one_tuple(mytuple))
# print(four_dim.itemsize)
# print(f'Сумма коробей на один вариант комбинации обеж: {match_corob()}')

four_dim = None

# set_printoptions(threshold=300000)

# cProfile.run('calc()')
#
