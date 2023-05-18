'''Задача 1. Квадраты чисел
Что нужно сделать
Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N
(1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите тремя способами: класс-итератор,
функция-генератор и генераторное выражение.'''

numN = int(input('Введите число N: '))

'''класс-итератор'''
class Iterator:
    def __init__(self, limit):
        self.limit = limit
        self.__start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start < self.limit:
            self.__start += 1
            return self.__start ** 2
        else:
            raise StopIteration

itter_cl = Iterator(numN)
for i in itter_cl:
    print(i, end=' ')

print('\n')
'''фукция-генератор'''

def iterator(num):
    for i_num in range(1, num + 1):
        yield i_num ** 2


for i in iterator(numN):
    print(i, end=' ')

print('\n')
'''генераторное выражение'''
expression = (num ** 2 for num in range(1, numN + 1))
for i_num in expression:
    print(i_num, end=' ')