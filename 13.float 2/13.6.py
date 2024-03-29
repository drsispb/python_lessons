'''Задача 6. Маятник
Что нужно сделать

Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды прошлого колебания.
Если качнуть маятник, то, строго говоря, он не остановится никогда, просто амплитуда будет постоянно уменьшаться
до тех пор, пока мы не сочтём такой маятник остановившимся. Напишите программу, определяющую, сколько раз качнётся
маятник, прежде чем он, по нашему мнению, остановится.

Программа получает на вход начальную амплитуду колебания в сантиметрах и конечную амплитуду его колебаний, которая
считается остановкой маятника. Обеспечьте контроль ввода.

Пример:
Введите начальную амплитуду: 1
Введите амплитуду остановки: 0.1
Маятник считается остановившимся через 27 колебаний'''

def amplitude(start, stop):
    count = 0
    x = float(start)
    y = float(stop)
    while x > y:
        count += 1
        x -= x * 0.084
    print('Маятник считается остановившимся через', count, 'колебаний')



while True:
    start = input('Введите начальную амплитуду: ')
    stop = input('Введите амплитуду остановки: ')
    x = start.replace('.','',1).isdigit()
    y = stop.replace('.','',1).isdigit()
    if x == True and y == True:
        amplitude(start, stop)
    else:
        print('Ввведены неверные значения, повторите ввод')