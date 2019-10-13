# coding=utf-8
# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

fid = 0  # счетчик торговых позиций
structure = []
article_list = []
price_list = []
amount_list = []
measure_list = []

while True:
    article = raw_input( "Enter name of article: " )
    fid += 1
    price = raw_input( "Enter the price: " )
    amount = raw_input( "Enter amount of goods: " )
    measure = raw_input( "Enter measure: " )
    user_dict = {'article': [article], 'price': [price], 'amount': [amount], 'measure': [measure]}
    feature_attr = (fid, user_dict)  # кортеж, объединяющий счетчик и словарь
    print ("We got: " + str(feature_attr)) # промежуточный результат для наглядности пользователю
    submit = str.lower(raw_input("Include the record into DB?\n(yes - 'Y', no - any key)")) # не успел предусмотреть вариант, когда пользователь не хочет подтвердить самую первую запись и хочет на этом этапе выйти из цикла
    if submit != "y":
        continue
    structure.append(feature_attr) # добавление утвержденной пользователем записи в структуру
    article_list.append(article)
    price_list.append((price))
    amount_list.append(amount)
    measure_list.append(measure)
    go_on = str.lower(raw_input("Do yo want to continue?\n(yes - 'Y', no - any key)"))
    if go_on != "y":
        break

print ("This is the stucture:" )
print (structure)
analytics = dict(article = list(set(article_list)), price=list(set(price_list)), amount=list(set(amount_list)), measure=list(set(measure_list)))
print ("This is analytics: ")
print (analytics)
