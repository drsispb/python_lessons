# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sds

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
sds.resolution = (700, 700)


def smile(x, y, color):
    start_point = sds.get_point(x, y)
    sds.circle(start_point, 50, color, width=4)
    sds.line(sds.get_point(x - 20, y - 5), sds.get_point(x - 10, y - 20), color, 2)
    sds.line(sds.get_point(x - 10, y - 20), sds.get_point(x + 10, y - 20), color, 2)
    sds.line(sds.get_point(x + 10, y - 20), sds.get_point(x + 20, y - 5), color, 2)
    sds.ellipse(sds.get_point(x - 20, y + 20), sds.get_point (x - 15, y + 25), color, 2)
    sds.ellipse(sds.get_point(x + 20, y + 20), sds.get_point(x + 15, y + 25), color, 2)


for i in range(10):
    point = sds.random_point()
    x = point.x
    y = point.y
    color = sds.random_color()
    smile(x, y, color)
sds.pause()
#    smile(point=point, step=10, color=(255,255,0))
