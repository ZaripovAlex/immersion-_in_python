# ЗАДАЧА 2: Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv
from random import randint
from pathlib import Path
import os
__all__ =["rename"]
def rename(wanted_name: str, count_nums: int =3,
           extension_old: str =".txt", extension_new :str = ".csv",
           diapazon: list =[3, 6], directory = "test"):
    os.chdir(directory)
    path = Path(Path().cwd())
    num = 1
    for elem in path.iterdir():
        file = str(elem).rsplit("\\", 1)[1]
        name, ext = file.split('.')
        if extension_old == f".{ext}":
            # print(name, ext)
            ext = extension_new
            name = name[diapazon[0]:diapazon[1]]
            # print(name, ext)
            number = randint(1, 10*count_nums+1)
            os.rename(elem, name+wanted_name+str(number)+ext)


if __name__ == '__main__':
        rename("QWEQWE")