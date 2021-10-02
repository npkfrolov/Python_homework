# coding=utf-8
"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор."""

numbers = [2, 20, 24, 56, 77, 56, 88, 34, 5]
print(list(el for el in numbers if numbers.count(el) == 1))