'''
Задача 2. Функция максимума
Что нужно сделать
Юра пишет различные полезные функции для Питона, чтобы остальным программистам стало проще работать.
Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения
максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения
максимума уже от трёх чисел?

Помогите написать Юре, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения
максимума из двух чисел
'''

def max_number(first, second):
    if first > second:
        result = first
    elif second > first:
        result = second
    else:
        result = second = first
    return result


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

max_num = max_number(first, second)
max_num = max_number(max_num, third)

print(max_num)

