#
# def aboutWater(price):
#     print('Название: КлирВотер')
#     print('Производитель: ВодЗавод')
#     print('цена:', price)
#
# aboutWater('25')
#
# aboutWater('30')
#
# aboutWater('40')
#
# def sphereArea():
#     s=4*3.14*(R**2)
#     print(s)
# def sphereVolume():
#     v=4/3*3.14*(R**3)
#     print(v)
#
# R=int(input())
# sphereArea()
# sphereVolume()
# def srednee():
#     sum = 0
#     count = 0
#     for i in range(choice_left, choice_right + 1):
#         sum += i
#         count += 1
#     print(sum / count)
#
#
# choice_left = int(input('Введите левую границу:'))
# choice_right = int(input('Введите правую границу:'))
# if choice_left < choice_right:
#     srednee()
# else:
#     print('Ошибка ввода')

def mail (f_n, s_n, country, sity, street, h, kv):
    print('Фамилия: ', f_n)
    print('Имя: ', s_n)
    print('Страна:', country)
    print('Город: ', sity)
    print('Улица: ', street)
    print('дом: ', h)
    print('квартира :', kv)
    print(f_n, s_n, country, sity, street, h, kv)

f_n = input('enter surname: ')
s_n = input('enter name: ')
country = input('enter country: ')
sity = input('enter sity: ')
street = input('enter street: ')
h = int(input('enter house: '))
kv = int(input('enter flat: '))

mail (f_n, s_n, country, sity, street, h, kv)
