"""Задача 6. Поиск разницы между двумя JSON-файлами (пример из реального тестового задания на должность
Python-разработчика уровня Junior)
Что нужно сделать
Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list, выведите различие.
Иными словами, вам нужно отловить изменение определённых параметров и вывести значение: что изменилось и на что.
Набор ключей в обоих файлах идентичный, различаются лишь значения.

Напишите программу, которая:
загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
выполняет сравнение параметров, указанных в diff_list;
формирует результат в виде словаря;
записывает словарь в JSON-файл с названием result.json.
Исходные данные
Файлы:
json_old.json,
json_new.json.
Список параметров для отслеживания (можно сформировать инпутом или ввести вручную):
diff_list = [‘services’, ‘staff’, ‘datetime’]
Формат итогового словаря с результатом:
Словарь {параметр: новое_значение, ….}
Пример
Данные, загруженные из json_old.json:"""

import json
from typing import Dict, List

with open('json_new.json', 'r') as new_file:
    new_data = json.load(new_file)

with open('json_old.json', 'r') as old_file:
    old_data = json.load(old_file)


def check(before_dict: Dict, after_dict: Dict, diff_list: List[str]) -> Dict:
    dict_of_values: Dict = {}
    for key in before_dict.keys():
        if isinstance(before_dict[key], dict):
            check(before_dict[key], after_dict[key], diff_list)
        elif before_dict[key] != after_dict[key] and key in diff_list:
            dict_of_values[key] = after_dict[key]
    return dict_of_values


diff_list: List[str] = ["services", "staff", "datetime"]
result: Dict = check(old_data, new_data, diff_list)
print(result)

with open('result.json', 'w') as final:
    json.dump(result, final, indent=4)
