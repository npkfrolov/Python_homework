from multiprocessing import Pool,Process
import time
import json
from itertools import combinations
import csv
import psycopg2
from psycopg2.extensions import register_adapter, AsIs

# def inters(myset,  digit):  # функция принимает набор множеств и их количество, находит все пересечения
#         mystr = 'list(set.intersection('  # поскольку число множеств меняется, формируем строку, которую затем исполняем
#         # как код
#         for inx, el in enumerate(myset):
#                 if inx != 0:
#                         mystr += ', '
#                 mystr += f'set(myset[{inx}])'
#                 if inx == digit-1:
#                         mystr += '))'
#         res = eval(mystr)  # запуск строки как кода
#         return res

# with open(f'/home/alexey/Документы/Google_disk/Тексты/АбулФида_2021/array.json', 'r') as file:



#
#         if len(inter) > 0:  # печатаем, если нашелся хотя бы один кортеж, общий для всех множеств
#                 z += 1  # увеличиваем счетчик, чтобы остановить цикл,  когда ни одна комбинация множеств их
#                 # заданного числа не даст хотя бы одного пересечения
#                 report = f'{mykeys_comb[ind]}; большая ось больше; {len([m for m in inter if m[0]>m[1]])}:малая ось больше:{len([m for m in inter if m[0] < m[1]])}:оси равны:{len([m for m in inter if m[0] == m[1]])}:всего:{len(inter)}'
#                 csvwriter.writerow([digit, mykeys_comb[ind], len(inter), len([m for m in inter if m[0] > m[1]]), len([m for m in inter if m[0] < m[1]])])
#                 print(report)
#     if z == 0:
#         print(f'Дальнейший перебор вариантов не имеет смысла, '
#               f'ни одна из комбинаций {digit} множеств не дала пересечений')
#         # break
#
from numpy import array

conn = psycopg2.connect(f"dbname='Base' user='npkfrolov' password='123308' host='127.0.0.1' port='5432'")
print("Database opened successfully")
cur = conn.cursor()

mylist = [2, 3, 14, 15, 17, 18, 20, 22, 23, 24, 27, 30, 32, 33, 34, 35, 36, 42, 45]  # это список айдишников городов,
# который можно  сделать в виде запроса к БД, но быстрее захардкодить
my_result = []
mylength = len(mylist)
# print(f'mylength: {mylength}')
coeff_all_digits = {}


def addapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))


def minims(combi):
    # for ind, combi in enumerate(combins):
        SQL = '''SELECT max(aggr_sph.count_comb) 
   FROM (      
     SELECT aggr_pairs_all_said.cities_names,
            array_agg(aggr_pairs_all_said.count_pairs) AS count_pairs,
            aggr_pairs_all_said.count_pairs AS count_comb
           FROM            
              (SELECT aggr_cities.count_pairs,
                aggr_cities.cities_names
                    FROM                       
                      ( SELECT string_agg(wind_pairs.cities_names, '; '::text ORDER BY wind_pairs.cities_names) AS cities_names,
                              wind_pairs.count_pairs                            
                            FROM                             
                                ( SELECT count(*) OVER (PARTITION BY pairs_all_said.major_semi_axis, pairs_all_said.minor_semi_axis ORDER BY pairs_all_said.major_semi_axis, pairs_all_said.minor_semi_axis) AS count_pairs,
                                          pairs_all_said.major_semi_axis,
                                          pairs_all_said.minor_semi_axis,
                                          pairs_all_said.count,
                                          pairs_all_said.cities_names
                                        FROM                                         
                                                (SELECT allscopes.major_semi_axis,
                                                      allscopes.minor_semi_axis,
                                                      allscopes.count,
                                                      allscopes.cities_names
                                                      FROM 
                                                        ( SELECT sph.major_semi_axis,
                                                              sph.minor_semi_axis,
                                                              sph.scope,
                                                              count(*) OVER (PARTITION BY sph.major_semi_axis, sph.minor_semi_axis, sph.scope ORDER BY sph.major_semi_axis, sph.minor_semi_axis, sph.scope) AS count,
                                                              concat(( SELECT abu_meditterenian_places.toponym
                                                                      FROM arabs.abu_meditterenian_places
                                                                    WHERE abu_meditterenian_places.fid = sph.first_city), ' - ', ( SELECT abu_meditterenian_places.toponym
                                                                      FROM arabs.abu_meditterenian_places
                                                                    WHERE abu_meditterenian_places.fid = sph.second_city)) AS cities_names
                                                              FROM arabs.coords_python_saidsaid sph
                                                                JOIN arabs.abu_meditterenian_calc_saidsaid geom ON geom.p1_fid = sph.first_city AND geom.p2_fid =
                                                                sph.second_city AND (geom.p1_fid <> ALL (%s)) AND (geom.p2_fid <> ALL (%s))) 
                                                          AS allscopes
                                                    WHERE abs(allscopes.scope - 0.1397::double precision) < 0.01::double precision)                                                                                               
                                                  AS pairs_all_said)                                          
                                  AS wind_pairs
                            GROUP BY wind_pairs.major_semi_axis, wind_pairs.minor_semi_axis, wind_pairs.count_pairs
                            ORDER BY wind_pairs.major_semi_axis, wind_pairs.minor_semi_axis, wind_pairs.count_pairs) 
                        AS aggr_cities) 
              AS aggr_pairs_all_said
          GROUP BY aggr_pairs_all_said.cities_names, aggr_pairs_all_said.count_pairs
          ORDER BY aggr_pairs_all_said.cities_names) 
      AS aggr_sph;'''
        # combi = [2, 3]
        data = (list(combi), list(combi))
        # print(SQL)
        # print(f'data: {data}')
        cur.execute(SQL, data)  # такое решение помогает избежать SQL-инъекций
        # conn.commit()
        # SQL2 = '''SELECT max(count_comb) FROM arabs.aggr_spheres_all_said;'''
        # cur.execute(SQL2)
        result_int = cur.fetchone()[0]

        # print(f'result: {result}')
        # result_int = int(result[0])
        # print(f'result_int: {result_int}')
        coef = result_int / combi_count
        # print(f'coef: {coef}')
        # coef_for_digit.append({str(combi): coef})
        #
        # digit_dict = {digit: coef_for_digit}
        # print(coef_for_digit)
        # # coeff_all_digits.update(digit_dict)
        #
        # with open("/home/alexey/Загрузки/Fida_closeness_test.json", 'a', encoding='utf-8') as jsonfile:  # запись в json
        #     json.dump(digit_dict, jsonfile)
        #     # writer.writerows(digit_dict)
        #     jsonfile.write('\n')
        #     print("Готово. Записано в файл")

for digit in range(1, mylength-2):  # для последовательного исключения из общего списка всех возможных сочетаний
# городов разной длины, чтобы можно было менять вьюшку (нет смысла исключать все города и оставлять в выборке менее
# 3 городов)
    start_time = time.time()

    if __name__ == '__main__':

        rest_count = mylength-digit
        # print(f'rest_count: {rest_count}')
        combi_count = ((rest_count)**2 - rest_count)/2 # вычисляем количество уникальных  комбинаций городов после исключения
    # того числа, которое  берется на этой итерации
    #     print(f'combi_count: {combi_count}')
        combins = array(tuple(combinations(mylist, digit)), dtype=tuple)  # собираем все соответствующие комбинации наборов кортежей
        # print(f'combins: {combins}')
        # z = 0
        coef_for_digit = []
        matrix = minims(combins)
        print(matrix)
        # with Pool(8) as p:
        #     p.map(minims, combins)
        # p = Process(target=minims, args=combins)
        # p.start()
        # p.join()

    finish_time = time.time()
    duration = (finish_time-start_time)/60
    print(duration)

# print(coeff_all_digits)

