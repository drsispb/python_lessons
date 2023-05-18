''' Задача 4. Счётчик
Что нужно сделать
Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.

Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).
'''
from typing import Callable


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    func.__cnt__ = 0

    def wrapper(*args, **kwargs):
        func.__cnt__ += 1
        res = func(*args, **kwargs)
        print('{} была вызвана: {}x'.format(func.__name__, func.__cnt__))
        return res

    return wrapper

@counter
def test(i: int) -> int:
    return i**2
@counter
def test2(i: int) -> int:
    return i**3

for i in range(5):
    test(i)
    for j in range(5):
        test2(j)





