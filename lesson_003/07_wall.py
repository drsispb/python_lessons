# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw
simple_draw.resolution = (600,600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for y in range(0, 600, 100):
    x = 0
    for x in range(0, 600, 100):
        start_point = simple_draw.get_point(x,y)
        end_point = simple_draw.get_point(x + 100,y + 50)
        simple_draw.rectangle(start_point, end_point, width=2)
for y in range(-50, 600, 100):
    x = 0
    for x in range(-50, 600, 100):
        start_point = simple_draw.get_point(x,y)
        end_point = simple_draw.get_point(x + 100,y + 50)
        simple_draw.rectangle(start_point, end_point, width=2)

simple_draw.pause()
