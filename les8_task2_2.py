# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque
forcoding = 'ddddfaggggggggggtfdcmml'
    # input('Введите кодируемую строку: ')
a = Counter(forcoding)
b = a.most_common() # превращение словаря в список кортежей
b = deque(b)
mydict = {}
print(b)

def nodes(arr):
    if len(arr) == 2:
        mydict.update({arr[0][0]: 0})
        mydict.update({arr[1][0]: 1})
        return

    first = arr.pop()
    second = arr.pop()
    summ = first[1] + second[1]
    mydict.update({first[0]:0})
    mydict.update({second[0]:1})
    i = 0
    while arr[i][1] > summ:
        i +=1
    k,l = (first[0], second[0])
    node = (str(l+k), summ)
    arr.insert(i, node)
    nodes(arr)

nodes(b)
mylist1 = [i for i in mydict.keys()]
mylist2 = [i for i in mydict.values()]
mylist3 = [i for i in mylist1 if len(i) == 1]
mylist4 = [i for i in mylist1 if len(i) > 1]

result_list = [][]
for index, x in enumerate(mylist4):
    for y in list(x):
        result_list.append([y][index])

# for item in mydict:
#     mylist.append(item)
# print(nodes(b))
# print(mydict)
# print(mylist1)
# print(mylist2)
# print(mylist3)
print(mylist4)
print(result_list)