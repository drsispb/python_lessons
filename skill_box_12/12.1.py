'''
Задача 1. Сумма чисел
Что нужно сделать

Напишите функцию summa_n, которая принимает одно целое положительное число N и
выводит сумму всех чисел от 1 до N включительно.
Пример работы программы:
Введите число: 5
Я знаю, что сумма чисел от 1 до 5 равна 15

Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода;
формат вывода соответствует примеру;
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

'''
def summa_n():
    count = 0
    if n < 0:
        print('Ошибка ввода')
    else:
        for x in range (1, n + 1):
            count += x
        print('Я знаю, что сумма чисел от 1 до', n, 'равна', count)


n = int(input('Введите целое положительное число: '))
summa_n()
