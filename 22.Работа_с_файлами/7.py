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
k = int(new_file.readline())

new_list = []

for line in new_file:
    new_line = line.split()

    if new_line != [] and int(new_line[-1]) > k:
        new_list.append(new_line)
new_file.close()

new_list.sort(key=lambda a: int(a[-1]))
new_list.reverse()

count = str(len(new_list))

out_lst = []
n = 1
for i in new_list:
    name_sim = str(i[0][0]) + '.'
    s_win = str(n) + ') ' + name_sim + ' ' + i[1] + ' ' + i[-1]
    out_lst.append(s_win)
    n += 1

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(count + '\n')
    s = '\n'.join(out_lst)
    f_out.write(s)

for i in out_lst:
    print(f'{i}')