'''Задача 2. Карма
Что нужно сделать
Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы
(это константа), чтобы достичь просветления.

Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и
может с вероятностью 1 к 10 выкинуть одно из исключений:

KillError,
DrunkError,
CarCrashError,
GluttonyError,
DepressionError.
(Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
кармы до уровня константы. Исключения обработайте и запишите в отдельный лог karma.log.
По итогу у вас может быть примерно такая структура программы:
открываем файл
цикл по набору кармы
   try
      карма += one_day()
   except(ы) с указанием классов исключений, которые нужно поймать
      добавляем запись в файл
закрываем файл'''

import random
class Exception():
    '''Родительский класс, по факту заведен для красоты'''
    pass

'''Прочие классы, для инициализации информации об исключении'''
class KillError(Exception):
    def __str__(self):
        return 'KillError'
class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'
class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'
class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'
class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'



def one_day():
    '''функция для получения кармы, либо инициализации исключения'''
    if random.randint(1,10) == 2:
        raise
    else:
        return random.randint(1,7)

with open('karma.log', 'w', encoding='utf8') as file:

    constanta = 500
    carma = 0
    cnt = 0

    while carma <= constanta:
        cnt += 1
        try:
            carma += one_day()
        except:
            error = random.choice([KillError(), CarCrashError(), DrunkError(), GluttonyError(), DepressionError()])
            file.write(str(error) + '\n')
    print('Уровень кармы достигнут, потребовалось ', cnt, 'дня(-ей)')