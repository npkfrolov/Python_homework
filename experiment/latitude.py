# в расчетах участвуют все отрезки, то есть не только A-B, но и B-A. Если же отбрасывать один из этих вариантов
# по условию разница меридианов >= или > 0, то при значении 0 мы либо дважды считаем значение (в первом случае),
# либо ни разу не считаем (во втором). Удвоение вариантов, однако, никак не влияет на расчеты, поскольку отклонение
# от азимута реального у каждого из двух отрезков одинаковое.

import math
import psycopg2
from operator import itemgetter
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# pswd = input('Нужно ввести пароль: ')
conn = psycopg2.connect(f"dbname='Base' user='npkfrolov' password='123308' host='127.0.0.1' port='5432'")
print("Database opened successfully")
cur = conn.cursor()
cur.execute('SELECT * FROM arabs.abu_meditterenian_calc')
dbrecords_calc = cur.fetchall()

pairs = [j[1] + '-' + j[2] for j in dbrecords_calc]
# print(f"pairs: {pairs}")
minutes_lat_diff = [abs(j[3]) for j in dbrecords_calc]  # чтобы в качестве первого города были представлены все города
# (это нужно для регрессии), пришлось в коде вьюшки убрать выборку только положительных или равных нулю значений,
# а здесь оперировать модулем разницы. В результате в расчетах участвует по два идентичных отрезка, просто развернутые
# относительно друг друга на 180 градусов (A-B и B-A). Но на статистику это не влияет
# print(f"minutes_lat_diff: {minutes_lat_diff}")
minutes_long_diff = [abs(j[4]) for j in dbrecords_calc]  # аналогично широтам
# print(f"minutes_long_diff: {minutes_long_diff}")

st_azimuth = [j[5] for j in dbrecords_calc]
st_distance = [j[6] for j in dbrecords_calc]
min_meridian = 50000
max_meridian = 150000
meridian_step = 1000

cur.execute('SELECT * FROM arabs.abu_meditterenian_said ORDER BY toponym')
dbrecords_points = cur.fetchall()
placenames = dict.fromkeys([j[1] for j in dbrecords_points], [])
# print(f"placenames: {placenames}")
dif_for_merid = dict.fromkeys([j for j in range(min_meridian, max_meridian+1, meridian_step)], set())
# print(f"dif_for_merid: {dif_for_merid}")
meridian = min_meridian  # пока не придумал, как обосновать выбор диапазона для вариантов меридиана


def stdev(nums):  # стандартное отклонение
    diffs = 0
    avg = sum(nums) / len(nums)
    for n in nums:
        diffs += (n - avg) ** 2
    return (diffs / (len(nums) - 1)) ** 0.5


for key in dif_for_merid.keys():
    set_diffs_pairs = set()
    for i, item in enumerate(st_azimuth):
        try:
            arab_angle = math.degrees(math.acos(minutes_lat_diff[i]*key/60/st_distance[i]))  # здесь вычисляем угол
            # треугольника (в десятичных градусах), который должен быть, если гипотенуза равна реальному расстоянию
            # между городами, а катет - это разница между городами в широте - по арабскому источнику, пересчитанная
            # в градусы и умноженная на длину одного градуса широты
        except ValueError:
            continue

        degrees = math.degrees(item)  # пересчет угла реального азимута из радиан в десятичные градусы
        if degrees < 90:  # проверка угла: если азимут меньше 90 градусов, то для расчетов берем этот угол, если же
            # больше 90 градусов, то для поиска катета нужен угол, смежный с ним
            arab_azim = arab_angle  # пересчет угла арабского треугольника в десятичных градусах в азимут,
            # сопоставимый с реальным
        elif degrees < 180:
            arab_azim = 180-arab_angle
        elif degrees < 270:
            arab_azim = 180+arab_angle
        elif degrees < 360:
            arab_azim = 360 - arab_angle
        else:
            arab_azim = None
        diff_angle = degrees - arab_azim  # вычисляем отклонение от реального азимута (если значение отрицательное,
        # арабский север левее, если положительное - правее)
        set_diffs_pairs.add((round(diff_angle, 2), i, *list(str(pairs[i]).split('-')), round(degrees, 2)))  # для
        # последующей записи городов -участников пары в отдельные поля, пара разбивается на отдельные города,
        # созданный в результате массив раскрывается
        # print(f"set_diffs_pairs: {set_diffs_pairs}")

    dif_for_merid[key] = set_diffs_pairs
    meridian += meridian_step    # поскольку у арабских географов приводятся градусы с точностью до минуты,
    # подбор длины "арабского" градуса производился с шагом соразмерным длине одной минуты. Поскольку длина дуги
    # меридиана в 1 градус составляет в действительности ок. 111 км, а длина одной минуты, соответственно,
    # около 1850 метров, нет смысла использовать шаг меньше 1000 метров.

grouped_by_towns_inside_meridian = {}   # сюда собрал отклонения, сгруппированные по городам
for i, value in dif_for_merid.items():
    one_meridian_groups = {}
    for k in placenames.keys():
        accum = []
        for j in value:
            if (j[2] == k) | (j[3] == k):
                accum.append(j)
        one_meridian_groups[k] = sorted(accum)
    grouped_by_towns_inside_meridian[i] = one_meridian_groups

grouped_without_towns_inside_meridian = {}  # сюда собраны данные об отклонениях от реального азимута без одного из
# городов
for i, value in dif_for_merid.items():
    one_meridian_groups = {}
    for k in placenames.keys():
        accum = []
        for j in value:
            if (j[2] != k) & (j[3] != k):
                accum.append(j)
        one_meridian_groups[k] = accum
    grouped_without_towns_inside_meridian[i] = one_meridian_groups

# for k, v in grouped_by_towns_inside_meridian.items():
#     print(k, v)

# for k, v in grouped_without_towns_inside_meridian.items():
#     print(k, v)

matrix = []  # здесь собираются значения стандартного отклонения без одного из городов
for ky, val in grouped_without_towns_inside_meridian.items():
    mylist = []
    for k, v in val.items():
        town_stdev = round(stdev([i[0] for i in v]), 2)
        mylist.append([k, town_stdev])
    matrix.append([ky, sorted(mylist, key=itemgetter(1))])  # выдаем список, отсортированный по возрастанию
    # стандартного отклонения, полученного без учета соответствующего города. То есть, соответствие некой общей СК в
    # этом списке возрастает
    # print(key,val)
# print(len(st_azimuth))

# for i in matrix:
#     print(i)
# with open("for_diagram3.csv", "w") as file:
#     i = 0
#     while i < len(matrix):
#         j = 0
#         while j < 2:
#             s = str(matrix[i][j])
#             file.write(s + ';')
#             j = j+1
#         file.write('\n')
#         i = i+1




# print(len(matrix[1]))
# data_names = [i[0] for i in matrix]
# data_values = []
# for i in matrix:
#     for j in i:
#         if type(j)==list:
#             for k in j:
#                 data_values.append(k[1])
# dpi = 80
# fig = plt.figure(dpi = dpi, figsize = (1024 / dpi, 768 / dpi) )
# mpl.rcParams.update({'font.size': 8})
# plt.title('Распределение стандартного отклонения в "группах без одного города" по значениям различных меридианов')
# ax = plt.axes()
# ax.yaxis.grid(True, zorder = 1)
# xs = range(len(data_names))
# plt.bar(xs, sorted(data_values), width = 0.5, color = 'red', alpha = 0.7, zorder = 1)
# plt.xticks(xs, data_names)
# fig.autofmt_xdate(rotation = 90)
# fig.savefig('bars.png')

# print(data_values)
# #
# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()
#
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
#
#         # create a cursor
#         cur = conn.cursor()
#
#         # close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


# if __name__ == '__main__':
#     connect()

# trg = [[i[1]] for i in devs_meridians]
# trn = []
# for i in devs_meridians:
#     dif = []
#     for j in i:
#         if type(j) == list:
#             dif.append(j[3])
#     trn.append([i[0], *dif])
# print(trg)
# print(trn)
# print(devs_meridians)
# myFile = open('stdev.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(trg)
#
# print("Writing complete")

# models = [LinearRegression(), RandomForestRegressor(n_estimators=100, max_features ='sqrt'), KNeighborsRegressor(
# n_neighbors=6), SVR(kernel='linear'), LogisticRegression()] Xtrn, Xtest, Ytrn, Ytest = train_test_split(trn, trg,
# test_size=0.4)
#
# TestModels = DataFrame()
# tmp = {}
# for model in models:  #для каждой модели из списка
#     m = str(model) #получаем имя модели
#     tmp['Model'] = m[:m.index('(')]
#     for i in range(Ytrn.shape[1]): #для каждого столбца результирующего набора
#         model.fit(Xtrn, Ytrn[:,i]) #обучаем модель
#         tmp['R2_Y%s'%str(i+1)] = r2_score(Ytest[:,0], model.predict(Xtest)) #вычисляем коэффициент детерминации
#     TestModels = TestModels.append([tmp]) #записываем данные и итоговый DataFrame
# TestModels.set_index('Model', inplace=True) #делаем индекс по названию модели
#
# fig, axes = plt.subplots(ncols=1, figsize=(10,4))
# TestModels.R2_Y1.plot(ax=axes[0], kind='bar', title='R2_Y1')
# TestModels.R2_Y2.plot(ax=axes[1], kind='bar', color='green', title='R2_Y2')


# cur.execute('''DROP TABLE IF EXISTS arabs.abu_meditterenian_said_diffs;
# CREATE TABLE arabs.abu_meditterenian_said_diffs
#      (first_point character varying NOT NULL,
#      second_point character varying NOT NULL,
#      diff_azim integer NOT NULL,
#      real_azim integer NOT NULL,
#      fid integer PRIMARY KEY DEFAULT nextval('arabs.abu_meditterenian_said_diffs_seq'::regclass));''')
# conn.commit()

# INSERT
# INTO
# arabs.abu_meditterenian_said_diffs
# VALUES()

# array_mins = []   #   этот массив будет собирать 10 наименьших расхождений между разницей широт двух пунктов (
# "арабский" катет меридиана) и катета, рассчитанного при переборе различных "арабских" азимутов
#
# while min_azimuth < max_azimuth: catet = abs(st_distance[i]*math.cos(math.radians(
# min_azimuth//60+min_azimuth%60/60))/meridian) #   это расчет катета, который получается при подстановке переменного
# азимута. Поскольку модуль Math работает с десятичным представлением градусов, при переводе минут в градусы это
# учитывается approx = abs(minutes_lat_diff[i] - catet)   #   это сравнение между разницей арабских минут широт
# каждой пары пунктов с "арабским" катетом. Чем меньше разница между ними, тем точнее соответствующий азимут
# характеризует арабскую СК if len(array_mins) > 0: if array_mins[-1][0] > approx:  #   сравниваем новое значение
# разницы с последним (то есть самым большим), содержащимся в списке if len(array_mins)>10: array_mins.pop()    #
# если в списке уже больше 10 значений, то самое последнее отбрасываем # diff = min_azimuth-st_azimuth[i]
# #формируем пару из а) разницы между подобранным значением азимута и реальным азимутом двух пунктов (то есь
# фактически - отклонение арабского полюса от современного) и б) значения минимального расхождения, чтобы забросить
# ее в список diff = min_azimuth - grades*60    # так ли это для углов больше 90 градусов? см. раздельно результаты
# mylist = [approx, int(diff)]    # вывод размера расхождения и соответствующей разницы в минутах array_mins.append(
# mylist) array_mins.sort()  # чтобы не создавать, а потом сортировать список из 11000 пар азимут-разница,
# каждый раз перед сравнением нового значения с имеющимися в списке проводится сортировка else: array_mins.append([
# 10000, 10000]) min_azimuth += 1    #увеличиваем тестируемое значение азимута на 1 минуту и повторяем расчеты в
# цикле pairs_mins.update({pairs[i]:array_mins})

# for i in devs_meridians:
#     print(i)
