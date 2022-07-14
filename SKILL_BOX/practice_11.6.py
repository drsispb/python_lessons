import math
''' Задача 1. Конвертация

Что нужно сделать
При покупках за рубежом с помощью карты банки делают конвертацию через промежуточную валюту. Например, 
если купить что-то в евро, то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.

Напишите программу, которая получает на вход стоимость покупки в евро, затем выводит ответ в рублях. 
Мы живём в альтернативной реальности, где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

Что оценивается
Задание считается успешно выполненным, если:

результат вывода соответствует условию;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);'''

# money = input('Введите стоимость покупки, в евро: ')
# dollar = float(money) * 1.25
# rub = float(dollar) * 60.87
#
# print('Сумма вашей покупке в рублях, составит: ', round(rub, 2))


'''Задача 2. Грубая математика

Что нужно сделать
В одном центре математического анализа работал практикант, который написал программу для расчёта некоторых 
функций. Правда, он в тот день очень устал и немного не так прочитал техническое задание, поэтому функции 
теперь рассчитываются довольно грубо. 

Программа работает следующим образом: вводится последовательность из N вещественных чисел. При этом 
положительные числа округляются вверх, отрицательные округляются вниз. Напишите программу, которая
выводит натуральный логарифм от числа, если оно положительное, и экспоненту в степени числа, если оно отрицательное.

Пример:
Введите кол-во чисел: 3
Введите число: 1.3
x = 2   log(x) = 0.6931471805599453
Введите число: -2.1
x = -3   exp(x) = 0.049787068367863944
Введите число: -5.9
x = -6   exp(x) = 0.0024787521766663585
'''

# count = 0
# numbers = int(input('Введите кол-во чисел: '))
# while count != numbers:
#     numb = float(input('Введите число: '))
#     if numb >= 0:
#         numb = math.ceil(numb)
#         x = math.log(numb)
#         print('x=', numb, 'log(x)=', x )
#     elif numb < 0:
#         numb = math.floor(numb)
#         x = math.exp(numb)
#         print('x=', numb, 'exp(x)=', x )
#     count +=1


'''Что оценивается
Задание считается успешно выполненным, если:

результат вывода соответствует условию, применяются корректные функции, округление осуществляется 
в нужную сторону, согласно условию;
формат вывода соответствует примеру;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 3. Убийца Steam

Что нужно сделать
Вы пишете программу-инсталлятор для компьютерной игры. Пока инсталлятор скачивает обновление, 
пользователю нужно показать сколько процентов уже скачалось, чтобы он мог решить пойти заварить чаю, 
или подождать у экрана компьютера. Обновления игры всегда занимают разное количество мегабайт, да и 
скорость интернет-соединения у игроков разная.

Напишите программу, принимающую на вход размер файла обновления в мегабайтах и скорость интернет 
соединения в мегабайтах в секунду. Для каждой секунды программа рассчитывает и выводит на экран сколько 
процентов от всего объема уже скачано, до тех пор пока не будет скачан весь объем. В конце программа должна 
показать сколько всего секунд заняло скачивание обновления. Обеспечьте контроль ввода.



Пример:

Укажите размер файла для скачивания: 123

Какова скорость вашего соединения? 27

Прошло 1 сек. Скачано 27 из 123 Мб (22%)

Прошло 2 сек. Скачано 54 из 123 Мб (44%)

Прошло 3 сек. Скачано 81 из 123 Мб (66%)

Прошло 4 сек. Скачано 108 из 123 Мб (88%)

Прошло 5 сек. Скачано 123 из 123 Мб (100%)



Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 4. Первая цифра

Что нужно сделать
Дано положительное действительное число X. Выведите его первую цифру после десятичной точки. 
При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками.



Что оценивается
результат вывода соответствует условию;
В вычислениях не используется for, if и работа со строками;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 5. Вот это объёмы!

Что нужно сделать
Для курсовой работы по физике Андрею нужно сравнить объёмы двух планет: Земли и какой-нибудь случайной, 
которая может в теории существовать в нашей вселенной. Андрей хорошо разбирается в формулах, 
а вот считать что-то, а уж тем более самому - это явно не его. 
Объём Земли ему известен заранее  - это 10.8321 * 10 11 км3

А вот объём случайной планеты ему нужно будет посчитать. Благо, у него есть формула:


где V - это объём, π - число пи, а R - радиус планеты.

Напишите программу, которая получает на вход радиус случайной планеты и выводит на экран во 
сколько раз планета Земля меньше или больше по объёму. Ответ округлите до трёх знаков после запятой



Пример:

Введите радиус случайной планеты: 3389.5

Объём планеты Земля больше в 6.641 раз



Пример 2:

Введите радиус случайной планеты: 7000

Объём планеты Земля меньше в (1/0.754) = 1.326 раз



Что оценивается
результат вывода соответствует условию;
формат вывода соответствует примеру;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 6. Метеостанция

Что нужно сделать
Сотрудники международной метеостанции должны каждый день передавать показания градусов по шкалам и 
Цельсия, и Фаренгейта. Напишите программу, которая принимает на вход три целых числа в градусах Цельсия: 
нижняя граница температуры, верхняя граница температуры и шаг. Программа выводит на экран таблицу 
соответствия градусов Цельсия градусам Фаренгейта от нижней до верхней границы с указанным шагом. 
Обеспечьте контроль ввода. Верхняя граница должна печататься, даже если последний шаг “перепрыгнул “ ее. 
Известно, что 0С соответствует 32F, а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта. 



Пример:

Ввод:

Нижняя граница: 0

Верхняя граница: 50

Шаг: 20

Вывод:

C   F

0   32

20  68

40  104

50  122



Что оценивается
результат вывода соответствует условию;
формат вывода соответствует примеру;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 7. Ход конём

Что нужно сделать
В рамках разработки шахматного ИИ стоит новая задача. По заданным вещественным координатам коня и 
второй точки программа должна определить может ли конь ходить в эту точку. Используйте как можно меньше 
конструкций if и логических операторов. Обеспечьте контроль ввода.



Пример:

Введите местоположение коня:

0.071

0.118

Введите местоположение точки на доске:

0.213

0.068

Конь в клетке (0, 1). Точка в клетке (2, 0).

Да, конь может ходить в эту точку.



Что оценивается
результат вывода соответствует условию;
формат вывода соответствует примеру;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 8. Часы

Что нужно сделать
С начала суток часовая стрелка повернулась на угол в α градусов. Определите на какой угол повернулась 
минутная стрелка с начала последнего часа. Входные и выходные данные — действительные числа.

При решении этой задачи нельзя пользоваться условными операторами и циклами.



Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 9. Уравнение

Что нужно сделать
Даны действительные коэффициенты a, b, c при этом a≠0. 
Решите квадратное уравнение a∙x2+b∙x+c=0 и выведите все его корни.

Если уравнение имеет два корня, выведите два корня в порядке возрастания, 
если один корень — выведите одно число, если нет корней — не выводите ничего



Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Задача 10. За что?

Что нужно сделать
Вы встретились со своим старым другом, который тоже изучает программирование, правда, в 
другом учебном заведении. За чашкой кофе он пожаловался вам, что сумасбродный препод дал им 
задание написать программу, которая из двух введённых чисел определяет наибольшее, не используя 
при этом условных операторов, циклов и встроенную функцию max. Радуясь, что на вашем курсе такого не требуют, 
вы всё-таки решаете помочь своему другу. Напишите для него эту программу.



Пример:

Введите первое число: 10

Введите второе число: 5

Наибольшее число: 10



Что оценивается
результат вывода соответствует условию;
input содержит корректное приглашение для ввода; 
вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);


Советы и рекомендации:
Рассмотрите разность суммы и разности чисел, сумму разности и суммы чисел.'''
