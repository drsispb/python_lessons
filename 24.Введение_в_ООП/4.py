'''Задача 4. Магия
Что нужно сделать
Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

Таблица преобразований:

Вода + Воздух = Шторм;
Вода + Огонь = Пар;
Вода + Земля = Грязь;
Воздух + Огонь = Молния;
Воздух + Земля = Пыль;
Огонь + Земля = Лава.
Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
Если результат не определён, то возвращается None.
Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:
class ExampleOne:
    def __add__(self, other):
        return ExampleTwo()
class ExampleTwo:
    answer = 'сложили два класса и вывели'
first_example = ExampleOne()
second_example = ExampleTwo()
result = first_example + second_example
print(result.answer)
Дополнительно: придумайте свой элемент (или элементы) и реализуйте его взаимодействие с остальными.'''

class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()

class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()

class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()

class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()

class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'

class Dirt:
    def __str__(self):
        return 'Грязь'
class Lightning:
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'

class Lava:
    def __str__(self):
        return 'Лава'

one_element = Water()
two_element = Air()
result = one_element + two_element

print('Смешиваем {} c {} и получаем {}'.format(one_element,two_element,result))