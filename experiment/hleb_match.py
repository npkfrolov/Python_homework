import array
import cProfile
from threading import Thread
from operator import itemgetter
import itertools
import timeit
import operator
import numpy as np

rozh_price = 10
oves_price = 5
pshen_price = 14
yachmen_price = 7
look_for_match =  352 # float(input('Соответствие какой сумме мы ищем (в деньгах)?'))
obji_count = 11  # float(input('Сколько обеж у нас есть?'))
obj_step = 0.5
corob_step = 0.25
scope_na_obju = 3
list_obj = np.arange(obj_step, obji_count+obj_step, obj_step, dtype=np.float16)  # это варианты количества обеж, платящих хлебный оброк
combins_obj = []
components = list_obj
divisor = obji_count / obj_step
# mylist = itertools.accumulate(components)

for j in range(int(obji_count/2)+2):  # range(4):
    mylist = [i for i in list(itertools.combinations(components, j)) if sum(i) == obji_count]  # делаем список всех
    # вариантов деления обеж на группы, в сумме дающих известное число обеж владения
    combins_obj.extend(mylist)

print(f'Комбинации обеж: {combins_obj}')

# def dengi(dengi_hleb):  # функция превращает список в словарь, который нужен для ускорения расчетов и фиксации позиции
#     # значения в таблице расчетов
#     mydict = {}
#     for ind, summ in enumerate(dengi_hleb.flat):
#         if summ <= look_for_match: # нет смысла обрабатывать значения, превышающие суммарное значение денег за хлеб
#             temp = {ind:summ}
#             mydict.update(temp)
#     return dict(sorted(mydict.items(), key=itemgetter(1)))  # это позволит на следующем шаге ограничить расчеты суммами,
    # не больше искомой

norma_corob = np.arange(corob_step, scope_na_obju, corob_step, dtype=np.float16)  # это варианты нормы (в коробьях хлеба),
# по которой дается хлеб с одного варианта количества обеж
# print(norma_corob.ndim)

def dengi_sort_hleb(price):
    template_summ_cor = np.array([])
    for i in template:
        summ = sum(i)*price
        template_summ_cor = np.append(template_summ_cor, summ)
    # sorted_data = template_summ_cor.sort(axis=0)
        # if summ <= look_for_match:
        #     i = {summ : tupl}  # пока не стал мучиться дальше, чтобы вывести заодно и норму хлеба с соотвтствующих обежных групп
        #     template_summ_cor = np.append(template_summ_cor, i)
    inds = np.array([el for el in template_summ_cor])
    sort_inds = np.argsort(inds)
    sorted_data = [template_summ_cor[ind] for ind in sort_inds]
    # keys = np.array([el.keys() for el in template_summ_cor])
    # print(keys)
    # sort_inds = np.argsort(keys)
    # print(sort_inds)
    # sorted_data = [template_summ_cor[key] for key in sort_inds]
    # sort_arr = map(lambda x: x.keys(), template_summ_cor)
    # print(sort_arr)
    # print(f'Сортированный массив: {sorted_data}')
    # template_summ_cor = template_summ_cor[np.argsort(sort_arr)]
    # return  template_summ_cor
    return  sorted_data
    # print(f'Сортированный массив: {template_summ_cor}')


for num, tupl in enumerate(combins_obj): # перебираем кортежи, представляющие варианты группировки обеж исследуемого владения
    # print(len(combins_obj))
    length = len(tupl)
    # vars_norms_groups = np.array(list(map(list, itertools.combinations(norma_corob, length))))  # выбираем все возможные варианты сочетания применения разных норм к разным группам обеж
    # print()
    combins_obj_arr = np.array(tupl, dtype=np.float16)
    # print(combins_obj_arr)
    norma_corob_ax, combins_obj_arr_ax = np.ix_(norma_corob, combins_obj_arr)
    template = norma_corob_ax*combins_obj_arr_ax  # шаблон получаем, умножив поэлементно норму платежа на число обеж в группе.
    # Теперь можно транслировать его на матрицы сортов хлеба и суммировать деньги
    columns_count = template.shape[1]
    template_list = np.array_split(template, columns_count, axis=1)
    # print(template_nd)
    template_accum = []
    for ind, i in enumerate(template_list):
        flat_arr = i.flat
        template_accum.append(np.array(flat_arr))
        list_of_table = [1] * columns_count
        # print(list_of_table)
        list_of_table[ind] = template.shape[0]
        # print(list_of_table)
        template_zeros = np.zeros(list_of_table, dtype=np.float16)
        # print(template_zeros)
        arr_summ_cor = template_zeros+flat_arr
        # print(f'Многомерный массив для сложения в кортеже {tupl}: {arr_summ_cor}')
        # template_accum.append(arr_summ_cor)
    # print((f'Многомерный массив для сложения в кортеже {tupl}:{sum(template_accum)}'))
    template_nd = np.zeros([columns_count])
    if length == 1: # это костыль галимый, но не могу придумать, как сгенерировать неизвестный заранее ряд переменных
        # в левой части выражения
        template_nd = np.array(*template_accum)
        # print(type(template_nd))
    elif length == 2:
        a, b = np.ix_(*template_accum)
        template_nd = a + b
        # print(template_nd)
    elif length == 3:
        a, b, c = np.ix_(*template_accum)
        template_nd = a + b + c
        # print(template_nd)
    elif length == 4:
        a, b, c, d = np.ix_(*template_accum)
        template_nd = a + b + c + d
        # print(template_nd)
    elif length == 5:
        a, b, c, d, e = np.ix_(*template_accum)
        template_nd = a + b + c + d + e
        # print(template_nd)
    elif length == 6:
        a, b, c, d, e, f = np.ix_(*template_accum)
        template_nd = a + b + c + d + e + f
        # print(template_nd)
    elif length == 7:
        a, b, c, d, e, f, h = np.ix_(*template_accum)
        template_nd = a + b + c + d + e + f + h
    # print(f'Суммы платежей за рожь со всех обеж: {(template_nd * rozh_price)}')
    # print(f'Многомерный шаблон, все возможные варианты суммирования платежей хлебом одного сорта разных групп обеж: {template_nd}')
    # template = vars_norms_groups*tupl
    # print(columns_count)
    # print(f'Кортеж обеж {num}: Суммарное количество хлеба со всех групп и распределение коробей по группам обеж {template_summ_cor}')
    table_rozh = template_nd.copy()*rozh_price  # dengi_sort_hleb(rozh_price)
    table_oves = template_nd.copy()*oves_price  # dengi_sort_hleb(oves_price)
    table_pshen = template_nd.copy()*pshen_price  # dengi_sort_hleb(pshen_price)
    table_yachm = template_nd.copy()*yachmen_price  # dengi_sort_hleb(yachmen_price)

    # vars_dengi = np.array(list(map(list, itertools.combinations_with_replacement(table_rozh, 4))))
    print(f'Варианты платежей с владения за рожь: {table_rozh}')
    four_dim = table_rozh + table_oves + table_pshen + table_yachm
    # print(type(four_dim))
    # print(f'{i} - {row*tupl[i]} ')
        # row = row * tupl[i]
        # template = hleb_from_groups
        # print(hleb_from_groups)
        # print(f'Платежи хлебом в группе: {tupl}:{i}): {template}')
    # np.set_printoptions(threshold=300000)
    # np.set_printoptions(edgeitems=20)
    # print(f'{num} - Варианты сочетания применения разных норм к разным группам обеж: {vars_norms_groups.shape}')
    # print(f'{num} - Варианты платежа разного объема хлеба разными группами обеж: {template.size}')


    # print(f'{num} - Суммарный платеж за хлеб разными группами обеж: {table_rozh}')
    # print(table_rozh+table_oves)

    # arr1 = np.array(table_rozh, dtype=np.float16)
    # arr2 = np.array(table_oves, dtype=np.float16)
    # arr3 = np.array(table_pshen, dtype=np.float16)
    # arr4 = np.array(table_yachm, dtype=np.float16)
    # arr1n, arr2n, arr3n, arr4n = np.ix_(arr1, arr2, arr3, arr4)
    # result = arr1n+arr2n+arr3n+arr4n
    indx = four_dim == look_for_match
    answer = np.argwhere(indx)

    # print(f'Совпадения по сумме денег, группа обеж {tupl}: {answer}')
#     print(arr1.itemsize)
        # print(f'Перемножение на число обеж: {hleb_from_groups}')
    # print(f'Варианты нормы в коробьях в разных группах: {templ_norm_group}')
    # axes_obj_corob = []  # сюда записываем ряды, образованные умножением нормы хлеба на число обеж в группе -
    # # оси будущего многомерного массива
    # for group in tupl:
    #     combins_obj_cor = group*norma_corob  # это шаблон, на значения которого можно перемножать цены конкретного
    # # сорта хлеба, чтобы вычислять варианты сумм платежей
    #     axes_obj_corob.extend(list(combins_obj_cor))
    # matrix_obj_corob = np.array(axes_obj_corob)
    # # print(axes_obj_corob)
    # print(matrix_obj_corob.size)

        # print(f'Шаблон платежа хлебом по всему спектру норм для отдельной группы обеж: {combins_obj_cor}')
# print(type(combins_obj_cor))

# list_cor_oves = np.arange(corob_step, scope_na_obju, corob_step)
# list_cor_pshen = np.arange(corob_step, scope_na_obju, corob_step)
# list_cor_yachmen = np.arange(corob_step, scope_na_obju, corob_step)
# dengi_rozh = dengi(np.outer(list_cor*rozh_price, list_obj))  # внешнее произведение векторов дает все возможные
# # варианты сумм денег, которые начисляются за хлеб определенного сорта по всем вариантам норм с разного числа обеж.
# dengi_oves = dengi(np.outer(list_cor*oves_price, list_obj))
# dengi_pshen = dengi(np.outer(list_cor*pshen_price, list_obj))
# dengi_yachmen = dengi(np.outer(list_cor*yachmen_price, list_obj))


# print(f'Варианты платежей за хлеб с каждого элемента группы обеж одной волостки: {matrix_rozh}')

# summ_volostka_rozh = []  # данные о вариантах платежей всех групп обеж всех кортежей (по одной волостке)
#
# for l in matrix_rozh: # l - один из вариантов деления волостки на группы обеж, платящих одинаково (кортеж)
#     length = len(l)       # найдем число групп обеж волостки ( длину кортежа)
#     long = len(l[0])    # узнаем число вариантов хлебных платежей по числу вариантов платежей нулевой группы
#     array_summ_tuple_rozh_var = []  # сюда складываем все возможные сочетания сумм платежей нескольких групп обеж одного
#     # сорта хлеба внутри одного кортежа
#     if length == 1:  # если кортеж состоит всего из одной группы обеж
#         array_summ_tuple_rozh_var.append(list(l[0]))  # если все обжи платят по одной норме, то матрица будет одномерной,
#         # платежи этой группы полностью совпадают с деньгами единственного элемента
#     else:  # если групп больше, берем первую группу и добавляем к ней деньги второй
#         for m in range(long):  # перебираем варианты платежей с первой группы обеж
#             array_for_member = []  # создадим пустой список для складирования всех вариантов суммирования платежей
#             # одного варианта нулевой группы обеж с разными вариантами платежей остальных групп обеж
#             for n in range(long):  # пробегаем по каждой группе обеж, начиная с 1, прибавляя один из вариантов платежа
#                 # к платежу 0-й группы
#                 summ_for_member = l[0][m]  # сюда собираем результат суммирования одного из вариантов платежей из всех групп обеж
#                 for k in range(length - 1):  # количество итераций зависит от того, сколько в наборе групп обеж
#                     # if n == m:  # нет смысла брать варианты использования одной нормы коробей для разных групп обеж,
#                     # #потому что этот случай учтен в другой группе обеж - которая их объединяет по одной норме
#                     #     summ_for_member = None
#                     # else:
#                     summ_for_member += l[k+1][n]
#                         # array_for_member.append(summ_for_member)  # += l[k+1][n]  # увеличиваем сумму
#                     # print(summ_for_member)
#                 array_for_member.append(summ_for_member)
                # print(array_for_member)
            # summ_volostka_rozh_var.append(array_for_member)

#             summ = chain[m]+target[t]
#     summ_volostka_rozh.append(summ)
# print(summ_volostka_rozh_cell)
# print(np.array(l[0]))
# print(f'Суммы за сорт хлеба со всех групп обеж волостки {summ_volostka_rozh_var}')

# matrix = np.array([dengi_rozh+dengi_oves], dtype=float)
# matrix = np.array([dengi_rozh], float)
# print(matrix_obj_corob)
# print(list_obj)
# print(matrix_obj_corob.shape)
# operations = len(dengi_rozh)*len(dengi_oves)*len(dengi_pshen)*len(dengi_yachmen)
# print(operations)
# print(mydict)

# def calc(dict1, dict2, name1, name2):
#     summ_dicts = {}
#     for keya, valuea in dict1.items():
#         for keyb, valueb in dict2.items():
#             newkey = f'{name1}.{keya}.{name2}.{keyb}.'
#             result = valuea + valueb
#             if result <= look_for_match:
#                 newdict = {newkey: result}
#                 summ_dicts.update(newdict)
#             else: continue
#     return summ_dicts
#
#
# def sorting(dict1, dict2, name1, name2):
#     return dict(sorted(calc(dict1, dict2, name1, name2).items(), key=itemgetter(1)))
#
# summ_r_o = sorting(dengi_rozh, dengi_oves, "r", "o")
# summ_p_y = sorting(dengi_pshen, dengi_yachmen, "p", "y")
# print(len(summ_r_o))
# print(len(summ_p_y))
#
#
# def hleb(r, o, p, y):
#     rozh = ((r % divisor) * corob_step + corob_step)
#     oves = ((o % divisor) * corob_step + corob_step)
#     pshen = ((p % divisor) * corob_step + corob_step)
#     yachmen = ((y % divisor) * corob_step + corob_step)
#     result = [rozh, oves, pshen, yachmen]
#     return result
#
#
# def transf_back(list):
#     addresses = [int(i) for j, i in enumerate(list) if j % 2]
#     ind_r = addresses[0]
#     ind_o = addresses[1]
#     ind_p = addresses[2]
#     ind_y = addresses[3]
#     transf = hleb(ind_r, ind_o, ind_p, ind_y)
#     return transf
#
# for keya, valuea in summ_r_o.items():
#     for keyb, valueb in summ_p_y.items():
#         if (valuea+valueb) == look_for_match:
#             addr = (keya + keyb).split('.')
#             match = transf_back(addr)
#             matches.append(match)
#         else: break

# # cProfile.run('calc()')
#
# print(matches)
# print(dict(sorted(dengi_rozh.items(), key=itemgetter(0))))
# print(dengi_rozh[346])
# print(dengi_oves[48])
# print(dengi_pshen[0])
# print(dengi_yachmen[0])
# print(f'{dengi_rozh[346]+dengi_oves[48]+dengi_pshen[0]+dengi_yachmen[0]}')

# записать в словарь  или сохранить в четыре таблицы, а потом их обсчитывать,