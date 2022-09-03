'''Задача 9. Сообщение
Что нужно сделать
Вашему другу надоело общаться простыми сообщениями, и он решил делать это необычным способом: он переворачивает
каждое слово в тексте, при этом не трогая знаки препинания.
Пользователь вводит текст, состоящий из слов и знаков препинания. Напишите программу, которая переворачивает
(записывает в обратном порядке) все слова текста, оставив знаки препинания без изменений. Словом в тексте считается
последовательность символов из прописных и строчных букв кириллицы.

Пример 1:
Сообщение: Это задание очень! простое.
Новое сообщение: отЭ еинадаз ьнечо! еотсорп.

Пример 2:
Сообщение: Хотя ,. возм:ожно и нет.
Новое сообщение: ятоХ ,. мзов:онжо и тен.'''

def reverse_word(word):
    return ''.join(reversed(word))

symbol = '!#$%&()*+,-./:;<=>?@[\]^_`{|}~'
text = input('Сообщение: ').split()
result = []

for word in text:
    word_part = ''
    word_back = ''
    for sym in word:
        if not sym in symbol:
            word_part += sym
        else:
            word_back += reverse_word(word_part) + sym
            word_part = ''

    word_back += reverse_word(word_part)
    result.append(word_back)

print('Новое сообщение:', *result)