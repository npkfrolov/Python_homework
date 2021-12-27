from socket import AF_INET, SOCK_STREAM, socket
import time
import json
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('address')  # В задании параметр указан как обязательный
    parser.add_argument('port', nargs='?', default='7777', type=int)

    return parser

timestamp = time.time()

credentials = {"user":
        {
        "account_name": "C0deMaver1ck",
        "password": "CorrectHorseBatterStaple"
        }
}

presence = {"action_type": "status"}

actions = {  # Справочник actions общий для сервера и клиента
    'authenticate': credentials,
    'quit': '',
    'presence': [credentials, presence],
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

def pres(): # сформировать presence-сообщение;
    fields = actions['presence']
    msg = {
        "action": 'presence',
        "time": timestamp,
    }
    msg.update(fields[0])
    msg.update(fields[1])
    return msg

def send_mes(msg): # отправить сообщение серверу;
    with open('mess.json', 'w') as mess_json:  # Это костыль. Конечно, должен быть способ напрямую отправлять, минуя
        # файл
        mess_json.write(json.dumps(msg))
    with open('mess.json', 'rb') as mess_read:
        s.send(mess_read.read())

def receiving(): # получить ответ сервера;
    msg = s.recv(50000)
    return msg

def parse(msg): # разобрать сообщение сервера
    parsed = msg.decode('utf-8')
    print(f'Сервер вернул код: {parsed}')


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    params = (namespace.address, namespace.port)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(params)
    send_mes(pres())
    parse(receiving())
