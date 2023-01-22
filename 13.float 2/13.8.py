'''Задача 8. Сумма ряда
Что нужно сделать

Пользователь вводит действительное число х и точность precision.
Напишите программу, которая по числу х вычисляет сумму ряда в точности до precision.

Операцией возведения в степень и функцией factorial пользоваться нельзя.
Пример:
Введите точность: 0.001
Введите x: 5
Сумма ряда =  0.2836250150891709
'''

def summ_1(precision, x):
    i = 0
    start = 0
    current = 1
    fn = 1
    xn = 1
    while abs(current - start) > precision:
        start = current
        xn *= x * x
        i += 1
        fn *= 2 * i *(2 * i - 1)
        if i % 2 != 0:
            current += -1 * xn / fn
        else:
            current += 1 * xn / fn
    return current


precision = float(input('Введите необходимую точность: '))
x = float(input('Введите действительное число: '))
summ1 = summ_1(precision, x)
print('Сумма ряда =', summ1)
