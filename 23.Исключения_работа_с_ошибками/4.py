'''Задача 4. Регистрация
Что нужно сделать

У вас есть файл с протоколом регистраций пользователей на сайте — registrations.txt.
Каждая строка содержит: ИМЯ ИМЕЙЛ ВОЗРАСТ, разделённые пробелами. Например: Василий test@test.ru 27

Напишите программу, которая проверяет данные из файла для каждой строки:

Присутствуют все три поля.
Поле имени содержит только буквы.
Поле «Имейл» содержит @ и . (точку).
Поле «Возраст» является числом от 10 до 99.
В результате проверки сформируйте два файла:

registrations_good.log_index — для правильных данных, записывать строки как есть,
registrations_bad.log_index — для ошибочных, записывать строку и вид ошибки.
Для валидации строки данных напишите функцию, которая может выдавать исключения:

НЕ присутствуют все три поля: IndexError.
Поле имени содержит НЕ только буквы: NameError.
Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.
Поле «Возраст» НЕ является числом от 10 до 99: ValueError.


Формат выходных данных

Содержимое файла registrations_bad.log_index:
Ольга kmrn@gmail.com 123        Поле «Возраст» НЕ является числом от 10 до 99
Чехова kb@gmail.com 142        Поле «Возраст» НЕ является числом от 10 до 99
……
Степан ky 59        Поле «Имейл» НЕ содержит @ и . (точку)
……
Содержимое файла registrations_good.log_index:
Геннадий ttdababmt@gmail.com 69
Ольга ysbxur@gmail.com 20
……

'''

def check_index(check):
    x = 'Поле «Возраст» НЕ является числом от 10 до 99'
    try:
        if len(check.split()) != 3:
            raise IndexError
    except IndexError:
        return check, '........', x

def check_name(check):
    y = 'Поле имени содержит НЕ только буквы: NameError.'
    try:
        if not check.split()[0].isalpha():
            raise NameError
    except NameError:
        return check, '........', y

def check_syntax(check):
    z = 'Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.'
    try:
        if '@' not in check.split()[1] and '.' not in check.split()[1]:
            raise SyntaxError
    except SyntaxError:
        return check, '........', z

def check_value(check):
    c = 'Поле «Возраст» НЕ является числом от 10 до 99: ValueError.'
    try:
        if int(check.split()[2]) not in range(10,99):
            raise ValueError
    except ValueError:
        return check, '........', c

log_bad = open('registrations_bad.log', 'w', encoding='utf8')
list_reg = []

with open('registrations.txt', 'r', encoding='utf8') as file:
    for i_user in file.readlines():
        list_reg.append(i_user.rstrip('\n'))

    for check in list_reg:
        log_index = check_index(check)
        if log_index != None:
            log_bad.write(' '.join(log_index))
            list_reg.remove(check)
    log_bad.write('\n....................................\n')

    for check in list_reg:
        log_name = check_name(check)
        if log_name != None:
            log_bad.write(' '.join(log_name))
            list_reg.remove(check)
    log_bad.write('\n....................................\n')

    for check in list_reg:
        log_syntax = check_syntax(check)
        if log_syntax != None:
            log_bad.write(' '.join(log_syntax))
            list_reg.remove(check)
    log_bad.write('\n....................................\n')

    for check in list_reg:
        log_value = check_value(check)
        if log_value != None:
            log_bad.write(' '.join(log_value))
            list_reg.remove(check)
    log_bad.write('\n....................................\n')

with open('registrations_good.log', 'w', encoding='utf8') as log_good:
    for i in list_reg:
        log_good.write(str(i))
        log_good.write('\n')
