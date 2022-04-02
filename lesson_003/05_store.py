# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# TODO здесь ваш код
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for x in goods:
    print (x, goods[x])


total_quantity_c = 0
total_price_c = 0
store_chair = store ['45678']
for chair in store_chair:
    total_quantity_c += chair['quantity']
    total_price_c += chair['price']
print('Стул -',  total_quantity_c, 'шт, стоимость', total_price_c, 'руб.')

total_quantity_t = 0
total_price_t = 0
store_table = store ['23456']
for table in store_table:
    total_quantity_t += table ['quantity']
    total_price_t += table ['price']
print('Стол -',  total_quantity_t, 'шт, стоимость', total_price_t, 'руб.')


total_quantity_l = 0
total_price_l = 0
store_lamp = store ['12345']
for lamp in store_lamp:
    total_quantity_l += lamp ['quantity']
    total_price_l += lamp ['price']
print('Лампа -',  total_quantity_l, 'шт, стоимость', total_price_l, 'руб.')

total_quantity_s = 0
total_price_s = 0
store_sofa = store['34567']
for sofa in store_sofa:
    total_quantity_s += sofa ['quantity']
    total_price_s += sofa ['price']
print('Диван -',  total_quantity_s, 'шт, стоимость', total_price_s, 'руб.')
