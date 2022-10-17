'''Задача 4. Поиск элемента 2
Что нужно сделать
Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень,
до которого будет просматриваться структура.
Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран.
По умолчанию уровень не задан. В качестве примера можно использовать такой словарь:
Пример 1:
Введите искомый ключ: head
Хотите ввести максимальную глубину? Y/N: n
Значение ключа: {'title': 'Мой сайт'}
Пример 2:
Введите искомый ключ: head
Хотите ввести максимальную глубину? Y/N: y
Введите максимальную глубину: 1
Значение ключа: None'''

def search_y(data, tag, depth):
    result = None
    if depth == 1:
        if tag in data:
            return data[tag]
    elif depth > 1:
        cnt = 1
        for key, value in data.items():
            if isinstance(value, dict) and cnt < depth:
                result = search_n(value, tag)
                cnt += 1
                if result:
                    return result
    else:
        return result

def search_n(data, tag):
    result = None
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_n(value, tag)
            if result:
                return result
    return result

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

while True:
    ask_key = input('Введите искомый ключ: ')
    ask_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if ask_depth == 'y':
        depth = int(input('Введите максимальную глубину: '))
        print('Значение ключа: ', search_y(site, ask_key, depth))
    elif ask_depth == 'n':
        print('Значение ключа: ', search_n(site, ask_key))
    else:
        print('Некорректный выбор глубины, повторите')
