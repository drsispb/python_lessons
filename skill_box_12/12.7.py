'''Задача 7. Опять?
Что нужно сделать
Вы снова встретились со своим старым другом, который был безмерно благодарен вам за то,
что вы помогли ему сдать задачу тому преподавателю. Вот только друг всё равно выглядел довольно
грустным. Когда вы спросили, в чём дело, друг взорвался эмоциями и рассказал, что теперь препод
попросил написать функцию нахождения минимального числа без использования условного оператора и циклов.
Конечно же, вы решили снова помочь бедняге. Напишите для него такую программу.

Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода;
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).'''

def serach_min():
    x1 = abs(firth - second)
    x2 = abs(firth + second)
    x3 = (abs(x2) - abs(x1)) / 2
    print('Наименьшее число: ', int(x3))

firth = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
serach_min()