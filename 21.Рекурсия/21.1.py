'''Задача 1. Challenge 2
Что нужно сделать
Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой задачу, но не сильно связанную с математикой,
а именно: написать функцию, которая выводит все числа от 1 до num_end без использования циклов. Помогите другу реализовать
такую функцию.

Пример работы программы:
Введите num_end: 10
1
2
3
4
5
6
7
8
9
10'''

def countdown (num):
    if num <= 0:
        return
    countdown(num - 1)
    print(num)

num = int(input('Введите num_end: '))
countdown(num)