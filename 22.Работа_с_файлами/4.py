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


def file_sizes(path):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1

        else:
            result = file_sizes(os.path.abspath(os.path.join(path, i_elem)))
            files_stat[0] += result[0]
            files_stat[1] += result[1]
            files_stat[2] += 1
    return files_stat


path = os.path.abspath(os.path.join('..', '..', 'python'))

result = file_sizes(path)
print('Размер каталога (в Кб):', result[0] / 1024)
print('Количество файлов:', result[1])
print('Количество подкаталогов:', result[2])