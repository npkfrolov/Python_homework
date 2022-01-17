import inspect
import logging
import sys
import traceback
import time


if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('mssngr.server')
else:
    LOGGER = logging.getLogger('mssngr.client')


class Log:  # декоратор в виде класса - использовал на клиенте
    def __call__(self, func):
        def log_saver(*args, **kwargs):
            ret = func(*args, **kwargs)
            LOGGER.debug(f'{time.asctime()} Функция {func.__name__} '
                         f'(параметры: {args}, {kwargs}; '
                         f'модуль: {func.__module__}) '
                         f'вызвана из функции {traceback.format_stack()[0].strip().split()[-1]}. '
                         f'Вызов из функции {inspect.stack()[1][3]}.')
            return ret
        return log_saver


def log(func):  # Декоратор в виде функции - использовал на сервере
    def log_saver(*args, **kwargs):
        ret = func(*args, **kwargs)
        LOGGER.debug(f'{time.asctime()} Функция {func.__name__} '
                         f'(параметры: {args}, {kwargs}; '
                         f'модуль: {func.__module__}) '
                         f'вызвана из функции {traceback.format_stack()[0].strip().split()[-1]}. '
                     f'Вызов из функции {inspect.stack()[1][3]}.')
        return ret
    return log_saver

