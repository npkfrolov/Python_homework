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
    mess_json = json.dumps(msg)
    response = mess_json.encode('utf-8')
    transport.send(response)

def receiving(serv): # получить ответ сервера;
    serv_data = serv.recv(50000)
    if isinstance(serv_data, bytes):
        json_response = serv_data.decode('utf-8')
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError

def parse(msg): # разобрать сообщение сервера
    if msg['response'] == 200:
        return '200: OK'
    return f'400 : Error'

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    params = (namespace.address, namespace.port)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect(params)
    send_mes(pres())
    try:
        response = receiving(transport)
        parse(response)
        print(f'Ответ от сервера: {response}')
    except (ValueError, json.JSONDecodeError):
            print(f'Ошибка декодирования сообщения')
