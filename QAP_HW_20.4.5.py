import json
with open('orders_july_2023.json', 'r') as my_file:
    orders_july = my_file.read()
orders = json.loads(orders_july)

#1 Какой номер самого дорогого заказа за июль?
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

#2 Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_order = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'Номер заказа с самым большим количеством товара: {max_order}, максимальное количество товара: {max_quantity}')

#3 В какой день в июле было сделано больше всего заказов?
max_quantity = 0
date = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        date = orders_data.get('date')
        max_quantity = quantity
print(f'Больше всего заказов : {max_quantity}, было сделано: {date}')

#4 Какой пользователь сделал самое большое количество заказов за июль?
max_quantity = 0
user_id = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        user_id = orders_data.get('user_id')
        max_quantity = quantity
print(f'Пользователь {user_id} сделал самое большое количество заказов : {max_quantity}')

#5 У какого пользователя самая большая суммарная стоимость заказов за июль?
max_price = 0
user_id = ''
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        user_id = orders_data.get('user_id')
        max_price = price
print(f'Самая большая суммарная стоимость заказов : {max_price}, за июль у пользователя : {user_id}')

#6 Какая средняя стоимость заказов в июле?
sum_all, count = 0, 0
for order, data in orders.items():
    sum_all += data['price']
    count += 1
print(f'Средняя стоимость заказов в июле :{sum_all/count}')

#7 Какая средняя стоимость товаров в июле?
sum_all, count = 0, 0
for order, data in orders.items():
    sum_all += data['price']
    count += quantity
print(f'Средняя стоимость товаров в июле: {sum_all/count}')