a = float(input('Введите длину первого отрезка '))
b = float(input('Введите длину второго отрезка '))
c = float(input('Введите длину третьего отрезка '))

if (a < b+c) and (b < a+c) and (c < a+b):
    if a==b:
        if b==c:
            print('треугольник равносторонний')
        else:
            print('треугольник равнобедренный')
    else:
        if b==c:
            print('треугольник равнобедренный')
        else:
            if a==c:
                print('треугольник равнобедренный')
            else:
                print('треугольник разносторонний')
else:
    print('отрезки указанных длин не могут составить треугольник')