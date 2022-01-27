# конфиг клиентского логгера

import logging
import os
import sys

sys.path.append('../')

# создаём форматер:
client_formatter = logging.Formatter('%(asctime)s %(levelname)-9s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'app.client.log')

# файловый обработчик
fh = logging.FileHandler(PATH, encoding='utf-8')
fh.setFormatter(client_formatter)
fh.setLevel(logging.DEBUG)

# регистратор верхнего уровня и добавляем обработчик, устанавливаем уровень
logger = logging.getLogger('app.client')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger.debug('Отладочная информация')
    logger.info('Информационное сообщение')
    logger.warning('Предупреждение')
    logger.error('Ошибка')
    logger.critical('Критическая ошибка')
