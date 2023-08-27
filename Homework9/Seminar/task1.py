# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.


def game(num2guest: int, tries:int):

    def guesting_game():
        for _ in range(tries):
            if num2guest == int(input("Введите число: ")):
                return  True
        return False
    return guesting_game


if __name__ == '__main__':
    process = game(10,3)
    print(process())