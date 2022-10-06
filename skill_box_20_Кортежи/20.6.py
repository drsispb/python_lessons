'''
Задача 6. По парам
Что нужно сделать
Напишите программу, которая инициализирует список из 10 случайных целых чисел, а затем делит эти числа на пары кортежей
внутри списка. Выведите результат на экран.
Дополнительно: решите задачу несколькими способами.
Пример:
Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
'''
from random import randint

#1
original = [randint(0, 40) for i in range(10)]
print('Оригинальный список: ', original)

new_original = [*map(tuple, zip(original[::2], original[1::2]))]
print('Новый список: ', new_original)

#2
res_lst = []
origin_lst = [randint(0, 40) for j in range(10)]

for index, item in enumerate(origin_lst):
  if index % 2 != 0:
    res_lst.append((origin_lst[index - 1], item))

print('Оригинальный список: ', origin_lst)
print('Новый список: ', res_lst)