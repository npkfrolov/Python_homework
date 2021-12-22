# coding=utf-8
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

n = 0   # счетчик элементов списка
user_list = []

while True:     # создание списка значений, пока пользователь не решит завершить
    element = raw_input("Enter %i element of the list\n(Type 'f' to pass to the next step): " % (n+1))
    if element == "f": # костыльное решение, по-хорошему надо иначе, чтобы f можно было вводить и как значение списка
        break
    n += 1
    user_list.append(element)

print ("So, we got the list of %i elements: " % n)
print (user_list)
print ('Now let us start magic')

listA = user_list[::2]
listB = user_list[1::2]
changed_list = zip(listB, listA)
if len(user_list) % 2 != 0:
    changed_list.append(user_list[-1])

print("Magic list looks like: ")
print(changed_list)
