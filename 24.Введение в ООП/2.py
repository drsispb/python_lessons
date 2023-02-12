'''Задача 2. Студенты
Что нужно сделать
Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
Затем создайте список из десяти студентов (данные о студентах можете придумать свои или запросить их у пользователя)
и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.
'''
import random

class Students:

    def __int__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress
        self.average = sum(progress)/len(progress)

    def add_student(self, count):
        for _ in range(1, count + 1):
            self.name = choise_name[_]

quantity = int(input('Введите количество студентов: '))
name_list = []
cnt = 0
with open('name_for_24.txt', 'r', encoding='utf-8') as choise_name:
    for i_name in choise_name:
        cnt += 1
        if cnt <= quantity:
            name_list.append(i_name.strip('\n'))
    print(name_list)




student = Students()
student.add_student(quantity)