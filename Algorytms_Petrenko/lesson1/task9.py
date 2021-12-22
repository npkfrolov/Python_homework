print("Введите три разных числа для поиска среднего")
a = float(input('Введите первое из чисел: '))
b = float(input('Введите втоое из чисел: '))
c = float(input('Введите третье из чисел: '))

if a > b:
    if b > c:
        print(f'среднее число {b}')
    elif a > c:
        print(f'среднее число {c}')
    else:
        print(f'среднее число {a}')
else:
    if a > c:
        print(f'среднее число {a}')
    elif b > c:
        print(f'среднее число {c}')
    else:
        print(f'среднее число {b}')
