"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open("homework2.txt") as file:
    i = 0
    for line in file:
        i += 1
        print(f"Строка {i}: {len(line.split())} слов")

print(f"Всего строк - {i}")


