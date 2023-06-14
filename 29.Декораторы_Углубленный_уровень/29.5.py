'''Задача 5. Синглтон
Что нужно сделать
Синглтон — это порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр, и
предоставляет к этому экземпляру глобальную точку доступа. Синглтонами мы уже пользовались, к ним относятся, например,
None, True и False. Благодаря тому, что None — синглтон, можно использовать оператор is: он возвращает True только для
объектов, представляющих одну и ту же сущность.

Реализуйте декоратор singleton, который превращает класс в одноэлементный. При множественной инициализации объекта
этого класса будет сохранён только первый инстанс, а все остальные попытки создания будут возвращать первый экземпляр.

Пример кода:

@singleton
class Example:
    pass

my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
Результат:
1986890616688
1986890616688
True'''


def singleton(cls):
    instance = {}

    def wrapped(*args, **kwargs):
        if cls not in instance.keys():
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)
