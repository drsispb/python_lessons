'''Задача 4. Вечеринка
Что нужно сделать

В честь своего дня рождения Артём решил закатить вечеринку у себя на даче. Он не стал рассылать приглашения,
а просто сообщил всем: «Если хотите — приходите и своих друзей тоже зовите». В ходе вечеринки люди приходили и
уходили, ночевать остались не все. К тому же и сама дача не резиновая — на ней помещается всего шесть человек.

Дан изначальный список гостей — имена тех, кто пришёл к началу:

guests = [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
Напишите программу, которая спрашивает у пользователя, ушёл человек или пришёл новый гость, и, исходя из ответа,
добавляет в список или удаляет из него нужное имя. При этом гостей может быть не больше шести. Имена запрашиваются
до тех пор, пока пользователь не введёт сообщение «Пора спать».

Пример:

Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]

Гость пришёл или ушёл? пришёл

Имя гостя: Алекс

Привет, Алекс!


Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]

Гость пришёл или ушёл? пришёл

Имя гостя: Гоша

Прости, Гоша, но мест нет.



Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]

Гость пришёл или ушёл? ушёл

Имя гостя: Ваня

Пока, Ваня!



Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]

Гость пришёл или ушёл? Пора спать

Вечеринка закончилась, все легли спать.'''

status = 0
name = 0
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while status != 'Пора спать':
    print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
    status = input('Гость пришёл или ушёл? ')
    if status == 'Пора спать':
        break
    name = str(input('Имя гостя: '))
    if status == 'пришел' and len(guests) < 6:
        guests.append(name)
        print('Привет, ', name, '!')
    elif status == 'ушел':
        guests.remove(name)
        print('Пока,', name, '!')
    elif status == 'пришел' and len(guests) >= 6:
        print('Прости,', name, ', но мест нет.')
print('Вечеринка закончилась, все легли спать.')