'''Задача 2. Пути файлов
Что нужно сделать
Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам указанной директории
(по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов.
В решении не нужно использовать рекурсию.

Подсказка: вместо написания кода с рекурсией используйте готовую рекурсивную функцию os.walk() — os — Miscellaneous
operating system interfaces — Python 3.11.0 documentation.'''

''' есть у меня подозрение, что задачу я не так понял, но вот как то так'''

import os

default = os.path.abspath('C:/')
def gen_files_path(directori: str, catalog: str):
    if os.path.isdir(directori + '\\' + catalog):
        for i in os.walk(directori + '\\' + catalog):
            print(i)
    else:
        print('Такой каталог не найден')




dir_path = input('Введите нужную директорию: (если требуется проход по корневому диску, просто нажмите "enter") ')
cat_path = input('Введите нужный каталог: ')

gen_files_path(default + dir_path, cat_path)

