# coding=utf-8
#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = []
my_list.append("hello")
my_list.append(None)
my_list.append(-10)
my_list.append(3.14)
my_list.append(5)
my_list.append(True)
my_list.append([1, 3, 5])
my_list.append({'d', 'g'})
my_list.append({"first": 1, "second": 2})
new_list = []

for ind, el in enumerate(my_list, 0):
    el_type = str(type(el))
    answer = el_type[1:-1]
    new_list.append(answer[6:-1])
    print("Index " + str(ind) + " ('" + str(el) + "')" + " has %s" % answer)

zip_list = zip(my_list, new_list)
print ("\n As you asked: " + str(zip_list))
