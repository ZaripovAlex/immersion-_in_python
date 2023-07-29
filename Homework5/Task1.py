# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def str_to_tuple(path:str) :
    path=path.replace("\\", "/")
    *lst, filename = path.rsplit('/',1)
    *filename, extension = filename.split(".")
    return *lst, *filename, extension
    



path = "C:\\Users\Duke\Desktop\example.txt"
print(str_to_tuple(path))