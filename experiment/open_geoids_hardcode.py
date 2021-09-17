from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, Process
import time
import json
from itertools import combinations
import csv
from multiprocessing.pool import ThreadPool

import psycopg2
from contextlib import closing
import concurrent.futures

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

mylist = [2, 3, 14, 15, 17, 18, 20, 22, 23, 24, 27, 30, 32, 33, 34, 35, 36, 42, 45]  # это список айдишников городов,
# который можно  сделать в виде запроса к БД, но быстрее захардкодить
my_result = []
mylength = len(mylist)
# print(f'mylength: {mylength}')
coeff_all_digits = {}

def sql(combi):
    # for combi in combin:
    with closing(psycopg2.connect(f"dbname='base' user='npkfrolov' password='123308' host='127.0.0.1' port='5432'")) \
            as conn:
        # print("Database opened successfully")
        cur = conn.cursor()
        conn.autocommit = True
        SQL = '''SET SESSION CHARACTERISTICS AS TRANSACTION READ ONLY; 
        SELECT max(aggr_sph.count_comb) 
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
        print(data)
        # print(SQL)
        # print(f'data: {data}')
        cur.execute(SQL, data)  # такое решение помогает избежать SQL-инъекций
        # conn.commit()
        # SQL2 = '''SELECT max(count_comb) FROM arabs.aggr_spheres_all_said;'''
        # cur.execute(SQL2)
        result = cur.fetchone()

        # print(f'result: {result}')
        result_int = int(result[0])
        # print(f'result_int: {result_int}')
        coef = result_int / combi_count
        # print(f'coef: {coef}')
        coef_for_digit.append({str(combi): coef})

        digit_dict = {digit: coef_for_digit}
        # print(coef_for_digit)
        coeff_all_digits.update(digit_dict)


def minims(combins):
    first = combins[::32]
    second = combins[1::32]
    third = combins[2::32]
    forth = combins[3::32]
    fifth = combins[4::32]
    sixth = combins[5::32]
    seventh = combins[6::32]
    eights = combins[7::32]
    more9 = combins[8::32]
    more10 = combins[9::32]
    more11 = combins[10::32]
    more12 = combins[11::32]
    more13 = combins[12::32]
    more14 = combins[13::32]
    more15 = combins[14::32]
    more16 = combins[15::32]
    more17 = combins[16::32]
    more18 = combins[17::32]
    more19 = combins[18::32]
    more20 = combins[19::32]
    more21 = combins[20::32]
    more22 = combins[21::32]
    more23 = combins[22::32]
    more24 = combins[23::32]
    more25 = combins[24::32]
    more26 = combins[25::32]
    more27 = combins[26::32]
    more28 = combins[27::32]
    more29 = combins[28::32]
    more30 = combins[29::32]
    more31 = combins[30::32]
    more32 = combins[31::32]
    # even = [combi for ind, combi in enumerate(combins) if ind%2]
    if __name__ == '__main__':
        # start 4 worker processes
        with ThreadPoolExecutor() as pool:
            pool.map(sql, first)
            pool.map(sql, second)
            pool.map(sql, third)
            pool.map(sql, forth)
            pool.map(sql, fifth)
            pool.map(sql, sixth)
            pool.map(sql, seventh)
            pool.map(sql, eights)
            pool.map(sql, more9)
            pool.map(sql, more10)
            pool.map(sql, more11)
            pool.map(sql, more12)
            pool.map(sql, more13)
            pool.map(sql, more14)
            pool.map(sql, more15)
            pool.map(sql, more16)
            pool.map(sql, more17)
            pool.map(sql, more18)
            pool.map(sql, more19)
            pool.map(sql, more20)
            pool.map(sql, more21)
            pool.map(sql, more22)
            pool.map(sql, more23)
            pool.map(sql, more24)
            pool.map(sql, more25)
            pool.map(sql, more26)
            pool.map(sql, more27)
            pool.map(sql, more28)
            pool.map(sql, more29)
            pool.map(sql, more30)
            pool.map(sql, more31)
            pool.map(sql, more32)


# for digit in range(1, mylength - 2):  # для последовательного исключения из общего списка всех возможных сочетаний
    # городов разной длины, чтобы можно было менять вьюшку (нет смысла исключать все города и оставлять в выборке менее
    # 3 городов)
digit = 8
start_time = time.time()

# if __name__ == '__main__':
rest_count = mylength - digit
# print(f'rest_count: {rest_count}')
combi_count = ((rest_count) ** 2 - rest_count) / 2  # вычисляем количество уникальных  комбинаций городов после исключения
# того числа, которое  берется на этой итерации
#     print(f'combi_count: {combi_count}')
combins = tuple(combinations(mylist, digit))  # собираем все соответствующие комбинации наборов кортежей
print(f'combins: {len(combins)}')
# z = 0
coef_for_digit = []
minims(combins)

with open("/home/alexey/Fida_closeness_new.json", 'a', encoding='utf-8') as jsonfile:  # запись в json
    json.dump(coeff_all_digits, jsonfile)
    # writer.writerows(digit_dict)
    jsonfile.write('\n')
    print("Готово. Записано в файл")

finish_time = time.time()
duration = (finish_time - start_time) / 60
print(duration)

# print(coeff_all_digits)

