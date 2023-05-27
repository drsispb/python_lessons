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
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year

    @classmethod
    def from_string(cls, date: str) -> str:
        date_list = date.split('-')
        return 'День: {day} Месяц: {month} Год: {year}'.format(
            day=date_list[0],
            month=date_list[1],
            year=date_list[2])

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))