# Задание на закрепление знаний по модулю json.

import json

def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'w') as f_n:
        dict_to_json = {
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date,
        }
        json.dump(dict_to_json, f_n, indent=4)

    with open('orders.json') as f_n:
        print(f_n.read())

write_order_to_json("Товар", 3, 100, "Рога и копыта лимитед", "2021-12-22")