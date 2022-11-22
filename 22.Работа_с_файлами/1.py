'''Задача 1. Сумма чисел 2
Что нужно сделать
Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк.
Напишите программу, которая выводит сумму чисел в выходной файл answer.txt.

Пример:
Содержимое файла numbers.txt
     2
2
  2
        2

Содержимое файла answer.txt
8'''

text_file = open('answer.txt', 'r')

count = 0
for i_elem in text_file:
    count += int(i_elem)
print(count)

text_file.close()
