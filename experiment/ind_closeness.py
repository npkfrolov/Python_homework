import itertools
import json
import operator
from contextlib import closing
import ast

import psycopg2

with closing(psycopg2.connect(f"dbname='Base' user='npkfrolov' password='123308' host='127.0.0.1' port='5432'")) \
        as conn:
    # print("Database opened successfully")
    cur = conn.cursor()
    cur.execute('''SELECT fid, toponym FROM arabs.abu_meditterenian_places;''')
    result = cur.fetchall()
    places = {}
    # print(result)
    for i in result:
        places.update({i[0]:i[1]})
    # print(places)
mydict = {}

with open("/home/alexey/Загрузки/cwf_generated.json", 'r', encoding='utf-8-sig') as jsonfile:
    data = json.loads(jsonfile.read())['foo']
    # print(data)
    # presented = []
    for el in data:
        level = list(el.items())[0][0]
        # print(level)
        figures = list(el.items())[0][1]
        # print(figures.values())
    #     mylist = list(*figures)
    #     # super_dict = {key:val for d in mylist for key,val in d.items()}
    # # print(data[0])
    #     for d in figures:
    #         print(d)
        sorted_list = sorted(figures.items(), key=operator.itemgetter(1), reverse=True)
            # if level[0]=='2':
        # print(sorted_list)
    #     # cleared_str = "".replace('(', '').replace(')', '') #.split(', ') # join(c for c in sorted_list[0][0]. if c.isdecimal())
    #         print(sorted_list)
    #     mylist = []
        filtered_tuples = [el for i, el in enumerate(sorted_list) if sorted_list[i][1]==sorted_list[0][1]]
        koef = {sorted_list[0][1]: [el[0] for y, el in enumerate(filtered_tuples)]}
        print(f'{level}: {koef}')
        # print(filtered_tuples)


#         for i in ast.literal_eval(filtered[0][0]):
#             mylist.append(places[i])
#         rows = {tuple(mylist):sorted_list[0][1]}
#         # mydict.update(rows)
# # sorted_by_length = sorted(mydict.items(), key=operator.itemgetter(0))
#         print(str(rows).replace('{', '').replace('}', ''))
#         #     city = places[i]
#         #     presented.append(city)
#         # print(presented)
#         print(f'{level[0]}; {sorted_list[0][0]}; {sorted_list[0][1]}')
        # if int(level[0]) == 16:
        #     print(sorted_list)
        # print(figures)