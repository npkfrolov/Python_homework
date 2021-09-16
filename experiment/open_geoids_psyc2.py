import multiprocessing
from concurrent.futures import ThreadPoolExecutor
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
digit = 8
cpu = int(multiprocessing.cpu_count()/2)
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
    with closing(psycopg2.connect(f"dbname='Base' user='npkfrolov' password='123308' host='127.0.0.1' port='5432'")) \
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
        list_combi = list(combi)
        data = (list_combi, list_combi)
        print(data)
        cur.execute(SQL, data)  # такое решение помогает избежать SQL-инъекций
        # conn.commit()
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

    with ThreadPoolExecutor() as pool:
        for i in comb_list:
            pool.map(sql, i.myset)

        # first = combins[::8]
        # second = combins[1::8]
        # third = combins[2::8]
        # forth = combins[3::8]
        # fifth = combins[4::8]
        # sixth = combins[5::8]
        # seventh = combins[6::8]
        # eights = combins[7::8]
        # # even = [combi for ind, combi in enumerate(combins) if ind%2]
        # if __name__ == '__main__':
        #     # start 4 worker processes
        #     with ThreadPoolExecutor() as pool:
        #         pool.map(sql, first)
        #         pool.map(sql, second)
        #         pool.map(sql, third)
        #         pool.map(sql, forth)
        #         pool.map(sql, fifth)
        #         pool.map(sql, sixth)
        #         pool.map(sql, seventh)
        #         pool.map(sql, eights)


    # with concurrent.futures.ThreadPoolExecutor(max_workers=cpu) as executor:
    #     # Start the load operations and mark each future with its URL
    #     future_to_url = {executor.submit(sql, obj.myset): obj for obj in comb_list}
    #     for future in concurrent.futures.as_completed(future_to_url):
    #         combi = future_to_url[future]
    #         try:
    #             data = future.result()
    #         except Exception as exc:
    #             print('%r generated an exception: %s' % (combi, exc))
            # else:
            #     print('%r page is %d bytes' % (combi, len(data)))

with open("/home/alexey/Загрузки/Fida_closeness_test.json", 'a', encoding='utf-8') as jsonfile:  # запись в json
    json.dump(coeff_all_digits, jsonfile)
    # writer.writerows(digit_dict)
    jsonfile.write('\n')
    print("Готово. Записано в файл")

finish_time = time.time()
duration = (finish_time - start_time) / 60
print(f'duration: {duration}')

# print(coeff_all_digits)

