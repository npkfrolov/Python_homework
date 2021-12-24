# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл
# в формате Unicode и вывести его содержимое.
# PS.  Чтобы получить кракозябры, пришлось дополнить ДЗ.

import locale
def_coding = locale.getpreferredencoding()
print(f'Дефолтная кодировка: {def_coding}')
encs = [def_coding, 'cp1251', 'cp866']

def encoding(enc):
    with open('/home/alexey/git_python/Python_homework/experiment/lesson1/test_file.txt', encoding=enc) as f_n:
            for el_str in f_n:
                print(el_str)

for enc in encs:
    encoding(enc)