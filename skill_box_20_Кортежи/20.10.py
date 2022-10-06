'''Задача 10. Своя функция zip
Что нужно сделать

В самом конце собеседования вас неожиданно спросили: «Расскажите, что делает функция zip?».
Чтобы произвести впечатление, вы решили не только рассказать про неё, но и написать её аналог.

Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число».
Затем выведите на экран сам генератор и кортежи.

Пример:
Строка: abcd
Кортеж чисел: (10, 20, 30, 40)

Результат:
<generator object <genexpr> at 0x00000204A4234048>
('a', 10)
('b', 20)
('c', 30)
('d', 40)

Дополнительно: создайте полный аналог функции zip — сделайте так,
чтобы программа работала с любыми итерируемыми типами данных.'''

def analog_zip(x,y):
    if isinstance(x, dict):
        return ((x.items(), y[i]) for i in range(len(x)))
    elif isinstance(y, dict):
        return ((x[i], y.items()) for i in range(len(x)))
    elif isinstance(y, dict) and isinstance(x, dict):
        return ((x.items(), y.items()) for i in range(len(x)))
    else:
        return ((x[i], y[i]) for i in range(len(x)))

string = {10: 20, 30: 40, 50: 60, 70:80}
tpl = (10, 20, 30, 40)
zip_view = analog_zip(string, tpl)
print(zip_view)

for a, b in zip_view:
    print((a, b))