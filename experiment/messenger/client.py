import logging
from socket import AF_INET, SOCK_STREAM, socket
import time
import json
import argparse

from log.client_log_config import msngr_log
import utils

logging.getLogger("mssngr.client")


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('address')  # В задании параметр указан как обязательный
    parser.add_argument('port', nargs='?', default='7777', type=int)
    msngr_log.debug(f'Парсинг команды запуска клиента выполнен')

    return parser


timestamp = time.time()

credentials = {"user": {
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


def pres():  # сформировать presence-сообщение;
    fields = actions['presence']
    msg = {
        "action": 'presence',
        "time": timestamp,
    }
    msg.update(fields[0])
    msg.update(fields[1])
    msngr_log.debug('Presence-сообщение для сервера сформировано')
    return msg


def send_mes(msg):  # отправить сообщение серверу;
    mess_json = json.dumps(msg)
    response = mess_json.encode('utf-8')
    transport.send(response)
    msngr_log.info('Сообщение серверу отправлено')


def parse(msg):  # разобрать сообщение сервера
    if msg['response'] == "200":
        msngr_log.debug('Сервер сообщил об успешном соединении')
        return '200: OK'
    else:
        msngr_log.critical(f'Сервер сообщил об ошибке {msg}')
        return '400 : Error'


if __name__ == '__main__':
    my_parser = create_parser()
    namespace = my_parser.parse_args()
    params = (namespace.address, namespace.port)

    transport = socket(AF_INET, SOCK_STREAM)
    try:
        transport.connect(params)
        send_mes(pres())
    except Exception:
        msngr_log.critical(f'Параметры соединения ({params}) не принимает сервер')
    try:
        response = utils.receiving(transport, msngr_log)
        print(parse(response))
    except (ValueError, json.JSONDecodeError):
        msngr_log.critical('Ошибка декодирования сообщения')
