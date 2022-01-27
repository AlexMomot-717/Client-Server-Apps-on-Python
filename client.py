# Программа клиента


from socket import *
from sys import argv, exit
from common.utils import *
from common.variables import *
from time import time
import json
import logging
import log.client_log_config
from deco_client import log


# получаем уже созданный логгер
logger = logging.getLogger('app.client')


@log
def create_presence(account_name='Guest'):
    """
    Формируется запрос присутствия клиента
    :param account_name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        TIME: time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    logger.debug('Сформирован запрос на присутствие Клиента')
    return out


@log
def process_answer(message):
    """
    Функция читает ответ сервера
    :param message:
    :return:
    """

    if RESPONSE in message:
        if message[RESPONSE] == 200:
            logger.debug('От Сервера получен ответ "200"  на запрос присутствия Клиента')
            return '200 : OK'
        logger.debug('Получен ответ "400"  на запрос присутствия Клиента')
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """ Считываем параметры командной строки """
    try:
        server_address = argv[1]
        server_port = int(argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT

    except ValueError:
        logger.error('В качестве порта может быть только число в диапазоне от 1024 до 65535')
        exit(1)

    # Инициализация сокета и обмен
    logger.debug('Создаем сокет')

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))

    message_to_server = create_presence()
    send_message(transport, message_to_server)
    logger.debug('Отправлен запрос Серверу')
    try:
        logger.debug('Получаем ответ от Сервера')
        answer = process_answer(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        logger.error('Не удалось декодировать сообщение сервера')

    finally:
        transport.close()


if __name__ == '__main__':
    main()









