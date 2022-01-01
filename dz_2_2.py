# 2. Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
# автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров —
# товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# В это словаре параметров обязательно должны присутствовать юникод-символы,
# отсутствующие в кодировке ASCII.
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее
# значений каждого параметра.


def write_order_to_json(item, quantity, price, buyer, date):
    import json

    with open('orders.json', 'r', encoding='utf-8') as f:
        orders_data = json.load(f)

    with open('orders.json', 'w', encoding='utf-8') as f:
        orders = orders_data['orders']
        order_dict = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }

        orders.append(order_dict)
        json.dump(orders_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':

    write_order_to_json('wifi-адаптер', '8', '78€', 'ООО "Кампио"', '15 декабря 2021')
    write_order_to_json('bluetooth-колонка', '2', '5000 руб', 'ИП Иванов', '30 августа 2021')



