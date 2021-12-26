# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление
# в формат Unicode и также проверить тип и содержимое переменных.


print("*******№1******")
print()
str_1 = "разработка"
str_2 = "сокет"
str_3 = "декоратор"

print(type(str_1), f'content: {str_1}')
print(type(str_1), f'content: {str_2}')
print(type(str_1), f'content: {str_3}')
print()

str_1_uc_converted = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
str_2_uc_converted = "\u0441\u043e\u043a\u0435\u0442"
str_3_uc_converted = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440\u000a"
print(type(str_1_uc_converted), f'content: {str_1_uc_converted}')
print(type(str_2_uc_converted), f'content: {str_2_uc_converted}')
print(type(str_3_uc_converted), f'content: {str_3_uc_converted}')
print()

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе.
# Сделать это небходимо в автоматическом, а не ручном режиме с помощью добавления
# литеры b к текстовому значению, (т.е. ни в коем случае не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.


print("*******№2******")
print()


def b_converter(some_arr):
    for w in some_arr:
        bw = eval(f'b"{w}"')
        print(type(bw), f'content: {bw}, length: {len(bw)}')
    return ''


if __name__ == '__main__':
    w_1 = "class"
    w_2 = "function"
    w_3 = "method"

    w_arr = [_ for _ in (w_1, w_2, w_3)]

    b_converter(w_arr)

print()


# 3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе.
# Для проверки правильности работы кода используйте значения:
# «attribute», «класс», «функция», «type»


def check_byte_type(data_arr):
    for w in data_arr:
        if w.isascii():
            bw = eval(f'b"{w}"')
            print(type(bw), bw)
        else:
            print(f'"{w}" is not ASCII! bytes can only contain ASCII literal characters')
    return ''


if __name__ == '__main__':
    print("*******№3******")
    print()
    w1 = "attribute"
    w2 = "класс"
    w3 = "функция"
    w4 = "type"

    w_arr = [_ for _ in (w1, w2, w3, w4)]

    check_byte_type(w_arr)

print()

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).


print("*******№4******")


def convert_str_to_bytes(some_str_arr):
    byte_arr = []
    for some_str in some_str_arr:
        if type(some_str) != str:
            print(f"{some_str} is not a string")
        else:
            byte_arr.append(some_str.encode("utf-8"))
    return byte_arr


def convert_bytes_to_str(some_byte_arr):
    str_arr = []
    for some_byte in some_byte_arr:
        if type(some_byte) != bytes:
            print(f"{some_byte} is not bytes class")
        else:
            str_arr.append(some_byte.decode("utf-8"))
    return str_arr


if __name__ == '__main__':

    data_1 = "разработка"
    data_2 = "администрирование"
    data_3 = "protocol"
    data_4 = "standard"
    data_5 = 733

    data_list = [_ for _ in (data_1, data_2, data_3, data_4, data_5)]

    bytes_arr = convert_str_to_bytes(data_list)
    for b in bytes_arr:
        print(b)

    print("--------------")

    bytes_arr.append("dfudcdfu")

    str_list = convert_bytes_to_str(bytes_arr)
    for s in str_list:
        print(s)

    print()

    #
    # print(convert_bytes_to_str("gydgvydgsy"))
print()

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый (предварительно определив кодировку выводимых сообщений).

import platform
import subprocess
import chardet


def do_server_pinged(some_url):
    if type(some_url) != str:
        print(f"{some_url} is not a web-address")
        return ""

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', some_url]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
    return ""


if __name__ == '__main__':
    print("*******№5******")
    print()
    web_source_1 = 'yandex.ru'
    web_source_2 = 'youtube.com'
    do_server_pinged(7)
    do_server_pinged(web_source_1)
    do_server_pinged(web_source_2)

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку созданного файла
# (исходить из того, что вам априори неизвестна кодировка этого файла!).
# Затем открыть этот файл и вывести его содержимое на печать.
# ВАЖНО: файл должен быть открыт без ошибок вне зависимости от того,
# в какой кодировке он был создан!


from chardet import detect

print("*******№6******")
print()

file_name = "test_file.txt"
data_list = ["сетевое программирование", "сокет", "декоратор"]

# записываем в файл:
with open(file_name, "w", encoding="utf-8") as test_file:
    for row_content in data_list:
        test_file.write(row_content + "\n")

# определяем кодировку файла:
with open(file_name, "rb") as test_file:
    file_encoding = detect(test_file.read())["encoding"]
    print("encoding:", file_encoding)

print()

# читаем из файла
print(f"Содержимое файла {file_name}:")
with open(file_name, "r", encoding=file_encoding) as test_file:
    file_content = test_file.readlines()
    print("", *file_content)
    # for line in r:
    #     print(line)

