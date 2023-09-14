# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора
# строки и время создания
# (time.time)


import time


class MyStr(str):
    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time_create = time.time()
        return instance

    def __repr__(self):
        return f'MyStr({self.value =}, {self.name =}, {self.time_create =})'


if __name__ == "__main__":
    str1 = MyStr(value="Это моя строка", name='Федор')
    print(repr(str1))
    print(str1.name)
    print(str1.time_create)