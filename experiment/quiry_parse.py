import psycopg2
import re

conn = psycopg2.connect(f"dbname='Base' user='npkfrolov' password='123308' host='127.0.0.1' port='5432'")
print("Database opened successfully")
cur = conn.cursor()

def search(start, end, content):    #принимает границы, внутри которых содержится искомая подстрока, и строку
    patt = start+'(.*?)'+end
    return re.findall(patt, content)

# def parsing(string):    # приводит результат работы функции search к виду, необходимому для загрузки в БД.
    # roman_numb = str(*search('@','@', content))
    # row = str(*search('#','#', content))
    # raw_height = int(*search('=','=', content))
    # raw_width = int(*search('<','>', content))
    # watermark = str(*search('ff','fff', content))
    # watermark_leaves = str(*search('pp','ppp', content))
    # pontuso = str(*search('ww','www', content))
    # capture = str(search('zz','zzz', content))
    # mark = str(search('nn','nnn', content))
    # scr_one = str(search('one','first', content))
    # scr_two = str(search('two','second', content))
    # scr_three = str(search('three','third', content))
    # cur.execute('''INSERT INTO sophia.quires
    #      (roman_numb, row, raw_width, raw_height, watermark, watermark_leaves, pontuso, capture, mark, scr_one, scr_two, scr_three) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (roman_numb, row, raw_width, raw_height, watermark, watermark_leaves, pontuso, capture, mark, scr_one, scr_two, scr_three))
    # cur.execute('''UPDATE sophia.quires SET whole_descr = ''')
    # conn.commit()
    # return roman_numb


with open("/home/alexey/Документы/Yandex_disk/программер/quiries_descr_cleared.txt", "r") as file:
    for content in file:
        num = str(*search('@','@', content))
        cur.execute('''UPDATE sophia.quires SET whole_descr = %s WHERE roman_numb LIKE %s''', (content, num)) #обновляет поле уже существующей записи
        conn.commit()

# cur.execute('SELECT * FROM sophia.quires')
# dbrecords_calc = cur.fetchall()