"""Unit-тесты утилит"""

import json
import os
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from common.utils import get_message, send_message


class TestSocket:
    """
    тестовый класс для тестирования отправки и получения
    при создании трбует словарь, который будет прогоняться через тестовую функцию
    """
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        """
        тестовая функция отправки, корректно кодирует сообщения,
        так же сохраняет то, что должно быть отправлено в сокет,
        message_to_send  - то, что отправляем в сокет
        :param message_to_send:
        :return:
        """
        json_test_message = json.dumps(self.test_dict)
        # кодирует сообщение
        self.encoded_message = json_test_message.encode(ENCODING)
        # сохраняем, что должно быть отправлено в сокет
        self.received_message = message_to_send

    def recv(self, max_len):
        """
        Получаем данные из сокета
        :param max_len:
        :return:
        """
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    """
    Тестовый класс, выполняющий тестирование
    """

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 111111.111111,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def setUp(self):
        """ настройка тестов """
        pass

    def tearDown(self):
        """ завершающее удаление настроек """
        pass

    def test_send_correct_message(self):
        """
        Тестируем коооректность работы функции отправки,
        создаем тестовый сокет
        :return:
        """
        # экземпляр тестового словаря, хранит собственно текстовый словарь
        test_socket = TestSocket(self.test_dict_send)
        # вызов тестируемой функции, результаты будут сохранены в тестовом сокете
        send_message(test_socket, self.test_dict_send)
        # проверка корректности кодирования словаря
        # сравниваем результат проверенного кодирования и результат тестируемой функции
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_wrong_message(self):
        """
        проверяем корректность отправки словаря
        :return:
        """
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        # проверка генерации исключения: если на входе не словарь
        self.assertRaises(TypeError, send_message, test_socket, 'wrong_dictionary')

    def test_get_correct_message(self):
        """
        тест функции приема сообщений
        :return:
        """
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        # тест корректной расшифровки корректного словаря
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_wrong_message(self):
        """
        тест проверки корректности входящего словаря
        :return:
        """
        test_sock_err = TestSocket(self.test_dict_recv_err)
        # тест корректной расшифровки некорректного словаря
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
