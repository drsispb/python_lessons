'''Задача 9. Родословная
Что нужно сделать
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. Каждому элементу дерева
сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого
элемента высота на один больше, чем у его родителя. Вам нужно написать программу, которая по заданному генеалогическому
древу определяет высоту всех его элементов.
Программа получает на вход N количество человек в генеалогическом древе. Далее следует N − 1 строк, в каждой из которых
задаётся родитель для каждого элемента дерева, кроме родоначальника. Каждая строка имеет вид «имя_потомка имя_родителя».
Программа должна вывести список всех элементов древа в лексикографическом порядке (по алфавиту). После вывода имени
каждого элемента необходимо вывести его высоту.

Пример:7
Введите количество человек: 9
Первая пара: Alexei Peter_I
Вторая пара: Anna Peter_I
Третья пара: Elizabeth Peter_I
Четвёртая пара: Peter_II Alexei
Пятая пара: Peter_III Anna
Шестая пара: Paul_I Peter_III
Седьмая пара: Alexander_I Paul_I
Восьмая пара: Nicholaus_I Paul_I
«Высота» каждого члена семьи:
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2'''

def height(i):
    if i not in total_family:
        return 0
    else:
        return 1 + height(total_family[i])

order_human = int(input('Введите количество человек: '))
total_family = {}


for i in range(1, order_human):
    human = input('{0}-я пара: '.format(i))
    child, parent = human.split()
    total_family[child] = parent

heights = {}
for i in set(total_family.keys()).union(set(total_family.values())):
    heights[i] = height(i)

for key, value in sorted(heights.items()):
    print(key, value)
