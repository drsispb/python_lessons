'''Задача 1. Песни 2
Что нужно сделать

Мы продолжаем писать приложение для удобного прослушивания музыки, но теперь наши песни хранятся в виде словаря,
а не вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.



violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


Напишите программу, которая запрашивает у пользователя количество песен из списка и названия этих песен,
а на экран выводит общее время их звучания.

Пример:
Сколько песен выбрать? 3
Название первой песни: Halo
Название второй песни: Enjoy the Silence
Название третьей песни: Clean

Общее время звучания песен: 14,93 минуты'''

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
total_long = 0
check_song = int(input('Сколько песен выбрать? '))
for i in range(1, check_song + 1):
    song = input('Название {} песни:'.format(i))
    if song in violator_songs:
        total_long +=violator_songs[song]
    else:
        print('такой песни нет', song)
print('Общее время звучания песен: ', round(total_long, 2), 'минуты')




