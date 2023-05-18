'''Задача 2. Пути файлов
Что нужно сделать
Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам указанной директории
(по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов.
В решении не нужно использовать рекурсию.

Подсказка: вместо написания кода с рекурсией используйте готовую рекурсивную функцию os.walk() — os — Miscellaneous
operating system interfaces — Python 3.11.0 documentation.'''

import os

default = os.path.join('\рабочая папка')
def gen_files_path(directori: str, search_elem: str):
    for dirpath, dirnames, filenames in os.walk(directori):
        if search_elem in dirnames or search_elem in filenames:
            yield dirpath

cnt = 0
search_elem = input('Введите нужный каталог и файл: ')

for i in gen_files_path(default, search_elem):
    cnt += 1
    print(i)
if cnt == 0:
    print('Файл или папка не найдены')

