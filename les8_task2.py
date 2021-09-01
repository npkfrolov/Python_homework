from collections import Counter, deque
forcoding = 'ddddfaggggggggggtfdcmml'
    # input('Введите кодируемую строку: ')
a = Counter(forcoding)
b = a.most_common() # превращение словаря в список кортежей

def code(arr):
    nodes(arr)


def nodes(arr):
    if len(arr) == 1:
        root = (arr[0][0], 0)
        # summ = arr[0][1]
        # code = '0'
        return #root, summ

    first = deque([i for index, i in enumerate(arr) if index % 2 == 0])
    second = deque([j for index, j in enumerate(arr) if index % 2 > 0])
    if len(arr) == len(a):  #чтобы разворот очереди был только в самом начале работы функции
        first.reverse()
        second.reverse()
    spam = []
    k = 0
    while k < len(arr) // 2:
        summ = first[k][1] + second[k][1]
        parent = (first[k][0], 0) + (second[k][0], 1)
        node = (parent, summ)
        print(node)
        spam.append(node)
        k += 1
    nodes(spam)

print(nodes(b))

