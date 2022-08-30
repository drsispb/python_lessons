'''Задача 3. Детали
Что нужно сделать

В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
['обод', 2000], ['шатун', 200], ['седло', 2700]]
Продавец решил, что считать количество и стоимость деталей вручную не очень удобно, поэтому решил попросить помощи
у программиста, чтобы оптимизировать этот процесс.
Напишите программу, которая запрашивает у пользователя деталь, считает их количество, а также общую стоимость.
Пример:
Название детали: седло
Кол-во деталей — 3
Общая стоимость — 4500
'''

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
['обод', 2000], ['шатун', 200], ['седло', 2700]]

detal = input('Введите необходимую деталь: ')
shop_count = len(shop)
count = 0
summ_detal = 0

for i in range(shop_count):
    if shop[i][0] == detal:
        count += 1
        summ_detal += shop [i][1]

print('Название детали:  ', detal)
print('Кол-во деталей — ', count)
print('Общая стоимость — ', summ_detal)