import csv

pages = []
pagination = []
table = [['quiry', 'watermark', 'position', 'count']] # заголовки для таблицы заранее прописаны


with open("/home/alexey/Загрузки/temp_Клушин_pages.csv") as f_obj: # файл, откуда берем данные для парсинга познаково
    for index, line in enumerate(f_obj):
        pages.append(list(line))

for ind_i, i in enumerate(pages):
    for ind_j, j in enumerate(i):
        pos = [ind_i+1, j, ind_j+1, len(i)-1] # вычисление номера строки в файле, атрибута филиграни, позиции филиграни в тетради, числа листов в тетради
        if pos[1] != '\n':  # освобождение от переносов строки, записанных в конце каждой строки при превращении ее в список
            table.append(pos)

with open("/home/alexey/Загрузки/pagination.csv") as page_obj: # файл, откуда берем данные о пагинации
    reader = csv.reader(page_obj)
    for row in reader:
        pagination.append(row)
        # print(pagination)

myzip = [x + y for x, y in zip(pagination, table)] # объединяет распарсенное поле с формулой тетрадей с любыми другими csv, где есть полистные атрибуты

with open("/home/alexey/Загрузки/convert_pages.csv", "w") as csvfile: # запись в csv
    writer = csv.writer(csvfile)
    writer.writerows(myzip)
    print("Готово")

# for x in table:
#     print(*x)

