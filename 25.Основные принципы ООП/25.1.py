'''Задача 1. Налоги
Что нужно сделать
Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса Property
и производных от него классов Apartment, Car и CountryHouse.

Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога,
 переопределённый в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.

Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.

Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества,
а затем выдаёт налог на соответствующее имущество и показывает, сколько денег ему не хватает (если это так).
'''

class Property:
    rate = 0
    ''' Базовый класс, для приема в себя стиомости '''
    def __init__(self, worth):
        self.worth = worth

    def __str__(self):
        return '{} стоят {}:  \nРазмер налога {}: \n'

    def tax_calculation(self):
        '''Метод для расчета налога'''
        return self.worth * (1 / self.rate)


class Apartment(Property):
    '''Дочерний класс для апартаментов, принимает стоимость и налоговую базу'''

    def __init__(self, worth, rate):
        super().__init__(worth)
        self.rate = rate

    def __str__(self):
        return super().__str__().format('Апартаменты', self.worth, self.tax_calculation())

class Car(Property):
    '''Дочерний класс для автомобиля, принимает стоимость и налоговую базу'''
    def __init__(self, worth, rate):
        super().__init__(worth)
        self.rate = rate

    def __str__(self):
        return super().__str__().format('Машина', self.worth, self.tax_calculation())


class CountryHouse(Property):
    '''Дочерний класс для загородного дома, принимает стоимость и налоговую базу'''
    def __init__(self, worth, rate):
        super().__init__(worth)
        self.rate = rate

    def __str__(self):
        return super().__str__().format('Загородный дом', self.worth, self.tax_calculation())


apt = Apartment(worth=int(input('Введите стоимость квартиры: ')), rate=1000)
car = Car(worth=int(input('Введите стоимость автомобиля: ')), rate=200)
cHouse = CountryHouse(worth=int(input('Введите стоимость загородного дома: ')), rate=500)
print(apt)
print(car)
print(cHouse)
all_tax = apt.tax_calculation() + car.tax_calculation() + cHouse.tax_calculation()
money = int(input('Введите сколько у вас имеется денег '))
if all_tax > money:
    print('Очень жаль, вам не хватет денег на оплату налогов ;(   в размере', all_tax - money)
else:
    print('Поздравляю, ваших денег хватит на оплату налогов')