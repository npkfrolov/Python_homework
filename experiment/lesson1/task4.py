# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standard']
encs = ['utf-8', 'cp1251', 'cp866']

def codecode(word):
    for el in encs:
        encoded = word.encode(el)
        decoded = encoded.decode(el)
        return (f'байты: {encoded}, строка:  {decoded}')

for i in words:
    result = codecode(i)
    print(f'слово {i}:  {result}')