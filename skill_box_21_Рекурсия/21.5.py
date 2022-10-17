'''Задача 5. Ускоряем работу функции
Что нужно сделать

У нас есть функция, которая делает определённые действия с входными данными:
берёт факториал от числа;
результат делит на куб входного числа;
получившееся число возводит в 10-ю степень.
def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result
Однако каждый раз нам приходится делать сложные вычисления, хотя входные и выходные данные одни и те же.
И тут наши знания тонкостей Python должны нам помочь.
Оптимизируйте функцию так, чтобы высчитывать факториал для одного и того же числа только один раз.
Подсказка: вспомните, что происходит с изменяемыми данными, если их выставить по умолчанию в параметрах функции.'''


def rec_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * rec_factorial(number - 1)


def calculating_math_func(data):
    result = rec_factorial(data) / (data ** 3)
    result = result ** 10
    return result


print(calculating_math_func(3))
