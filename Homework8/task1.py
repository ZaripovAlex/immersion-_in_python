# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
#
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }
#
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
#
import json
import os
from os.path import  getsize

# def directory_scan(directory:str):
#     for elem in os.walk(directory):
#         print(elem)
def directory_scan(directory):
    res = []
    for root, dirs , files in os.walk(directory):

            for file in files:
                path =root
                extension = file.split(".")[1]
                *_, root = root.rsplit("\\", maxsplit=1)
                size = getsize(os.path.join(directory, path, file))
                res.append({
                    "name": file,
                    "extension":extension,
                    "type" : "file",
                    "parent": os.path.basename(root),
                    "size":size
                })
            for dir in dirs:
                res.append({
                    "name": dir,
                    "parent": os.path.basename(root),
                    "type": "dir"
                })
    return res
def list_to_json(file:str, data:list):
    with open(file,"w") as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    list_to_json("file.json",directory_scan("C:\\Users\\Алексей\\Desktop\\test"))
