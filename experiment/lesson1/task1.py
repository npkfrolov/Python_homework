# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

# PS. В DOM онлайн-конвертера атрибут .text в поле, возвращающем результат конвертации, почему-то не работает. Пришлось
# просто захардкодить формат юникод.

# from time import sleep
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager

mydict = {
    'разработка': '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    'сокет': '\u0441\u043e\u043a\u0435\u0442',
    'декоратор': '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'}

for key, value in mydict.items():
    print(f'тип переменной: {type(str(key))}')
    print(f'содержание переменной: {str(key)}')
    print(f'тип переменной (юникод-строка): {type(str(value))}')
    print(f'содержание переменной (юникод-строка): {str(value)}')

    # driver.get(url)
    # data = driver.find_element_by_id('cbi_text').send_keys(i)
    # sleep(2)
    # result = driver.find_element_by_id('cbo_text').text
    # print(result)

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# options = webdriver.FirefoxOptions()
# options.add_argument('headless')
# url = 'https://calcsbox.com/post/konverter-teksta-v-unikod.html'

# driver.quit()
