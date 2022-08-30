'''Задача 5. Песни
Что нужно сделать

Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode.
Каждая песня состоит из названия и продолжительности с точностью до долей минут:

violator_songs = [
    ['World in My Eyes', 4,86],
    ['Sweetest Perfection', 4,43],
    ['Personal Jesus', 4,56],
    ['Halo', 4,9],
    ['Waiting for the Night', 6,07],
    ['Enjoy the Silence', 4,20],
    ['Policy of Truth', 4,76],
    ['Blue Dress', 4,29],
    ['Clean', 5,83]
]


Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками. И при
этом ему важно, сколько времени в сумме эти N песен будут звучать.
Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен,
а на экран выводит общее время их звучания.

Пример:
Сколько песен выбрать? 3
Название 1-й песни: Halo
Название 2-й песни: Enjoy the Silence
Название 3-й песни: Clean
Общее время звучания песен: 14,93 минуты'''


def get_song(i,violator_songs):
    time_min = 0
    time_sec = 0
    print('Название', i, '-й песни')
    sing = input()
    for s in violator_songs:
        if s[0] == sing:
            time_min += s[1]
            time_sec += s[2]
            total_time = time_min + time_sec / 100
    return total_time

violator_songs = [
    ['World in My Eyes', 4,86],
    ['Sweetest Perfection', 4,43],
    ['Personal Jesus', 4,56],
    ['Halo', 4,90],
    ['Waiting for the Night', 6,7],
    ['Enjoy the Silence', 4,20],
    ['Policy of Truth', 4,76],
    ['Blue Dress', 4,29],
    ['Clean', 5,83]
]
count_sing = int(input('Сколько песен выбрать? '))

for i in range(1, count_sing + 1):
    total_time = get_song(i,violator_songs)
    total_time += total_time

print('Общее время звучания песен:', total_time, 'минуты')