'''Задача 5. Совместное проживание
Что нужно сделать
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве, Артём решил провести необычное
исследование. Для этого он реализовал модель человека и модель дома.

Человек может (должны быть такие методы):

есть (+ сытость, − еда);
работать (− сытость, + деньги);
играть (− сытость);
ходить в магазин за едой (+ еда, − деньги);
прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):

имя,
степень сытости (изначально 50),
дом.
В доме есть:

холодильник с едой (изначально 50 еды),
тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.

Логика действий человека определяется следующим образом:

Генерируется число кубика от 1 до 6.
Если сытость < 20, то нужно поесть.
Иначе, если еды в доме < 10, то сходить в магазин.
Иначе, если денег в доме < 50, то работать.
Иначе, если кубик равен 1, то работать.
Иначе, если кубик равен 2, то поесть.
Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз. '''
import random


class Human:
    house = True

    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):
        self.satiety += 10
        House.fridge_with_food -= 10


    def work(self):
        self.satiety -= 10
        House.nightstand_with_money += 10

    def game(self):
        self.satiety -= 10


    def go_in_shop(self):
        House.fridge_with_food += 10
        House.nightstand_with_money -= 10

    def info(self):
        print('Сытость {} в данный момент {}'.format(self.name, self.satiety))

class House:
    fridge_with_food = 50
    nightstand_with_money = 0

sergey = Human('Сергей')
ivan = Human('Иван')
house = House()

for _ in range(365):
    if sergey.satiety > 0 or ivan.satiety > 0:
        cube = random.randint(1,6)
        choice = random.randint(1,2)
        if sergey.satiety < 20 or ivan.satiety < 20:
            if sergey.satiety < 20:
                sergey.eat()
                sergey.info()
            else:
                ivan.eat()
                ivan.info()
        elif house.fridge_with_food < 10:
            if choice == 1:
                sergey.go_in_shop()
            else:
                ivan.go_in_shop()
        elif house.nightstand_with_money < 50:
            if choice == 1:
                sergey.work()
                sergey.info()
            else:
                ivan.work()
                ivan.info()
        elif cube == 1:
            if choice == 1:
                sergey.work()
                sergey.info()
            else:
                ivan.work()
                ivan.info()
        elif cube == 2:
            if cube == 1:
                sergey.work()
                sergey.info()
            else:
                ivan.work()
                ivan.info()
        else:
            if cube == 1:
                sergey.game()
            else:
                ivan.game()
    elif sergey.satiety > 0:
        print('К сожалению {} умер'.format(sergey.name))
    elif ivan.satiety > 0:
        print('К сожалению {} умер'.format(ivan.name))
print('Оба жильца выжили')