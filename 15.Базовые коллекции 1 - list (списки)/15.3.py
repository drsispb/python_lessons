'''Задача 3. Клетки
Что нужно сделать
В научной лаборатории выводят и тестируют новые виды клеток. Есть список из N этих клеток, элементом которого
является показатель эффективности, а индексом — ранг клетки. Учёные отбирают клетки по следующему принципу:
если эффективность клетки меньше её ранга, то она не подходит.
Напишите программу, которая выводит на экран элементы списка, значения которых меньше их индекса.
Пример:
Количество клеток: 5
Эффективность 1 клетки: 3
Эффективность 2 клетки: 0
Эффективность 3 клетки: 6
Эффективность 4 клетки: 2
Эффективность 5 клетки: 10
Неподходящие значения: 0 2
'''

list = []
N = int(input('Количество клеток: '))
for _ in range(1,N + 1):
    list.append(_)
bad_effectiv = []
for i in list:
    effectiv = int(input('Введите эффективность '))
    if i > effectiv:
        bad_effectiv.append(effectiv)
    print('Эффективность', i, 'клетки:', effectiv)
print('Неподходящие значения:', " ".join(map(str,bad_effectiv)))