# логгер сервера

import logging.handlers
import os
import sys

# sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append('../')

# форматер:
server_formatter = logging.Formatter('%(asctime)s %(levelname)-9s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'app.server.log')

# файловый обработчик, настройка ежедневной ротации файла
fh = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
fh.setFormatter(server_formatter)
fh.setLevel(logging.DEBUG)

# регистратор верхнего уровня
logger = logging.getLogger('app.server')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

# отладка
if __name__ == '__main__':
    logger.debug('Отладочная информация')
    logger.info('Информационное сообщение')
    logger.warning('Предупреждение')
    logger.error('Ошибка')
    logger.critical('Критическая ошибка')
