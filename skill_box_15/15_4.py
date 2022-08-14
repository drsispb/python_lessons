'''Задача 4. Видеокарты
Что нужно сделать
В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо
полных названий хранятся только числа, которые обозначают модель и поколение видеокарты. Недавно
компания выпустила новую линейку видеокарт. Самые старшие поколения разобрали за пару дней.
Напишите программу, которая удаляет из списка видеокарт наибольшие элементы.

Пример:
Количество видеокарт: 5
1 Видеокарта: 3070
2 Видеокарта: 2060
3 Видеокарта: 3090
4 Видеокарта: 3070
5 Видеокарта: 3090

Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
Новый список видеокарт: [ 3070 2060 3070 ]'''


N = int(input('Количество видеокарт: '))
old_list = []
count = 0

while count != N:
    count += 1
    print('\n ', count, end='')
    card = input(' Видеокарта: ')
    old_list.append(card)
check = 0
for i in old_list:
    if int(check) < int(i):
        check = i
new_list = []
for _ in old_list:
    if _ != check:
        new_list.append(_)
print('\nСтарый список видеокарт:', " ".join(map(str,old_list)))
print('Новый список видеокарт:', " ".join(map(str,new_list)))
