'''Задача 6. Сжатие
Что нужно сделать

С увеличением объёма данных возникла потребность в сжатии этих данных без потери важной информации.
Для этого было придумано кодирование, которое осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
на этот символ и количество его повторений в этой позиции строки.
Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
последовательность на экран. Кодирование должно учитывать регистр символов.

Пример:
Введите строку: aaAAbbсaaaA
Закодированная строка: a2A2b2с1a3A1'''

word =(input('Введите строку: '))
count = 0
shifr = ''

for i in range(len(word)):
    sim = word[i]
    count += 1
    if i == len(word) - 1:
        shifr = shifr + word[i] + str(count)
        break
    if word[i] != word[i+1]:
        shifr = shifr + word[i] + str(count)
        count = 0
print (shifr)
