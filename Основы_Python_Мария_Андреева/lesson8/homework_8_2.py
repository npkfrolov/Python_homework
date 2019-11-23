"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""

class New_error_type(Exception):
    def __init__(self, error_text):
        self.error_text = error_text

try:
    dividend = int(input("Введите делимое: "))
except ValueError:

    print("Вы ввели не число")
try:
    denomin = int(input("Введите делитель: "))
    if denomin == 0:
        raise New_error_type("Деление на ноль запрещено")
except New_error_type as err:
    print(err)
except ValueError:
    print("Вы ввели не число")
finally:
    print("Программа завершена")


