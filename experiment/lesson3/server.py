import json
from socket import AF_INET, SOCK_STREAM, socket
import time
import argparse


def createParser():
    myparser = argparse.ArgumentParser()
    myparser.add_argument('-a', '--address', default='')
    myparser.add_argument('-p', '--port', default='7777', type=int)

    return myparser


timestamp = time.time()
code_table = {
    '100': 'базовое уведомление',
    '101': 'важное уведомление',
    '200': 'Необязательное сообщение/уведомление',
    '201': 'объект создан',
    '202': 'подтверждение',
    '400': 'неправильный запрос/JSON-объект',
    '401': 'не авторизован',
    '402': 'This could be "wrong password" or "no account with that name"',
    '403': 'пользователь заблокирован',
    '404': 'пользователь/чат отсутствует на сервере',
    '409': 'Someone is already connected with the given user name',
    '410': 'адресат существует, но недоступен (offline)',
    '500': 'ошибка сервера',
}

credentials = {"user":
    {
        "account_name": "C0deMaver1ck",
        "password": "CorrectHorseBatterStaple"
    }
}

actions = {
    'quit': '',
    'probe': '',
    'msg': {
        "to": "account_name",
        "from": "account_name",
        "encoding": "utf-8",
        "message": "message"
    },
    'join': {
        "room": "#room_name"
    },
    'leave': {
        "room": "#room_name"
    },
}


def receiving(clnt):  # принимает сообщение клиента;
    try:
        client_data = clnt.recv(50000)
        print(f'От клиента пришло сообщение: {client_data.decode()}')
        resp_code = 200
    except PermissionError:  # это пока заглушка - коды ошибок не анализировал
        resp_code = 402
    return resp_code


def response(resp_code, action_type):  # формирует ответ клиенту;
    msg = {
        "action": action_type,
        "time": timestamp,
        "response": str(resp_code),
        "alert": code_table[str(resp_code)]
    }
    msg.update(actions[action_type])
    return msg


def send_mes(cli, mesg):  # отправляет ответ клиенту
    with open('mess_to_cl.json', 'w') as mess_json:  # Это костыль. Конечно, должен быть способ напрямую отправлять,
        # минуя файл
        mess_json.write(json.dumps(mesg))
    with open('mess_to_cl.json', 'rb') as mess_read:
        cli.send(mess_read.read())


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    params = (namespace.address, namespace.port)

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(params)
    s.listen(5)

    while True:
        client, addr = s.accept()
        print(f'Принято соединение от клиента с адреса {addr}')
        mess = response(receiving(client), 'msg')
        send_mes(client, mess['response'])
        client.close()
