'''Задача 4. Урок информатики 3
Что нужно сделать
Наконец-то учитель смог объяснить детям, что такое эта «плавающая точка». Однако долго его радость не продлилась,
ведь на следующем уроке нужно будет объяснить такие страшные слова, как «экспоненциальное», «мантисса» и «порядок».
Хоть старшеклассники и знакомы с экспонентой, учитель всё равно не уверен, что здесь всё будет понятно. Поэтому для
наглядности он также написал программу.

На вход подаётся строка — это экспоненциальная форма числа. Напишите программу, которая выводит отдельно мантиссу и
отдельно порядок этого числа.'''

def mantice(num):
    res = ''
    for i in num:
        if i != 'e':
            res += i
        elif i == 'e':
            manticce = res
            res = ''
    print('Мантиса введенного числа:', manticce)
    print('Порядок введенного числа:', res)


num = input('Введите число в эспоненциальной форме: ')

mantice(num)


num = input('Введите экспоненциальную форму числа: ')

print(num)
