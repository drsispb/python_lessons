'''Задача 8. Частотный анализ
Что нужно сделать

Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет частотный анализ, определяя долю
каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат в файл analysis.txt.
Символы, не являющиеся буквами английского алфавита, учитывать не нужно.

В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. Буквы должны
быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.
Пример:
Содержимое файла text.txt:
Mama myla ramu.
Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083'''

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


text = open('work8.txt', 'r').read().lower()
dict_letter = {}
cnt = 0
for i_letter in text:
    if i_letter in alfabet:
       x = dict_letter.get(i_letter, 0)
       dict_letter[i_letter] = x + 1
       cnt += 1


sort_dict = sorted(dict_letter)
anal = [[i_elem, round((dict_letter[i_elem] / cnt),3)] for i_elem in sort_dict]
analysis = '\n'.join([i_elem[0] + ' ' + str(i_elem[1]) for i_elem in anal])
open('analysis.txt', 'w').write(analysis)


