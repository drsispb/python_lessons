
clock = int(input('Введите время  от 0 до 23 часов: '))
if clock <= 7 or 10 <= clock < 12 or 14 <= clock < 15 or 18 <= clock < 20 or clock >= 22:
  print('посылку не получить')
else:
  print('посылку можно получить')