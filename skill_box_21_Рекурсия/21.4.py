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


def search(data, tag, depth):
    result = None
    if depth == 1:
        if tag in data:
            return data[tag]
    elif depth > 1:
        cnt = 1
        for key, value in data.items():
            if isinstance(value, dict) and cnt < depth:
                result = search(value, tag)
                cnt += 1
                if result:
                    return result
    elif depth == 0:
        for key, value in data.items():
            if isinstance(value, dict):
                result = search(value, tag)
                if result:
                    return result
    return result



while True:
    ask_key = input('Введите искомый ключ: ')
    ask_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if ask_depth == 'y':
        depth = int(input('Введите максимальную глубину: '))
        print('Значение ключа: ', search(site, ask_key, depth))
    elif ask_depth == 'n':
        print('Значение ключа: ', search(site, ask_key, depth = 0))
    else:
        print('Некорректный выбор глубины, повторите')
