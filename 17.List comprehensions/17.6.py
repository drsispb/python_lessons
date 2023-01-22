'''Задача 6. Сжатие списка
Что нужно сделать

Дан список из N целых случайных чисел (число от 0 до 2). Напишите программу,
которая выполняет «сжатие списка» — переставляет все нулевые элементы в конец массива. При этом все
ненулевые элементы располагаются в начале массива в том же порядке. Затем все нули из списка удаляются.

Пример:
Количество чисел в списке: 10
Список до сжатия: [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
Список после сжатия: [2, 1, 1, 2]'''
import random

N = int(input('Количество чисел в списке: '))

fst = [random.randint(0, 2) for _ in range(N)]
print('Список до сжатия: ', fst)

scnd = [x for x in fst if x]
print(scnd)