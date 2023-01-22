'''
Задача 8. НОД
Что нужно сделать
Напишите функцию, вычисляющую наибольший общий делитель двух чисел.

Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода;
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).
'''

# def search_max_del(firth, second):
#     x = 0
#     if firth > second:
#         i = second
#     else:
#         i = firth
#     for num_end in range(1, i + 1):
#         if firth % num_end == 0 and second % num_end == 0:
#             x = num_end
#     print('Наибольший общий делитель:', x)
#
#
# firth = int(input('Введите первое число: '))
# second = int(input('Введите второе число: '))
# search_max_del(firth, second)

'''"типо правильный вариант'''

def search_evklid(a, b):
    while a != 0 and b != 0:
        if a > b:
           a = a % b
        else:
            b = b % a
    print(a + b)


firth = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

search_evklid(firth, second)