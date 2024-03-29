# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

m = random.randint(0, 100)
n = int(input('Угадайте натуральное число от 0 до 100 (у Вас 10 попыток): '))
i = 0
while i < 9:
    if n == m:
        print('Вы угадали число')
        break
    else:
        i += 1
        if n > m:
            print(f'Загаданное число меньше предложенного, \n у Вас осталось {10-i} попыток')
            n = int(input('Ваша новая попытка: '))
            continue
        else:
            print(f'Загаданное число больше предложенного, \n у Вас осталось {10-i} попыток')
            n = int(input('Ваша новая попытка: '))
            continue
else:
    print(f'Число {m} не угадано. Вы истратили все попытки')
print('Игра закончена')