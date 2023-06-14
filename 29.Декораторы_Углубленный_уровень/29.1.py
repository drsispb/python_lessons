'''Задача 1. Права доступа
Что нужно сделать
Перед вами стоит задача создать и поддерживать специализированный форум.
Вы только приступили и сейчас работаете над действиями, которые могут совершать посетители
форума. Для разных пользователей прописаны разные возможности.

Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ к
вызываемой функции, и если нет, то выдаёт исключение PermissionError.

Пример кода:
user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()

Результат:
Удаляем сайт
PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment
'''

from typing import Callable
import functools


def check_permission(user: str) -> Callable:
    user_permissions = ['admin']

    def check_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            try:
                if user in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print('PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment')

        return wrapped

    return check_decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()