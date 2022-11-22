'''Задача 6. Паранойя
Что нужно сделать

Артуру постоянно кажется, что за ним следят и все хотят своровать «крайне важную информацию» с его компьютера,
включая переписку с людьми. Поэтому он эти переписки шифрует. И делает это с помощью шифра Цезаря
(чем веселит агента службы безопасности).

Напишите программу, которая шифрует содержимое текстового файла text.txt шифром Цезаря, при этом символы первой строки
файла должны циклически сдвигаться на один, второй строки — на два, третьей строки — на три и так далее.
Результат выведите в файл cipher_text.txt.
Пример:
Содержимое файла text.txt:
Hello
Hello
Hello
Hello

Содержимое файла cipher_text.txt:
Ifmmp
Jgnnq
Khoor
Lipps'''

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def cesar(message, step):
    schifer = [alfabet[(alfabet.index(i) + step) % len(alfabet)] if i in alfabet else i for i in message]
    return ''.join(schifer)


file = open('text.txt', 'r')
cipher_file = open('cipher_text.txt', 'w')
data = file.read()

cnt = 1
for i_word in data:
    if i_word == '\n':
        cnt += 1
    word = cesar(i_word,cnt)
    cipher_file.write(word)

file.close()
cipher_file.close()