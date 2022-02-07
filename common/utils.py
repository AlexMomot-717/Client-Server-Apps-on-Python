""" Функции для использования обоими сторонами: сервера и клиента"""

import json
import sys
from common.variables import MAX_PACKAGE_LENGTH, ENCODING
from errors import IncorrectDataRecivedError, NonDictInputError
from deco_server import log
from deco_client import log
# sys.path.append('../')


@log
def get_message(client):
    """
    Утилита для приема в байтах и декодирования
    сообщений, возвращает словарь или ошибку (если на входе не байты)
    :param client:
    :return:
    """

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


@log
def send_message(sock, message):
    """
    Утилита для кодирования и отправки
    сообщения, принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """

    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
