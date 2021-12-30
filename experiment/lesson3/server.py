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
    client_data = clnt.recv(50000)
    print(f'От клиента пришло сообщение: {client_data.decode()}')
    if isinstance(client_data, bytes):
        json_response = client_data.decode('utf-8')
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError


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
    mess_json =  json.dumps(mesg)
    response = mess_json.encode('utf-8')
    cli.send(response)


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
        try:
            mess = receiving(client)
            resp = response(200, 'msg')
            send_mes(client, resp)
        except (ValueError, json.JSONDecodeError):
            print(f'Принято некорректное сообщение от клиента с адреса {addr}')
        client.close()
