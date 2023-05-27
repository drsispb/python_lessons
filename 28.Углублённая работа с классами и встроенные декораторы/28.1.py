'''Задача 1. Работа с файлом 2
Что нужно сделать
Реализуйте модернизированную версию контекст-менеджера File:

теперь при попытке открыть несуществующий файл менеджер должен автоматически
создавать и открывать этот файл в режиме записи;
на выходе из менеджера должны подавляться все исключения, связанные с файлами.'''

class File:

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File("example.txt", "w") as file:
    file.write("Всем привет!")
