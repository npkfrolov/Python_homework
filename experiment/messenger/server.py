import json
import logging
from socket import AF_INET, SOCK_STREAM, socket
import time
import argparse

from log.server_log_config import msngr_log
from utilss import utils
from utilss.decorators import log

logging.getLogger("mssngr.server")

@log
def create_parser():
    myparser = argparse.ArgumentParser()
    myparser.add_argument('-a', '--address', default='')
    myparser.add_argument('-p', '--port', default='7777', type=int)
    msngr_log.debug(f'Парсинг команды запуска сервера выполнен')

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

credentials = {"user": {
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

@log
def response(resp_code, action_type):  # формирует ответ клиенту;
    msg = {
        "action": action_type,
        "time": timestamp,
        "response": str(resp_code),
        "alert": code_table[str(resp_code)]
    }
    msg.update(actions[action_type])
    msngr_log.debug('Ответ сервера клиенту сформирован')
    return msg

@log
def send_mes(cli, mesg):  # отправляет ответ клиенту
    mess_json = json.dumps(mesg)
    rsp = mess_json.encode('utf-8')
    cli.send(rsp)
    msngr_log.info('Ответ клиенту отправлен')


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    params = (namespace.address, namespace.port)

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind(params)
        s.listen(5)
    except Exception:
        msngr_log.critical(f'Параметры сокета ({params}) не позволяют запустить сервер')

    while True:
        client, addr = s.accept()
        msngr_log.debug(f'Принято соединение от клиента с адреса {addr}')
        try: 
            mess = utils.receiving(client, msngr_log)
            resp = response(200, 'msg')
            send_mes(client, resp)
        except (ValueError, json.JSONDecodeError):
            msngr_log.error(f'Принято некорректное сообщение от клиента с адреса {addr}')
        client.close()
