# 3. Задание на закрепление знаний по модулю yaml.
# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
# Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
# отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml


def get_yaml_written(yaml_file, data):
    with open(yaml_file, 'w', encoding='utf-8') as yf:
        yaml.dump(data, yf, default_flow_style=False, allow_unicode=True)


def get_yaml_read(yaml_file):
    with open(yaml_file, encoding='utf-8') as yf:
        print(yf.read())


if __name__ == '__main__':
    data_list = [77, 'str1', 'str11', 101]
    num = 777
    put_in_dict = {'key1': 'ы9', 'key2': '8ь', 'key3': '465ц'}

    data_dict = {
        'key_1': data_list,
        'key_2': num,
        'key_3': put_in_dict
    }

    file_name = 'file.yaml'

    get_yaml_written(file_name, data_dict)

    get_yaml_read(file_name)
