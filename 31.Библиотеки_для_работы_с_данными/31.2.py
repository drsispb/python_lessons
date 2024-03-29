"""Задача 2. Регистрационные знаки
Что нужно сделать
В России для транспорта применяются регистрационные знаки нескольких видов.

Общее в них то, что они состоят из цифр и букв. Причём используются только 12 букв кириллицы, имеющих
графические аналоги в латинском алфавите: А, В, Е, К, М, Н, О, Р, С, Т, У и Х.

У частных легковых автомобилей номера — это буква, три цифры, две буквы, затем две или три цифры с кодом региона.

У такси — две буквы, три цифры, затем две или три цифры с кодом региона.

Напишите программу, которая в перечне номеров находит номера частных автомобилей и номера такси.

Пример перечня:
'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

Результат:
Список номеров частных автомобилей: ['А578ВЕ777', 'К901МН666']
Список номеров такси: ['ОР233787', 'СТ46599']"""

import re

numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

search_private = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', numbers)
print('Список номеров частных автомобилей: ', search_private)

search_taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', numbers)
print('Список номеров такси: ', search_taxi)
