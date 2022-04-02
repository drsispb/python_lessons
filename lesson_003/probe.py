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
total = 0
for x in goods:
    print (x, goods[x])
for y in store:
    if y == '12345':
        print ('Ламп на складе', store [y])
    elif y == '23456':
        print('Столов на складе', store[y])
    elif y == '34567':
        print('Диванов на складе', store[y])
    elif y == '34567':
        print('Диванов на складе', store[y])

