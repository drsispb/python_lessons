'''Задача 1. Имена 2
Что нужно сделать
Есть файл people.txt, в котором построчно хранится N имён пользователей.
Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой
именно строке ошибка возника. Программа при этом не завершается и обрабатывает все имена файла.
Также при желании можно вывести все ошибки в отдельный файл errors.log_index.
Пример работы программы
Содержимое файла people.txt:
Василий
Николай
Надежда
Никита
Ян
Ольга
Евгения
Кристина
Ответ в консоли:
Ошибка: менее трёх символов в строке 5.
Общее количество символов: 49.
'''

try:
    log_w = open('errors.log', 'w', encoding='utf8')
except NameError:
    print('Файла для записи ошибок errors.log не существует')
try:
    with open('people.txt', 'r', encoding='utf8') as file_people:
        file_people = file_people.readlines()
        total_count = sum([len(i.strip()) for i in file_people])
        for x, i_name in enumerate(file_people, 1):
            try:
                if len(i_name.strip()) < 3:
                    raise ValueError(f'Ошибка: менее трёх символов в строке {x}\n')
            except ValueError as log:
                log_w.write(str(log))
                print(log)
except NameError:
    print('Файла people.txt для считывания участников не существует')
finally:
    print('Общее количество символов: ', total_count)
    log_w.close()