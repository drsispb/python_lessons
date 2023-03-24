'''Задача 2. Студенты
Что нужно сделать
Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость»
(список из пяти элементов). Затем создайте список из десяти студентов (данные о студентах можете придумать
свои или запросить их у пользователя) и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.'''

import random
class Student:

    def __init__(self, name, group, order):
        self.name = name
        self.group = group
        self.avg = sum(order) / len(order)

    def info(self):
        print('ФИ {}\nНомер группы {}\nСредний балл {}\n'.format(
            self.name,
            self.group,
            self.avg,))


name_list = ['Сидоров Олег', 'Петров Андрей', 'Александров Петр', 'Усманова Алия',
             'Усова Дарья', 'Петров Петр', 'Александров Александр',
             'Короткова Олеся', 'Сергеев Сергей', 'Арбузов Ашот']

group_list = [random.randint(11,12) for i in range(10)]

order_list = []
for _ in range(10):
    order_list.append([random.randint(1, 5) for _ in range(5)])



students = []
for i in range(10):
    students.append(Student(name_list[i], group_list[i], order_list[i]))

students.sort(key=lambda x: x.avg)
for i in students:
    print('ФИ ',i.name, 'Группа ', i.group, 'Средний балл ', i.avg)
