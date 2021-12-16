#  1) Для каждой пары городов двумерная матрица. По осям: варианты длины а) большой полуоси эллипсоида; б) малой полуоси
#  эллипсоида/ Каждый вариант должен быть зарегистрирован в spatial_ref_sys БД постгис как отдельная SRID. На нее нужно
#  будет потом ссылаться в запросе при определении расстояний между двумя точками, определяемыми по координатам;
#  2) В ячейках записи - значение расстояний на эллипсоиде между парой точек;
#  3) (?) Сортировка по близости к реальным значениям расстояний;
#  4) Наложение полученных нечетких множеств, характеризующих все пары городов и анализ результата.

import numpy as np
from numpy import ix_, array, arange, argwhere, array_split, set_printoptions, unique, intersect1d
import psycopg2
import json

semi_major_axis_min = 4500001 # 5729137  # это значение взято как равное малой полуоси +1 (избегаем деления на 0)
semi_major_axis_max = 7500001 # 7161973  # это значение взято как равное малой полуоси +1 (избегаем деления на 0)
semi_minor_axis_min = 5500000  #- это значение округленно соответствует длине градуса широты в 100 км
semi_minor_axis_max = 7500000  # это значение округленно соответствует длине градуса широты в 125 км
axis_step = 10000  # изменение длины малой полуоси на 50 км ведет к увеличению длины одного градуса широты менее чем
# на  1 км. Но для того, чтобы попадались значения сжатия, близкие к современному, нужно брать сильно меньше. 5000.
# Число найденных значений, естественно, увеличивается с уменьшением шага. Но если при заданном значении scope
# ничего не нашлось при шаге 15000, то не будет ничего и при шаге 5000. Так что для поиска соответствий расстояний
# между городами нужно менять в первую очередь scope.
# ins = 6378137
axis_a_range = arange(semi_major_axis_min, semi_major_axis_max, axis_step, dtype=int)  # это варианты длины полуоси (м)
length_x = len(axis_a_range)
axis_b_range = arange(semi_minor_axis_min, semi_minor_axis_max, axis_step, dtype=int)  # это варианты длины полуоси (м)
length_y = len(axis_b_range)
axis_y, axis_x = np.ix_(axis_b_range, axis_a_range)  # создаем двумерный массив,
    # по одной оси - возможные размеры большой полуоси, по другой - малой
# print(axis_x[0][223])
template = 1/((axis_x - axis_y)/axis_x)  # в шаблон записываем коэффициент полярного сжатия 1/f, где f - полярное сжатие
# templ_test = f'{1/((axis_x[0][223]-axis_y[62][0])/axis_x[0][223])}'
# print(templ_test)
set_printoptions(edgeitems=100, precision=9)  # параметры вывода в консоль
# print(axis_x[0][223], axis_y[62][0])

# def inverse_flattening():


conn = psycopg2.connect(f"dbname='base' user='npkfrolov' password='123308' host='127.0.0.1' port='5432'")
print("Database opened successfully")
cur = conn.cursor()
cur.execute('SELECT * FROM arabs.abu_meditterenian_calc_saidsaid WHERE p1_fid < p2_fid')
dbrecords_calc = cur.fetchall() # [x for x in cur.fetchall() if x[1]=='Махдия' and x[2]=='Толмейта']
# print(dbrecords_calc)
scope = 0.0862  # от этого параметра зависит, какие пары городов будут участвовать в результате в поисках общих параметров
# эллипсоида. Анализ распределения минимальных значений расхождения расстояний с реальными (на основе естественных
# интервалов Дженкса) не очень точно характеризует релевантность данных, поскольку не учитывает ту долю, которую
# составляет расхождение от реального расстояния между городами. Поэтому вместо этого на интервалы Дженкинса разбивался
# ряд значений соотношения разницы между расстояниями к реальному расстоянию. Из 171 пары в 113 (более 66%) расхождения
# могут не превышать 12,72%.

options = {}  # сюда собираем результаты для дальнейшей обработки

for row in dbrecords_calc:  # по строкам БД, в строке одна пара городов
    first_point = row[1]
    second_point = row[2]
    first_fid = row[8]
    # first_fid = row[12]
    second_fid = row[9]
    # second_fid = row[13]
    pairs = first_point + ' - ' + second_point
    long_pl_deg1 = row[13]+row[14]/60 # переводим угловые градусы в десятичные,с которыми работает постгис
    # long_pl_deg1 = row[18]+row[19]/60 # переводим угловые градусы в десятичные,с которыми работает постгис
    lat_pl_deg1 = row[15]+row[16]/60
    # lat_pl_deg1 = row[20]+row[21]/60
    long_pl_deg2 = row[17]+row[18]/60
    # long_pl_deg2 = row[22]+row[23]/60
    lat_pl_deg2 = row[19]+row[20]/60
    # lat_pl_deg2 = row[24]+row[25]/60
    point1 = f'POINT({long_pl_deg1} {lat_pl_deg1})'
    point2 = f'POINT({long_pl_deg2} {lat_pl_deg2})'
    distance = row[6]
    # print(point1, point2)
    matrix = []  # сюда отправляем все списки с результатами измерений расстояний по всем вариантам большой полуоси

    for ind, el in enumerate(template):  # перебираем варианты длины большой полуоси для каждого значения малой,
        # обращаясь по индексу к списку вариантов
        row_x = []  # сюда собираем результаты измерений постгис на заданном эллипсоиде
        # print(ind, el)
        for num, x in enumerate(el):
            semi_major_axis = int(axis_a_range[num])
        #     print(ind, semi_major_axis)
            # for fl in el:  # перебираем варианты коэффициента полярного сжатия внутри одного варианта длины большой полуоси
            # print(f'{ind}) {pairs}: {fl}')
            cur.execute('''SELECT ST_distanceSpheroid(ST_GeomFromText(%s), ST_GeomFromText(%s), 'SPHEROID["USER",%s,%s]')''', (point1, point2, semi_major_axis, el[num]))
            dbrecords_distances = cur.fetchall()
            row_x.extend(*dbrecords_distances)  # отправляем результаты измерений в список, общий для одного варианта
            # длины большой полуоси
            # if pairs == 'Махдия - Толмейта':
            #         if int(524000<dbrecords_distances[0][0])<544000:
            # print(f'{pairs}:{semi_major_axis}/{el[num]}:{dbrecords_distances}, {point1}/{point2}')
        # print(row_x)
        matrix.extend(row_x)

    # for numb, matr in enumerate(matrix):
    #     print(numb,matr)
    arr = array(matrix, dtype=float).reshape(length_y, length_x)  # это матрица измерений на экспериментальном сфероиде
    diff_share = (arr - distance)/distance  # значение из каждой ячейки матрицы делим на реальные расстояния между соответствующими
    # print(f'{arr[1][1]}')
    # if abs(diff_share[62][223]) < scope:
    #     print(diff_share[62][223], axis_a_range[223], axis_b_range[62],template[62][223])
    # городами, чтобы не просто вычислить разницу, но оценить, какую долю эта разница составляет от расстояния между
    # пунктами

    #diff_min = abs(diff_share).min()
    #SQL = "INSERT INTO arabs.abu_meditterenian_said_diffs (first_point, second_point, shares) VALUES (%s, %s, %s);"
    #data = (first_point, second_point, diff_min)
    #cur.execute(SQL, data)  # такое решение помогает избежать SQL-инъекций
    #conn.commit()  # этот блок для заполнения БД значениями минимальных расхождений

    # print(f'{pairs}: {abs(diff_share).min()}')
    filtered = argwhere(abs(diff_share) < scope)  # отбираем индексы только тех ячеек, в которых значения меньше выбранного
    # порога. Поленился переделывать код, но в нынешнем виде код требует редактирования для выполнения всего
    # алгоритма. Селект из таблицы calc должен забирать данные о минимальной доле расхождений, но это поле
    # генерируется по результатам обработки данных на основании таблицы calc. По-правильному нужно создавать еще одну
    # вьюшку, объединяющую calc и shares, и для расчета множеств работать уже с ней
    # matchlist = []  # сюда собираем кортежи из пар (длина большой полуоси, длина малой полуоси) одной пары городов
    # print(filtered)
    for j in filtered:  # перебираем все отобранные варианты индексов и по ним находим значения длин полуосей
        filt_x = int(axis_a_range[j[1]])
        filt_y = int(axis_b_range[j[0]])
        # print(f'{j}:{axis_a_range[j[1]]}:{axis_b_range[j[0]]}')
        SQL = "INSERT INTO arabs.coords_python_saidsaid (first_city, second_city, major_semi_axis, minor_semi_axis, scope) VALUES (%s, %s, %s, %s, %s);"
        data = (first_fid, second_fid, filt_x, filt_y, scope)
    #     # print(type(first_fid), type(second_fid), type(filt_x), type(filt_y), type(scope))
        cur.execute(SQL, data)  # такое решение помогает избежать SQL-инъекций
        conn.commit()  # завершаем транзакцию после записи всех инсертов
    print(f'Данные о параметрах городов {pairs} отправлены в БД')


                    # match = (int(filt_x), int(filt_y))  # собираем кортеж из пары значений длин полуосей
                    # matchlist.append(match)
                    # print(f'{pairs}: {len(matchlist)}')
                # places = {pairs: matchlist}  # делаем словарь, где ключом указываем пару городов, значением все кортежи
                # print(places)
                # if len(matchlist):  # в общий словарь отправляем только те ключи, которые содержат  какие-то кортежи
                #     options.update(places)

                    # print(mystr)

                # print(len(list(options.values())[0]))
                # print(f'{pairs}: {arr[0, 1]} / {result[0, 1]}')
                # print(array(matrix, dtype=float))
                # print(f'{pairs} done')

                # with open(f'/home/alexey/Документы/Google_disk/Тексты/АбулФида_2021/array.json', 'w') as file:
                #     json.dump(options, file)   # выгружаем результат в джейсон
