'''
Задача 3. Число наоборот 2
Что нужно сделать
Пользователь вводит два числа — N и K. Напишите программу, которая заменяет каждое число на число,
которое получается из исходного записью его цифр в обратном порядке, затем складывает их, снова
переворачивает и выводит ответ на экран.

Пример:
Введите первое число: 102
Введите второе число: 123
Первое число наоборот: 201
Второе число наоборот: 321
Сумма: 522
Сумма наоборот: 225'''

def revers(number):
    revers_number = number[::-1]
    return int(revers_number)
def summ_revers(first, second):
    result = first + second
    print('Сумма: ', result)
    x = str(result)
    rev_result = x[::-1]
    print('Сумма наоборот: ', rev_result)

first_num = input('Введите первое число: ')
first = revers(first_num)
second_num = input('Введите второе число: ')
second = revers(second_num)

print('Первое число наоборот: ', first)
print('Второе число наоборот: ', second)

summ_revers(first, second)




