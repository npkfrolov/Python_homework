# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.

a = list(range(2, 100))
b = list(range(2, 10))
matrix = [[0]*len(a) for _ in b]

for i in a:
    for j in b:
        spam = 0
        if i % j == 0:
            spam = 1
        matrix[j-2][i-2] = spam

for j in b:
    print(f'чисел, кратных {b[j-2]}, {matrix[j-2].count(1)}')