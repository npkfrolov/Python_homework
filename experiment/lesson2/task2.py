# Задание на закрепление знаний по модулю json.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r') as file:
        orders_data = json.load(file)

    if not 'orders' in orders_data:
        orders_data['orders'] = []
    orders_data['orders'].append({
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    })

    with open('orders.json', 'w') as add_json:
        json.dump(orders_data, add_json, indent=4)


write_order_to_json("Товар", 3, 100, "Рога и копыта лимитед", "2021-12-22")