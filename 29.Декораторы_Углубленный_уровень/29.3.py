'''Задача 3. Логирование в формате
Что нужно сделать
Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов) и
 в который можно передавать формат вывода даты и времени логирования.

Пример кода, передаётся формат «месяц день год — часы:минуты:секунды»:
@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

Результат:
Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
Тут метод test_sum_1.
Завершение 'A.test_sum_1', время работы = 0,187 s.
Тут метод test_sum_1 у наследника.
Завершение 'B.test_sum_1', время работы = 0,187 s.
Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37.
Тут метод test_sum_2 у наследника.
Завершение 'B.test_sum_2', время работы = 0,370 s.

Совет: внимательно пересмотрите видео 29.4, если сталкиваетесь с трудностями в этой задаче.
'''
from typing import Callable, Any, Optional
import functools
import time
from datetime import datetime


def timer(cls, func, date_format):
    @functools.wraps(timer)
    def wrapped(*args, **kwargs):
        format = date_format
        for sym in format:
            if sym.isalpha():
                format = format.replace(sym, '%' + sym)
                print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now ().strftime(format)}")
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
                return result
    return wrapped

def log_methods(date_format: str) -> Callable:
    def decorator_log_methods(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
    return decorator_log_methods


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
