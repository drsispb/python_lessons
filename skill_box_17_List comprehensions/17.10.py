'''Задача 10. Шифр Цезаря
Что нужно сделать

Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по алфавиту через K позиций
по кругу. Если взять русский алфавит и K = 3, то в слове, которое мы хотим зашифровать,
буква А станет буквой Г, Б станет Д и так далее.
Пользователь вводит сообщение, а также значение сдвига. Напишите программу, которая зашифрует это сообщение
при помощи шифра Цезаря.

Пример:
Введите сообщение: это питон.
Введите сдвиг: 3
Зашифрованное сообщение: ахс тлхср.'''

alfabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
space = ' '

message = input('Введите сообщение: ').upper()
step = int(input('Введите сдвиг: '))
schifer = ''

for i in message:
    place = alfabet.find(i)
    new_place = place + step
    if i in alfabet and new_place < (len(alfabet) - 1):
        schifer += alfabet[new_place]
    elif i == space:
        schifer += space
    elif i in alfabet and new_place >= (len(alfabet) -1):
        schifer += alfabet[new_place - len(alfabet)]
    else:
        schifer += i

print('Зашифрованное сообщение: ', schifer.lower())
