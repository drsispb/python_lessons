# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(300, 300)
radius = 50
for _ in range (3):
    radius += 5
    sd.circle(center_position=point, radius=radius)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bubble (point, step):
    radius2 = 50
    for _ in range(3):
        radius2 += step
        sd.circle(center_position=point, radius=radius2)
point = sd.get_point(350, 350)
bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range (100, 1100, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for x in range (100, 1100, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)
    for x in range(100, 1100, 100):
        point = sd.get_point(x, 200)
        bubble(point=point, step=5)
        for x in range(100, 1100, 100):
            point = sd.get_point(x, 300)
            bubble(point=point, step=5)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range (100):
    point = sd.random_point()
    bubble(point=point, step=5)

sd.pause()


