'''Задача 3. Дата
Что нужно сделать
Реализуйте класс Date, который должен:

проверять числа даты на корректность;
конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.

При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации, например:
date = Date.from_string('10-12-2077')
Неверный вариант: date = Date(10, 12, 2077)
Пример основного кода:

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

Результат:
День: 10    Месяц: 12    Год: 2077
True
False'''


class Date:

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split('-'))
        if year % 4 == 0 and month == 2 and 0 < day <=29:
            return True
        elif year > 0 and month in [4, 6, 9,11] and 0 < day <= 30:
            return True
        elif year > 0 and month in [1, 3, 5, 7, 8, 10, 12] and 0 < day <= 31:
            return True
        elif year % 4 != 0 and month == 2 and 0 < day <= 28:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date: str) -> str:
        if cls.is_date_valid(date):
            date_l = date.split('-')
            return 'День: {day} Месяц: {month} Год: {year}'.format(
            day=date_l[0],
            month=date_l[1],
            year=date_l[2])
        else:
            return 'Неверный формат даты'



date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))