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
print(new_original)

#2
original_2 = [randint(0, 40) for j in range(10)]
print('Оригинальный список: ', original_2)
k1 = (original_2[0],original_2[1])
k2 = (original_2[2],original_2[3])
k3 = (original_2[4],original_2[5])
k4 = (original_2[6],original_2[7])
k5 = (original_2[8],original_2[9])
print('Новый список: ', ([k1, k2, k3, k4, k5]))
