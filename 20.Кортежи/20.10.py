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

def analog_zip(object_1, object_2):
  if not isinstance(object_1, dict) and not isinstance(object_2, dict):
    if len(object_1) > len(object_2):
      return ((object_1[i_element], object_2[i_element]) for i_element in range(len(object_2)))
    else:
      return ((object_1[i_element], object_2[i_element]) for i_element in range(len(object_1)))
  elif not isinstance(object_1, dict) and isinstance(object_2, dict):
    if len(object_1) > len(object_2):
      return ((object_1[i_element], list(object_2.keys())[i_element]) for i_element in range(len(object_2)))
    else:
      return ((object_1[i_element], list(object_2.keys())[i_element]) for i_element in range(len(object_1)))
  elif isinstance(object_1, dict) and not isinstance(object_2, dict):
    if len(object_1) > len(object_2):
      return (((list(object_1.keys())[i_element]), object_2[i_element]) for i_element in range(len(object_2)))
    else:
      return (((list(object_1.keys())[i_element]), object_2[i_element]) for i_element in range(len(object_1)))
  elif isinstance(object_1, dict) and isinstance(object_2, dict):
    if len(object_1) > len(object_2):
      return (((list(object_1.keys())[i_element]), list(object_2.keys())[i_element]) for i_element in range(len(object_2)))
    else:
      return (((list(object_1.keys())[i_element]), list(object_2.keys())[i_element]) for i_element in range(len(object_1)))

string = {10: 20, 30: 40, 50: 60, 70:80}
tpl = (10, 20, 30, 40)
zip_view = analog_zip(string, tpl)
print(zip_view)

for a, b in zip_view:
    print((a, b))