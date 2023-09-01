# Задача 2. Доработаем задания 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

import random



class Dog:
    def __init__(self, name:str, breed:str, age:int):
        self.name = name
        self.breed = breed
        self.age = age
    def __str__(self):
        return f"Собака породы {self.breed}. Кличка - {self.name}. Возраст {self.age} лет(года)"

class Cat:
    def __init__(self, name:str, breed:str, age:int):
        self.name = name
        self.breed = breed
        self.age = age
    def __str__(self):
        return f"Кошка породы {self.breed}. Кличка - {self.name}. Возраст {self.age} лет(года)"


class Rabbit:
    def __init__(self, name:str, breed:str, age:int):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f"Кролик породы {self.breed}. Кличка - {self.name}. Возраст {self.age} лет(года)"

class Factory:
    animal = []

    def __init__(self, other):
        self.animal.append(other)

    def add(self, other):
        self.animal.append(other)

    def __str__(self):
        rez =''
        for i in self.animal:
            rez+= f"{i}" +"\n"
        return rez






if __name__ == '__main__':
    d1 = Dog(name="Бобик", breed="Пудель", age= 2)
    # print(d1, d1.__class__)
    c1 = Cat(name="Мурка", breed="Сфинкс", age=1)
    # print(c1, c1.__class__)
    r1 = Rabbit(name="Степашка", breed="Серый великан", age=1)
    # print(r1, r1.__class__)
    f1 = Factory(d1)
    f1.add(c1)
    f1.add(r1)
    print(f1)