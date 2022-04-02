# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (600,600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

start_x = 50
end_x = 350

for i in range(7):
    start_x += 5
    end_x += 5
    sd.line(sd.Point(start_x, 50), sd.Point(end_x, 450), color=rainbow_colors[i], width=4)

sd.pause()


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

point_rw = sd.get_point(600,0)
radius_rw = 300

for _ in range (7):
    radius_rw += 5
    sd.circle (center_position=point_rw, radius=radius_rw, color=rainbow_colors [_], width=4)


sd.pause()
