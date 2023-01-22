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

with open('23.Исключения_работа_с_ошибками/registrations.txt', 'r', encoding='utf8') as file,\
        open('23.Исключения_работа_с_ошибками/registrations_bad.log', 'w', encoding='utf8') as log_bad,\
        open('23.Исключения_работа_с_ошибками/registrations_good.log', 'w', encoding='utf8') as log_good:

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

#
# for i in list_reg:
#     print(i)
#     validation_func(i)
#
#
# with open('registrations_good.log', 'w', encoding='utf8') as log_good:
#     for i in list_reg:
#         log_good.write(str(i))
#         log_good.write('\n')