''' Задача 2. Турнир
Что нужно сделать
Для соревнований по волейболу необходимо сформировать турнирнирную сетку из восьми человек на два дня.
На первый день из списка участников решили выбрать каждого второго.
Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар. Напишите программу,
которая выводит элементы списка только с чётными индексами.
Пример:
Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']'''

name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list_first_day = []
new_list_second_day = []
count = 0
for i in name_list:
    if count % 2 == 0:
        new_list_first_day.append(i)
    else:
        new_list_second_day.append(i)
    count += 1

print('Первый день:', new_list_first_day)
print('Второй день:', new_list_second_day)