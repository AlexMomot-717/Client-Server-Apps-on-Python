# Программа клиента


from socket import *
from sys import argv, exit
from common.utils import *
from common.variables import *
from time import time
import json


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
    return out


def process_answer(message):
    """
    Функция читает ответ сервера
    :param message:
    :return:
    """

    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
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
        print('В качестве порта может быть только число в \n'
              'диапазоне от 1024 до 65535')
        exit(1)

    # Инициализация сокета и обмен

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_answer(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера')

    finally:
        transport.close()


if __name__ == '__main__':
    main()









