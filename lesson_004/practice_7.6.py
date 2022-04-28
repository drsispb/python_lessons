'''Задача 1. Тайны археологии


Что нужно сделать

Археолог Ирина в последней экспедиции нашла древнюю глиняную табличку
с числами 114 12 14 10605 4907 450. Ирина предположила, что это шифр,
который можно расшифровать с помощью компьютерной программы.

Помогите Ирине — напишите программу, которая будет выводить на экран
числа, соответствующие следующему условию: они чётные и не делятся на три.
Для подходящих чисел программа выводит сообщение «Число подходит».
Для неподходящих под условие — «Число не подходит».'''

# for number in 114, 12, 14, 10605, 4907, 450:
#     if number % 3 == 0 and number % 2 == 0:
#         print(number, '«Число подходит»')
#     else:
#         print(number, '«Число не подходит»')


''' Задача 2. Должники


Что нужно сделать

В базе банка хранятся данные и должников, и законопослушных граждан. 
Каждому человеку система присваивает свой номер. У нас есть случайная выборка 
из десяти номеров. Правда, иногда база глючит и выдаёт нам номер с отрицательным 
значением. А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь
брал кредит и не выплатил его вовремя, то есть является должником.

Напишите программу, которая при вводе десяти чисел определяет, 
сколько из них являются одновременно чётными и положительными.'''

# count = 0
# for i in range(10):
#   client = int(input('Введите номер клиента '))
#   if client > 0 and client % 2 == 0:
#       count += 1
# print('Всего должников: ', count)



''' Задача 3. Посчитай чужую зарплату...


Что нужно сделать

Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании и, 
чтобы облегчить себе жизнь, обратилась к программисту.

Напишите программу, которая принимает от пользователя зарплату сотрудника за 
каждый из 12 месяцев и выводит на экран среднюю зарплату за год.'''

# month = 0
# pay_sum = 0
# for count in range(12):
#     pay = int(input('Введите оплату: '))
#     pay_sum += pay
#     month += 1
# pay_mid = pay_sum / month
# print('Средняя зарплата за', month, 'месяцев:', pay_mid)


'''Задача 4. С заботой о природе

Огромный заповедник поделён на большое количество секторов. Все сектора 
пронумерованы. Вы устроились на работу лесничим и отвечаете за группу секторов с номерами 30–35.

В ваши обязанности входит:

следить за тем, чтобы посетителей в каждом секторе было не больше десяти;
фиксировать количество нарушений этого правила.
Напишите программу, которая для каждого сектора запрашивает текущее количество 
людей в нём, и если оно больше десяти, то фиксирует нарушение. В конце выведите количество нарушений.'''

# count = 0
# for sector in (30, 31, 32, 33, 34, 35):
#     print('Вы проверяете сектор', sector)
#     how_human = int(input('Введите количество посетителей в секторе: ' ))
#     if how_human > 10:
#         count += 1
# print('Зафиксированно: ', count, 'нарушений численности')


'''Задача 5. Факториал

Мы всё ближе и ближе подбираемся к серьёзной математике. Одна из классических задач — 
задача на нахождение факториала числа. И в будущем мы с ней ещё встретимся.

Дано натуральное число n. Напишите программу, которая находит n! (n-факториал).
Запись n! означает следующее:
n! = 1 * 2 * 3 * 4 * 5 * … * n'''
# x_faktorial = 1
# number = int(input('Введите число для которого необходимо найти факториал: '))
# # number = number + 1
# for x in range(2, number + 1):
#     x_faktorial *= x
# print('Ваш факториал:', x_faktorial)

'''Задача 6. Успеваемость в классе

В классе N человек. Каждый из них получил за урок по информатике 
оценку: 3, 4 или 5, двоек сегодня не было. Напишите программу, 
которая получает список оценок — N чисел — и выводит на экран сообщение 
о том, кого сегодня больше: отличников, хорошистов или троечников.

Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.'''
# count_5 = 0
# count_4 = 0
# count_3 = 0
# study = int(input('Введите количество учеников: '))
# for x in range(study):
#     grade = int(input('Введите оценку ученика: '))
#     if grade == 5:
#         count_5 += 1
#     elif grade == 4:
#         count_4 += 1
#     elif grade == 3:
#         count_3 += 1
# if count_5 > count_3 and count_5 > count_4:
#     print('сегодня больше отличников')
# elif count_4 > count_3 and count_4 > count_5:
#     print('сегодня больше хорошистов')
# elif count_3 > count_5 and count_3 > count_5:
#     print('сегодня больше трочников')




'''Задача 7. Отрезок


Что нужно сделать

Напишите программу, которая считывает с клавиатуры два числа a и b, 
считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.'''


# one_numer = int(input('Введите число а: '))
# two_numer = int(input('Введите число b: '))
# count = 0
# number_sum = 0
# for number in range(one_numer,two_numer + 1):
#     if number % 3 == 0:
#         count += 1
#         number_sum += number
# mid_number = number_sum / count
# print('число полученное из Вашего отрезка: ', int(mid_number))
# print(count)

'''Задача 8. Замечательные числа


Что нужно сделать

Напишите программу, которая находит и выводит все двузначные числа, которые 
равны утроенному произведению своих цифр. К таким относятся, например, 15 и 24.'''


# for number in range(10,100):
#     number_1 = number // 10
#     number_2 = number % 10
#     total_number = (number_1 * number_2) + (number_1 * number_2) + (number_1 * number_2)
#     if total_number == number:
#         print(number)

'''Задача 9. ...Теперь можно посчитать и свою


Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно, 
а не зря ли она работает столько времени на одном месте? Ей захотелось узнать, 
увеличивается ли её зарплата с каждым месяцем или нет.

Пользователь вводит десять чисел. Напишите программу, которая проверяет, упорядочены ли они по возрастанию.'''
# pay_last = 0
# count = 0
# for x in range(10):
#     pay = int(input('Введите размер оплаты: '))
#     if pay < pay_last:
#         print('Не упорядочены')
#         break
#     else:
#         pay_last = pay
#         count += 1
# if count == 10:
#     print('Упорядочены')
'''Второй вариант, с вводом именно 10 чисел'''
# pay_last = 0
# count = 0
# for x in range(10):
#     pay = int(input('Введите размер оплаты: '))
#     if pay < pay_last:
#         continue
#     else:
#         pay_last = pay
#         count += 1
# if count == 10:
#     print('Упорядочены')
# else:
#     print('НЕ упорядочены')





'''Задача 10. Пропавшая карточка


Что нужно сделать

Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. 
Напишите программу, которая поможет найти потерянную карточку, если номера оставшихся известны. 
Найдите её, зная номера оставшихся карточек.

Введите число карточек — N.

Затем введите N - 1 номера оставшихся карточек. Они могут быть введены в любом порядке.'''

# total_card = int(input('Введите общее количество карт: '))
# count = 0
# sum_card = 0
# for un_card in range(1, total_card + 1):
#     sum_card += un_card
# while count != total_card - 1:
#     card = int(input('Введите известные карты: '))
#     sum_card -= card
#     count += 1
# print('Номер потерянной карты: ', sum_card)
