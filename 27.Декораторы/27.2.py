'''Задача 2. Замедление кода
Что нужно сделать
В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.

Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.'''

import time
import functools
from typing import Callable, Any
def timer(func: Callable) -> Callable:

    def wrapped_func(*args, **kwargs) -> Any:
        print('Пошла задержка')
        time.sleep(2)
        result = func
        return result
    return wrapped_func

@timer
def test():
    print(2**100)

test()



