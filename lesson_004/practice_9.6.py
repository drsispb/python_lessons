word = input('Введите тескт: ')
count = 0
count_u = 0
for x in word:
    if x == 'ы':
        count += 1
    elif x == 'Ы':
        count_u += 1
print('Больших букв Ы:', count_u)
print('Маленьких букв Ы:', count)