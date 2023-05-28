'''Задача 2. Математический модуль
Что нужно сделать
Вася использует в своей программе очень много различных математических вычислений, связанных с
 фигурами. Например, нахождение их площадей или периметров. Поэтому, чтобы не захламлять код огромным
 количеством функций, он решил выделить для них отдельный класс, подключить как модуль и использовать
 по аналогии с модулем math.

Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):

вычисление длины окружности,
вычисление площади окружности,
вычисление объёма куба,
вычисление площади поверхности сферы.
Пример основного кода:

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

Результат:
31.41592653589793
113.09733552923255
'''

from typing import Union
import math

all_numbers = Union[int, float]

class MyMath:

    @classmethod
    def circle_len(cls, radius: all_numbers) -> all_numbers:
        x = 2 * math.pi * radius
        return x

    @classmethod
    def circle_sq(cls, radius: all_numbers) -> all_numbers:
        x = math.pi * radius ** 2
        return x

    @classmethod
    def cube_volume(cls, radius: all_numbers) -> all_numbers:
        x = radius ** 3
        return x

    @classmethod
    def sphere_sq(cls, radius: all_numbers) -> all_numbers:
        x = 4 * math.pi * radius ** 2
        return x


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
