'''Задача 3. Дзен Пайтона 2
Что нужно сделать

Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк в файле zen.txt
(который содержит всё тот же Дзен Пайтона). Выведите три найденных числа на экран.

Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.

Обратите внимание, что регистр буквы не имеет значение. (А и а - одинаковые буквы).

Формат вывода:

Количество букв в файле:
Количество слов в файле:
Количество строк в файле:
Наиболее редкая буква: '''

text = open("zen.txt").read().lower()
letters = [i_elem for i_elem in text if i_elem in "abcdefghijklmnopqrstuvwxyz"]


print('Количество букв в файле: ', len(letters))
print('Количество слов в файле: ', len(text.split()))
print('Количество строк в файле: ', len(text.split()))
print('Наиболее редкая буква: ', min(letters, key=letters.count))

