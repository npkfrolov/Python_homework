number = tuple(input('Введите число из трех цифр: '))

a, b, c = number
sum = int(a) + int(b) + int(c)
product = int(a) * int(b) * int(c)

print(f'сумма цифр составляет {sum}, произведение чисел равно {product}')