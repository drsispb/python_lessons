'''Задача 3. Количество строк
Что нужно сделать
Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет количество строк в каждом
файле, игнорируя пустые строки и строки комментариев. По итогу функция-генератор должна с помощью yield каждый
раз возвращать количество строк в очередном файле.'''

import os

def get_str_file_py(def_path: str):
    for dirs, folder, files in os.walk(def_path):
        for file in files:
            if str(file).endswith('.py'):
                with open(os.path.join(dirs, file), 'r', encoding='utf-8') as open_file:
                    yield open_file


defaut_path = 'C:/Users/Питер Паркер/PycharmProjects/python_lessons/12.Функции'

for i_cnt in get_str_file_py(defaut_path):
    count = 0
    for i_open_file in i_cnt:
        if i_open_file != '\n':
            count += 1
    print('Количество строк в файле ', i_cnt.name, ' - ', count)
