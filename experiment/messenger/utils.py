import json


def receiving(host, msngr_log):  # получить ответ, в зависимости от того, на клиенте получается ответ или на сервере,
    # параметром передается и логгер;
    data = host.recv(50000)
    msngr_log.info(f'Получено сообщение: {data.decode()}')
    if isinstance(data, bytes):
        json_response = data.decode('utf-8')
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            msngr_log.debug('Ответ преобразован в словарь')
            return response_dict
        else:
            msngr_log.error('Ответ не удалось преобразовать в словарь')
            raise ValueError
    else:
        msngr_log.error('Неверный формат ответа хоста')
        raise ValueError
