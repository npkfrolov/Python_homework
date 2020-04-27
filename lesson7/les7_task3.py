# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

import random

m = int(input(f'Введите число m: '))
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2*m + 1)]
random.shuffle(array)
print(array)

def heapify(arr, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)

def sorting(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

sorting(array)
print(array)

print(f'Медиана массива чисел равна {array[m]}')