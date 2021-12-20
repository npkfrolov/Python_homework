# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
# У меня независимо от локали пинг отдает ответ по-английски
import locale
import subprocess
def_coding = locale.getpreferredencoding()
site = ['yandex.ru', 'youtube.com']
print(f'Дефолтная кодировка: {def_coding}')

def myping(arg):
    subproc_ping = subprocess.Popen(arg, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        print(f'NODECODE: {line} & DECODE: {line.decode("utf-8")}')

for i in site:
    print(f'Два варианта - байты (NODECODE) и строка Юникод (DECODE)')
    myping(['ping', '-c', '1', i])