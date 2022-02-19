from  sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, mapper
from common.variables import *
import datetime


# Класс  база данных Сервера:
class ServerStorage:

    # Класс AllUsers реализует таблицу всех пользователей
    # Экземпляр класса - запись в этой таблице
    class AllUsers:
        def __init__(self, username):
            self.id = None
            self.name = username
            self.last_login = datetime.datetime.now()

    # Класс ActiveUsers реализует таблицу активных пользователей:
    # Запись в этой таблице - его экземпляр
    class ActiveUsers:
        def __init__(self, user_id, ip_address, port, login_time):
            self.id = None
            self.user = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_time = login_time


    # Класс - отображение таблицы истории входов
    # Экземпляр этого класса - запись в таблице LoginHistory
    class LoginHistory:
        def __init__(self, name, date, ip, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip = ip
            self.port = port

    def __init__(self):
        # движок БД
        # SERVER_DATABASE - sqlite:///server_base.db3 - в common.variables
        # echo=False - отключает вывод на экран sql-запросов)
        #  pool_recycle=7200 (переустановка соединения через каждые 2 часа)
        self.db_engine = create_engine(SERVER_DATABASE, echo=False, pool_recycle=7200)

        self.metadata = MetaData()

        # таблица пользователей
        users_table = Table('Users', self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('name', String, unique=True),
                            Column('last_login', DateTime)
                            )

        # Создаём таблицу активных пользователей
        active_users_table = Table('Active_users', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('user', ForeignKey('Users.id'), unique=True),
                                   Column('ip_address', String),
                                   Column('port', Integer),
                                   Column('login_time', DateTime)
                                   )

        # Создаём таблицу истории входов
        user_login_history = Table('Login_history', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('name', ForeignKey('Users.id')),
                                   Column('date_time', DateTime),
                                   Column('ip', String),
                                   Column('port', String)
                                   )

        # Создаём  все таблицы
        self.metadata.create_all(self.db_engine)

        # Связываем класс в ORM с соответствующей таблицей
        mapper(self.AllUsers, users_table)
        mapper(self.ActiveUsers, active_users_table)
        mapper(self.LoginHistory, user_login_history)

        # Создаём сессию
        Session = sessionmaker(bind=self.db_engine)
        self.session = Session()

        # очищаем таблицу активных пользователей, т.к это новое подключение
        self.session.query(self.ActiveUsers).delete()
        self.session.commit()

    # Функция записывает в базу вход польователя
    def user_login(self, username, ip_address, port):
        print(username, ip_address, port)
        # Запрос в таблицу пользователей о данном пользователе
        result = self.session.query(self.AllUsers).filter_by(name=username)

        # Если пользователь уже существует, меняем время последнего входа
        if result.count():
            user = result.first()
            user.last_login = datetime.datetime.now()
        # или создание нового пользователя
        else:
            # Создаём экземпляр класса self.AllUsers - новую запись
            user = self.AllUsers(username)
            self.session.add(user)
            # Комит для присвоения ID
            self.session.commit()

        # запись в таблицу активных пользователей о факте входа.
        # Создаём экземпляр класса self.ActiveUsers, записываем данные в таблицу
        new_active_user = self.ActiveUsers(user.id, ip_address, port, datetime.datetime.now())
        self.session.add(new_active_user)

        # Создаём экземпляр класса self.LoginHistory, записываем данные в таблицу
        history = self.LoginHistory(user.id, datetime.datetime.now(), ip_address, port)
        self.session.add(history)

        # Сохраняем изменения
        self.session.commit()

    # Функция фиксирует выход пользователя
    def user_logout(self, username):
        # Запрос записи из таблицы self.AllUsers по имени
        user = self.session.query(self.AllUsers).filter_by(name=username).first()

        # Удаление пользователя из таблицы ActiveUsers
        self.session.query(self.ActiveUsers).filter_by(user=user.id).delete()

        # сохраняем
        self.session.commit()

    # Функция возвращает список всех пользователей
    def users_list(self):
        # Запрос строк таблицы пользователей.
        query = self.session.query(
            self.AllUsers.name,
            self.AllUsers.last_login
        )
        # Возвращаем список кортежей
        return query.all()

    # Функция возвращает список активных пользователей
    def active_users_list(self):
        # Запрашиваем соединение таблиц и собираем кортежи имя, адрес, порт, время.
        query = self.session.query(
            self.AllUsers.name,
            self.ActiveUsers.ip_address,
            self.ActiveUsers.port,
            self.ActiveUsers.login_time
        ).join(self.AllUsers)
        # Возвращаем список кортежей
        return query.all()

    # возвращает историю входов по всем или конткретному пользователю
    def login_history(self, username=None):
        # Запрос истории входа
        query = self.session.query(self.AllUsers.name,
                                   self.LoginHistory.date_time,
                                   self.LoginHistory.ip,
                                   self.LoginHistory.port
                                   ).join(self.AllUsers)
        # Если пользователь указан, фильтруем по его имени
        if username:
            query = query.filter(self.AllUsers.name == username)
        # Возвращаем список кортежей
        return query.all()



if __name__ == '__main__':
    testing_db = ServerStorage()
    # логирование пользователей
    testing_db.user_login('client_1', '192.168.1.4', 8080)
    testing_db.user_login('client_2', '192.168.1.5', 7777)

    #  список кортежей  активных пользователей
    print('Активные пользователи:')
    print(testing_db.active_users_list())

    # разлогирование пользователя
    testing_db.user_logout('client_1')

    # список активных пользователей
    print('Активные пользователи после выхода одного из них:')
    print(testing_db.active_users_list())

    # история входов выбранного пользователя
    print('История входов выбранного пользователя: ')
    print(testing_db.login_history('client_1'))

    # список всех пользователей
    print('Список всех пользователей: ')
    print(testing_db.users_list())
