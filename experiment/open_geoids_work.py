import multiprocessing
# from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, Process
import time
import json
from itertools import combinations
from multiprocessing.pool import ThreadPool

import psycopg2
from contextlib import closing
import concurrent.futures

mylist = [2, 3, 14, 15, 17, 18, 20, 22, 23, 24, 27, 30, 32, 33, 34, 35, 36, 42, 45]  # это список айдишников городов,
# который можно  сделать в виде запроса к БД, но быстрее захардкодить
my_result = []
mylength = len(mylist)
# print(f'mylength: {mylength}')
coeff_all_digits = {}
digit = 2 
cpu = 1 # int(multiprocessing.cpu_count()/2)
# print(cpu)
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
                                                            ( SELECT DISTINCT sph.major_semi_axis,
                                                                  sph.minor_semi_axis,
                                                                  sph.scope,
                                                                  (count(*) OVER (PARTITION BY sph.major_semi_axis, 
                                                                  sph.minor_semi_axis, sph.scope ORDER BY 
                                                                  sph.major_semi_axis, sph.minor_semi_axis, sph.scope))/2 AS count,
                                                                  concat(( SELECT abu_meditterenian_places.toponym
                                                                          FROM arabs.abu_meditterenian_places
                                                                        WHERE abu_meditterenian_places.fid = sph.first_city), ' - ', ( SELECT abu_meditterenian_places.toponym
                                                                          FROM arabs.abu_meditterenian_places
                                                                        WHERE abu_meditterenian_places.fid = sph.second_city)) AS cities_names,
                                                                    sph.first_city,
                                                                    sph.second_city
                                                                  FROM arabs.coords_python_saidsaid sph
                                                                    JOIN arabs.abu_meditterenian_calc_saidsaid geom ON geom.p1_fid = sph.first_city AND geom.p2_fid =
                                                                    sph.second_city AND (geom.p1_fid <> ALL (%s)) AND (geom.p2_fid <> ALL (%s))) 
                                                              AS allscopes
                                                        WHERE abs(allscopes.scope - 0.0862::double precision) < 0.01::double precision)                                                                                               
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
        list_combi = list(combi)
        data = (list_combi, list_combi)
        print(list_combi)
        cur.execute(SQL, data)  # такое решение помогает избежать SQL-инъекций
        # conn.commit()
        result = cur.fetchone()

      #  print(f'result: {result}')
        if result[0] != None:
            result_int = int(result[0])
        # print(f'result_int: {result_int}')
            coef = result_int / combi_count
        # print(f'coef: {coef}')
        else:
            coef = 0

        digit_dict.update({str(combi): coef})
        # coef_for_digit.append({str(combi): coef})
        # digit_dict = {digit: coef_for_digit}
        # print(coef_for_digit)
        # coeff_all_digits.update(digit_dict)
        

# for dig in range(digit, mylength-2):

digit_dict = {}

class Thread:
    tread_count = 0
    def __init__(self, combins):
        self.myset = combins[Thread.tread_count::cpu]
        Thread.tread_count += 1

if __name__ == '__main__':
    comb_list = []
    for el in range(cpu):
        obj = Thread(combins)  # чтобы не хардкодить  каждый раз потоки по числу ядер процессора, создаются объекты
        # потока в соответствующем количестве
        # print(obj)
        comb_list.append(obj)
        # print(comb_list[el].myset)   # minims(combins, mycount)
    # print(comb_list)

    with ThreadPool() as pool:
        for i in comb_list:
            if len(i.myset)>0:
                pool.map(sql, i.myset)

tojson = {digit: digit_dict}

with open("/home/alexey/Fida_closeness_correct.json", 'a', encoding='utf-8') as jsonfile:  # запись в json
    json.dump(tojson, jsonfile)
    # writer.writerows(digit_dict)
    jsonfile.write('\n')
    print("Готово. Записано в файл")

finish_time = time.time()
duration = (finish_time - start_time) / 60
print(f'duration: {duration}')

# print(coeff_all_digits)
