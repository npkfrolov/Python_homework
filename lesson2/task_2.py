# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, в нем 3 четные цифры(4, 6 и 0) и 2 нечетные(3 и 5).

even = 0
odd = 0
numb = input('Введите натуральное число: ')
numb = str(numb)
for i in numb:
    if int(i) % 2 == 0:
       even += 1
    else:
        odd += 1
print(f'Введенное число содержит четных {even} и нечетных {odd} цифр')