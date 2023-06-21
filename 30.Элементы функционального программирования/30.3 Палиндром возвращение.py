'''Задача 3. Палиндром: возвращение
Что нужно сделать
Есть множество встроенных и внешних библиотек для работы с данными в Python. С некоторыми из них вы уже работали.
Например, с модулем collections, когда использовали специальный класс OrderedDict, с помощью которого делали
упорядоченный словарь. В этой библиотеке есть и другие возможности, но их немного.
Официальная документация: collections — Container datatypes.
Используя модуль collections, реализуйте функцию can_be_poly, которая принимает на вход строку и проверяет,
можно ли получить из неё палиндром.

Пример кода:
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

Результат:
True
False'''
from collections import Counter


def can_be_poly(elem: str) -> bool:
    return len(elem) % 2 == sum(x % 2 for x in Counter(elem).values())


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

def can_be_poly_lambda(elem: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(elem).values()))) <= 2

print(can_be_poly_lambda('abcba'))
print(can_be_poly_lambda('abbbc'))
