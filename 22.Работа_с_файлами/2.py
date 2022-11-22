'''Задача 2. Дзен Пайтона
Что нужно сделать

В файле zen.txt хранится так называемый Дзен Пайтона — текст философии программирования на языке Python. Выглядит он так:

Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.

Кстати, попробуйте открыть консоль Python и ввести команду “import this”.'''

import os
file = os.path.abspath('zen.txt')

txt_file = open(file, 'r')
for i_elem in reversed(txt_file.readlines()):
    print(i_elem, end='')

txt_file.close()

