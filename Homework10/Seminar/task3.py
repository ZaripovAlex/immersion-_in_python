# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
# на ваш выбор. Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

class Person:

    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

if __name__ == '__main__':
    p1 = Person("Ivanov", 'Ivan', 'Ivanovich', 25)
    #print(p1.__age)
    print(p1.get_age())
    print(p1.name)
    print(p1)
