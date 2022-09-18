'''Задача 10. Снова палиндром
Что нужно сделать
Пользователь вводит строку. Необходимо написать программу, которая определяет, существует ли у этой строки такая
перестановка, при которой она станет палиндромом. Выведите соответствующее сообщение.

Пример 1:
Введите строку: aab
Можно сделать палиндромом

Пример 2:
Введите строку: aabc
Нельзя сделать палиндромом'''

check_word = input('Введите строку: ')
check = set()

for i in check_word:
    if i in check:
        check.remove(i)
    else:
        check.add(i)

if len(check) <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')