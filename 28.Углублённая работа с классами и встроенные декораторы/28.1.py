'''Задача 1. Работа с файлом 2
Что нужно сделать
Реализуйте модернизированную версию контекст-менеджера File:

теперь при попытке открыть несуществующий файл менеджер должен автоматически
создавать и открывать этот файл в режиме записи;
на выходе из менеджера должны подавляться все исключения, связанные с файлами.'''
import os.path
from typing import Any, Union

class File:

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        if not os.path.exists(self.filename):
            self.file = open(self.filename, 'w')
        else:
            self.filename = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File("example_2.txt", "r") as file:
    file.write("Всем привет!")
