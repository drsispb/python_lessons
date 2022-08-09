'''
Задача 5. Текстовый редактор
Что нужно сделать
Мы продолжаем разрабатывать новый текстовый редактор, и в этот раз нам поручили написать для него код,
который считает количество любой буквы и любой цифры в тексте (а не только буквы Ы, как раньше).
Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и букв N.
Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.
Пример:
Введите текст: 100 лет в обед
Какую цифру ищем? 0
Какую букву ищем? л
Количество цифр 0: 2
Количество букв л: 1

Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода;
формат вывода соответствует примеру;
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).
'''

def count_letters(frathe, num, letter):
    count_n = 0
    count_l = 0
    for i in list(frathe):
        if i == num:
            count_n += 1
        elif i == letter:
            count_l += 1
    print('Количество цифр ' + str(num) + ':', count_n)
    print('Количество букв ' + str(letter) + ':', count_l)

frathe = input('Введите текст: ')
num = input('Какую цифру ищем? ')
letter = input('Какую букву ищем? ')

count_letters(frathe, num, letter)

'''  123 '''