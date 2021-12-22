# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV

import csv
from pathlib import Path

pool = ['info_1.txt', 'info_2.txt', 'info_3.txt']
current_path = Path.cwd()

def get_data(pool):
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']  # ДЗ требует включить этот
    # список в функцию, хотя я бы вынес ее просто как переменную вне функций
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in pool:
        myfile = current_path / file
        with open(myfile, encoding='cp1251') as txt_file:
            for line in txt_file:
                my_list = line.split(':')
                try:
                    name = my_list[0]
                    value = my_list[1].lstrip().rstrip('\n')
                except IndexError:
                    continue

                if name == 'Изготовитель системы':
                    os_prod_list.append(value)
                elif name == 'Название ОС':
                    os_name_list.append(value)
                elif name == 'Код продукта':
                    os_code_list.append(value)
                elif name == 'Тип системы':
                    os_type_list.append(value)

    return [main_data, os_prod_list, os_name_list, os_code_list, os_type_list]  # из-за условий ДЗ лишний
            # хардкодинг. Если вынести main_data и четыре списка за пределы функции в отдельный список, то от этого
            # можно избавиться, редактируя из функции матрицу, обращаясь по номерам к отдельным спискам

def write_to_csv(link):
    with open(link, 'w') as csv_file:
        csv_file_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_file_writer.writerows(get_data(pool))

write_to_csv('result_task1.csv')

with open('result_task1.csv') as f_n:
    print(f_n.read())
