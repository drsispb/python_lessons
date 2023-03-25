'''Задача 1. Драка
Что нужно сделать
Вы работаете в команде разработчиков мобильной игры, и вам досталась такая часть от ТЗ заказчика:
Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков.
Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют,
оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, какой
юнит атаковал и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс
здоровья, программа завершается сообщением о том, кто одержал победу.

Реализуйте такую программу.

'''
import random

class Warrior:
    def __init__(self, name, health=100, kick=20):
        self.name = name
        self.health = health
        self.kick = kick

    def info_health(self):
        print('Здоровье {} {}'.format(self.name, self.health))

    def info_attack(self):
        print('{} нанес удар '.format(self.name))


warrior_1 = Warrior('Старк')
warrior_2 = Warrior('Танос')

for _ in range(100):
    if warrior_1.health > 0 and warrior_2.health > 0:
        x = random.randint(1,2)
        if x == 1:
            warrior_1.info_attack()
            warrior_2.health = warrior_2.health - warrior_1.kick
            warrior_2.info_health()
        else:
            warrior_2.info_attack()
            warrior_1.health = warrior_1.health - warrior_2.kick
            warrior_1.info_health()
    elif warrior_1.health <= 0:
        print('Победил ', warrior_2.name)
        break
    elif warrior_2.health <= 0:
        print('Победил', warrior_1.name)
        break