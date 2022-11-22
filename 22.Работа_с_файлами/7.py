'''Задача 7. Турнир
Что нужно сделать

В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»: фамилии,
имена и количество баллов, набранных в первом туре. Во второй тур проходят участники, которые набрали более K
баллов в первом туре.
Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур, с нумерацией.
В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа должна вывести
фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией. Имя нужно сократить
до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.
Пример:
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Segeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78
Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92'''



new_file = open('first_tour.txt', 'r')
limit = int(new_file.readline())

list_result = [i.split() for i in new_file]
list_surname_result = [[i[0], i[1][0:1], i[2]] for i in list_result if int(i[2]) > limit]
number_of_winners = str(len(list_surname_result))

second_tour = open('second_tour.txt', 'w')
second_tour.write(number_of_winners + '\n')
cnt = 1
for i_elem in list_surname_result:
    second_tour.write(str(cnt) + ') ' + str(i_elem[1]) + '. ' + i_elem[0] + ' ' + i_elem[2] + '\n')
    cnt += 1

