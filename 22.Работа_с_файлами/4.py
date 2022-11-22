'''Задача 4. Файлы и папки
Что нужно сделать

Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска) и выводит общее
количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.

Результат работы программы на примере python_basic\Module14:

E:\PycharmProjects\python_basic\Module14
Размер каталога (в Кб): 8.373046875
Количество подкаталогов: 7
Количество файлов: 15'''

import os

for _ in range(3):
    path = os.getcwd()
    os.chdir("..")

path = os.path.join(path, 'python')
print(path)
file_list = []
cat_list = []


def get_size(way, sum_size=0, total_file=0):
    dir_list = os.listdir(way)
    for i_file in dir_list:
        current_obj = os.path.abspath(os.path.join(way, i_file))
        if os.path.isfile(current_obj):
            file_list.append(current_obj)
        elif os.path.isdir(current_obj):
            cat_list.append(current_obj)
            get_size(current_obj, sum_size)
    return file_list, cat_list


res_list_file, res_list_dir = get_size(path)
total_size = 0
for i_elem in res_list_file:
    total_size += os.path.getsize(i_elem)

print('Размер каталога (в Кб): {}'.format(total_size / 1024))
print('Количество подкаталогов: {}'.format(len(res_list_dir)))
print('Количество файлов: {}'.format(len(res_list_file)))