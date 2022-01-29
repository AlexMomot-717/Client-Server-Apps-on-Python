"""Константы"""

import logging

# default порт для сетевой коммуникации:
DEFAULT_PORT = 7777

# default IP-адрес для соединения с клиентом:
DEFAULT_IP_ADDRESS = '127.0.0.1'

# максимальное число клиентов в ожидании подключения к серверу:
MAX_CONNECTIONS = 5

# ограничение длины сообщения в байтах:
MAX_PACKAGE_LENGTH = 1024

# кодировка проекта:
ENCODING = 'utf-8'

# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

# основные ключи протокола JIM:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'sender'

# вспомогательные ключи протокола JIM:
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'