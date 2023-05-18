'''Задача 3. Количество строк
Что нужно сделать
Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет количество строк в каждом
файле, игнорируя пустые строки и строки комментариев. По итогу функция-генератор должна с помощью yield каждый
раз возвращать количество строк в очередном файле.'''

import os

def get_str_file_py(def_path: str):
    for file in os.listdir(def_path):
        if str(file).endswith('.py'):
            yield file


defaut_path = 'C:/Users/Питер Паркер/PycharmProjects/python_lessons/12.Функции'

for i_file in get_str_file_py(defaut_path):
    count = 0
    with open(os.path.join(defaut_path, i_file), 'r', encoding='utf-8') as open_file:
        for i_str in open_file:
            if i_str.strip() != '' and '#' not in i_str:
                count += 1
    print('Количество строк в файле ', i_file, ' - ', count)


