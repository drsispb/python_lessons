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

def validation_func(string):
  lst_item = string.split()
  if len(lst_item) != 3:
    raise IndexError('НЕ присутствуют все три поля: IndexError')
  if not lst_item[0].isalpha:
    raise NameError('Поле имени содержит НЕ только буквы: NameError.')
  if '@' not in lst_item[1] or '.' not in lst_item[1]:
    raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.')
  if int(lst_item[2]) < 10 or int(lst_item[2]) > 99:
    raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99: ValueError.')
  return string


list_reg = []

with open('registrations.txt', 'r', encoding='utf8') as file,\
        open('registrations_bad.log', 'w', encoding='utf8') as log_bad,\
        open('registrations_good.log', 'w', encoding='utf8') as log_good:

        for i_user in file.readlines():
            try:
                validation_func(i_user)
                log_good.write(i_user)
            except IndexError:
                log_bad.write(i_user.rstrip('\n') + '.......НЕ присутствуют все три поля: IndexError.\n')
            except NameError:
                log_bad.write(i_user.rstrip('\n') + '.......Поле имени содержит НЕ только буквы: NameError.\n')
            except SyntaxError:
                log_bad.write(i_user.rstrip('\n') + '.......Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.\n')
            except ValueError:
                log_bad.write(i_user.rstrip('\n') + '.......Поле «Возраст» НЕ является числом от 10 до 99: ValueError.\n')
