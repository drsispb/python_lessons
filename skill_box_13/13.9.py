'''Задача 9. Аннуитетный платёж
Что нужно сделать

Кредит в сумме S млн руб., выданный на n лет под i% годовых, подлежит погашению равными ежегодными выплатами в
конце каждого года, включающими процентные платежи и сумму в погашение основного долга. Проценты начисляются в
один раз в год. После выплаты третьего платежа достигнута договорённость между кредитором и заёмщиком о продлении
срока погашения займа на n_2 лет и увеличении процентной ставки с момента конверсии до i_2%. Напишите программу,
которая выводит план погашения оставшейся части долга.

Используйте следующие формулы (А — размер аннуитетного платежа, его дробную часть округлите до двух знаков,
то есть до копеек):


i - процент в дробном виде (6% —> 0.06)
'''

def credit(s,y,p):
    count = 0
    p = p / 100
    while count != 3:
        count += 1
        K = (p * (1 + p) ** y) / ((1 + p) ** y - 1)
        persent = s * p
        A = K * s
        total = A - persent
        total = round(total, 2)
        print('\nПериод: ', count, '\nОстаток долга на начало периода:', s, '\nВыплачено процентов:', persent, '\nВыплачено тела кредита:', total)
        s = s - total
        y -= 1
        if count == 3:
            print('\nОстаток долга: ', s)
    return s,y


def prolongation (s, yp, y, p):
    count = 0
    p = p / 100
    y = y + yp
    while count != 4:
        count += 1
        K = (p * (1 + p) ** y) / ((1 + p) ** y - 1)
        persent = s * p
        A = K * s
        total = A - persent
        print('\nПериод: ', count, '\nОстаток долга на начало периода:', s, '\nВыплачено процентов:', persent, '\nВыплачено тела кредита:', total)
        s = s - total
        y -= 1
        if count == 4:
            print('\nОстаток долга: ', s)

summ_credit = float(input('Введите сумму кредита: '))
years = float(input('На сколько лет выдан? '))
credit_percent = float(input('Сколько процентов годовых? '))

credit,year = credit(summ_credit, years, credit_percent)

years_prolongation = float(input('\nНа сколько лет продлевается договор? '))
percent_prolongation = float(input('Увеличение ставки до?: '))

prolongation (credit,year, years_prolongation, percent_prolongation)