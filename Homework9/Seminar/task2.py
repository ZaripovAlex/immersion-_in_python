# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from random import randint

def game(num2guest: int, tries:int):

    def guesting_game():
        for _ in range(tries):
            if num2guest == int(input("Введите число: ")):
                return  True
        return False
    return guesting_game

def gaming(func):
    def wrapper(num2guest: int, tries:int):
        if 100 >= num2guest >=1:
            num2guest = randint(1, 100)
        if not 10 >= tries >= 1:
            tries = randint(1, 10)
        return func(num2guest, tries)
    return wrapper

@gaming
def guees_num(num2guest: int, tries:int):
    print(num2guest, tries)
    for _ in range(tries):
        if num2guest == int(input("Введите число: ")):
            return True
    return False


if __name__ == '__main__':

    print(guees_num(101, 11))