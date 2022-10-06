'''Задача 8. Контакты 3
Что нужно сделать
Мы уже помогали Степану с реализацией телефонной книги на телефоне, однако внезапно оказалось, что книге не хватает
ещё одной полезной функции: поиска.
Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить: добавить
контакт или найти человека в списке контактов по фамилии.
Действие «добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона, добавляет их в словарь
и выводит на экран текущий словарь контактов. Если этот человек уже есть в словаре, то выводится соответствующее сообщение.
Действие «поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты с такой фамилией и их номера
телефонов. Поиск не должен зависеть от регистра символов.

Пример работы программы:
Введите номер действия:
 1. Добавить контакт
 2. Найти человека
1
Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
Введите номер телефона: 888
Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
Введите номер действия:
 1. Добавить контакт
 2. Найти человека
1

Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
Такой человек уже есть в контактах.
Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
Введите номер действия:
 1. Добавить контакт
 2. Найти человека
1

Введите имя и фамилию нового контакта (через пробел): Алиса Петрова

Введите номер телефона: 999

Текущий словарь контактов: {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}

Введите номер действия:

 1. Добавить контакт

 2. Найти человека

2

Введите фамилию для поиска: Сидоров

Иван Сидоров 888

Введите номер действия:

 1. Добавить контакт

 2. Найти человека

…….

'''
phone_book = {('Иван', 'Сидоров'): 888}

while True:
    print('Введите номер действия: ', '\n1. Добавить контакт', '\n2. Найти человека')
    question = int(input())
    if question == 1:
        name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
        phone = int(input('Введите номер телефона: '))
        if name in phone_book.keys():
            print('Такой человек уже есть в контактах')
        else:
            phone_book[name] = phone
        print('Текущий словарь контактов:', phone_book)
    elif question == 2:
        surname = ((input('Введите фамилию для поиска: ').lower()).title())
        for fio, tel in phone_book.items():
            if surname.lower() in fio:
                print(*fio, tel)
    else:
        print('Ошибка выбора действия, повторите ввод')
