'''
Задача 8. НОД
Что нужно сделать
Напишите функцию, вычисляющую наибольший общий делитель двух чисел.

Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода;
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).
'''

def search_max_del():
    x = 0
    if firth > second:
        for i in range(1, firth + 1):
            if firth % i == 0 and second % i == 0:
                x = i
            else:
                continue
        print(x)
    else:
        for i in range(1, second + 1):
            if firth % i == 0 and second % i == 0:
                x = i
            else:
                continue
        print(x)




firth = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
search_max_del()
