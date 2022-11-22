'''Задача 2. Дзен Пайтона
Что нужно сделать

В файле zen.txt хранится так называемый Дзен Пайтона — текст философии программирования на языке Python. Выглядит он так:

Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.

Кстати, попробуйте открыть консоль Python и ввести команду “import this”.'''

txt_file = open('zen.txt', 'r')
txt_file_list = []
for i_elem in txt_file:
    txt_file_list.append(i_elem)

for i_elem_list in txt_file_list[::-1]:
    print(i_elem_list, end='')

txt_file.close()

