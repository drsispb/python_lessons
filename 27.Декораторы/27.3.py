'''Задача 3. Логирование
Что нужно сделать
Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции
и её документация. Если во время выполнения декорируемой функции возникла ошибка,
то в файл function_errors.log записываются название функции и ошибки.

Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.'''

import datetime
import functools
from typing import Callable, Any

def logging(func):

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print('Вызвана функция:', func.__name__)
            print('Документация:\n', func.__doc__)
            result = func(*args, **kwargs)
            return result
        except:
            with open('function_errors.log', 'w', encoding='utf8') as log:
                log.write(str(datetime.datetime.now()) + ' ' + 'BaseException' + func.__name__)
    return wrapped_func()


@logging
def test1():
    '''Тестовая функция, с приветствием'''
    print('Hello world!')

@logging
def test2():
    '''Тестовая фукнция для вызова ошибки'''
    raise BaseException



@logging
def test3():
    '''Тестовая фукнция для проверки, что код не остановился'''
    print('Код не остановился')

test1()
test2()
test3()
