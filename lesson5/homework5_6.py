"""Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести словарь на экран."""

with open("homework6.txt") as content:
    my_dict = {}
    for line in content:
        my_key = line.split()[0]
        total = 0
        for el in line.split():
            """здесь я схитрил - не придумал, как использовать 
            несколько вариантов для разбивки на элементы (" ", ":", ", "). 
        Поэтому перед двоеточием и запятой тоже поставил пробелы"""
            try:
                total = total + int(el)
            except ValueError:
                continue
        my_dict.update({my_key: total})
    print(my_dict)
