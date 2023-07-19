# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

BIN = 2
OCT = 8
HEX = 16


def func(num: int, base: int):
    result = ''
    temp = ''
    while num > 0:
        temp = num % base
        num //= base
        if temp > 10:
            match temp:
                case 10:
                    result = "a" + result
                case 11:
                    result = "b" + result
                case 12:
                    result = "c" + result
                case 13:
                    result = "d" + result
                case 14:
                    result = "e" + result
                case 15:
                    result = "f" + result
        else:
            result = str(temp) + result
    return result


num = int(input("Введите число\n-> "))
print(f"Число {num} в двоичном виде {func(num, BIN)} . При помощи bin() {bin(num)}")
print(f"Число {num} в восьмеричном виде {func(num, OCT)} . При помощи oct() {oct(num)}")
print(f"Число {num} в шестнадцатеричном виде {func(num, HEX)} . При помощи hex() {hex(num)}")
