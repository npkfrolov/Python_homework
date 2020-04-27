import random

SIZE = 10
MAX_ITEM = 50
array = [random.random()*MAX_ITEM for _ in range(SIZE)]
random.shuffle(array)
print(f'Массив до сортировки: {array}')
first = int(0)
last = int(SIZE-1)

def merge(left_list, right_list):
    sorted = []
    pos1 = 0
    pos2 = 0
    left_len = len(left_list)
    right_len = len(right_list)

    for i in range(left_len + right_len):
        if pos1 < left_len and pos2 < right_len:
            if left_list[pos1] <= right_list[pos2]:
                sorted.append(left_list[pos1])
                pos1 += 1
            else:
                sorted.append(right_list[pos2])
                pos2 += 1
        elif pos1 == left_len:
            sorted.append(right_list[pos2])
            pos2 += 1
        elif pos2 == right_len:
            sorted.append(left_list[pos1])
    return sorted

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    split = len(arr) // 2
    left_list = merge_sort(arr[:split])
    right_list = merge_sort(arr[split:])
    return merge(left_list, right_list)

print(f'Результат сортировки: {merge_sort(array)}')