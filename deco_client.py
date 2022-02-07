from functools import wraps
import logging
import log.client_log_config
from datetime import datetime
import inspect


logger = logging.getLogger('app.client')

def log(func):
    """
    внешняя функция
    :param param:
    :return:
    """
    def wrapper(*args, **kwargs):
        """
        истинно декоратор
        :param:
        :return:
        """
        func_res = func(*args, **kwargs)
        d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.debug(f'{d}: функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return func_res
    return wrapper
