# Программа сервера

from socket import *
from sys import argv, exit
from common.utils import *
from common.variables import *
import logging
import log.server_log_config


# получаем уже созданный логгер
logger = logging.getLogger('app.server')


def process_client_message(message):
    """
    Функция принимает сообщения клиента в виде словаря,
    выполняет проверку и формирует ответное сообщение (словарь) клиенту
    :param message:
    :return:
    """

    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        logger.debug('Получено корректное сообщение от Клиента и сформирован ответ "200"')
        return {RESPONSE: 200}
    logger.debug('Получено некорректное сообщение от Клиента и сформирован ответ "400"')
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Обработка параматеров командной строки,
    при их отсутствии устанавливаем значения по умолчанию
    Сначала обрабатывается порт:
    server.py -p 8888 -a 127.0.0.1
    :return:
    """

    try:
        if '-p' in argv:
            listen_port = int(argv[argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT

        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        logger.error('После параметра -\'p\' необходимо указать номер порта')
        exit(1)

    except ValueError:
        logger.error('В качестве порта может быть только число в \n'
              'диапазоне от 1024 до 65535')
        exit(1)

    # Указываем, какой адрес слушать:
    try:
        if '-a' in argv:
            listen_address = int(argv[argv.index('-a') + 1])
        else:
            listen_address = ''
    except IndexError:
        logger.error('После параметра -\'a\' необходимо указать адрес, который будет слушать сервер')
        exit(1)

    # Формируем сокет:
    logger.debug('Создаем сокет')
    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт:
    logger.debug('Слушаем порт')
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, address = transport.accept()
        logger.debug('Принимается запрос на присутствие Клиента')
        try:
            logger.debug('Получаем сообщение от Клиента')
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            logger.debug('Отправлен ответ Клиенту')
            client.close()
        except (ValueError, json.JSONDecodeError):
            logger.error('От Клиента получено некорректое сообщение!')
            client.close()


if __name__ == '__main__':
    main()
