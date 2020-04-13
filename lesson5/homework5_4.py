"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

rus_dict = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}
translate = open("result4_txt", "a")

with open("homework4.txt") as engl_numb:
    for line in engl_numb:
        my_list = line.split(" — ")
        my_key = my_list[1]
        for key, value in rus_dict.items():
            if key == my_key:
                translate.write(f"{value} - {key}\n")
                break
translate.close()
