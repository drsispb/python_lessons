'''Задача 4. Односвязный список
Что нужно сделать
Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.

Связный список — это структура данных, которая состоит из элементов, называющихся узлами. В узлах хранятся данные,
а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.
В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только
в сторону конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и
дополнительных модулей.

Для реализации напишите два класса: Node и LinkedList. В Node должна быть логика работы одного узла
(хранение данных и указателя).

Для структуры реализуйте следующие методы:

append — добавление элемента в конец списка;
get — получение элемента по индексу;
remove — удаление элемента по индексу.
Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.

Пример основной программы:
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

Результат:
Текущий список: [10 20 30]
Получение третьего элемента: 30
Удаление второго элемента.
Новый список: [10 30]'''

from typing import Any, Optional

class Node:
    def __init__(self, data: Optional[Any] = None, next: Optional['Node'] = None ) -> None:
        self.data = data
        self.next = next

    def __str__(self)-> str:
        return 'Node[{data}]'.format(
            data=str(self.data)
        )
class LinkedList:

    def __init__(self)->None:
        self.head: Optional[Node] = None
        self.lenght = 0

    def __str__(self)-> str:
        if self.head is not None:
            current = self.head
            data = [str(current.data)]
            while current.next is not None:
                current = current.next
                data.append(str(current.data))
            return '[{data}]'.format(data=' '.join(data))
        return 'LinkedList []'



    def append(self, elem: Any)->None:
        new_node = Node(elem)
        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.lenght += 1

    def remove(self, index)->None:
        cur_node = self.head
        cur_index = 0
        if self.lenght == 0 or self.lenght <= index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.lenght -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break

            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.lenght -= 1




my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)

print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)