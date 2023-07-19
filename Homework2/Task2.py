# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6

import fractions
import math



def get_data(text: str) -> list:
    try:
        result = input(text).split("/")
        result = list(map(int, result))
        return result
    except:
        quit("Ошибка ввода")


def print_data(lst: list):
    if lst[1] == 1:
        print(f"Результат: {lst[0]}")
    else:
        print(f"Результат: {lst[0]}/{lst[1]}")



def addition(lst1: list[int], lst2: list[int]) -> list:
    result  = []
    if lst1[1] == lst2[1]:
        result.append(lst1[0] + lst2[0])
        result.append(lst1[1])

    else:
        temp = math.lcm(lst1[1],lst2[1])
        result.append(lst1[0]*int(temp/lst1[1]) + lst2[0]*int(temp/lst2[1]))
        result.append(temp)
    result = reduction(result)
    return result
def addition_fractions(lst1: list, lst2: list):
    result_fractions = fractions.Fraction(ch1[0], ch1[1]) + fractions.Fraction(ch2[0], ch2[1])
    print(f"Результат сложения fractions {result_fractions}")

def multiplication(lst1: list, lst2: list) -> list:
    result = []
    result.append(lst1[0]*lst2[0])
    result.append(lst1[1]*lst2[1])
    result = reduction(result)
    return result

def multiplication_fractions(lst1: list, lst2: list):
    result_fractions = fractions.Fraction(lst1[0], lst1[1]) * fractions.Fraction(lst2[0], lst2[1])
    print(f"Результат умножения fractions {result_fractions}")

def reduction(lst:list) -> list:
    result =[]
    temp = math.gcd(lst[0], lst[1])
    result.append(int(lst[0] / temp))
    result.append(int(lst[1] / temp))
    return result

ch1 = get_data("Введите первую дробь: \n-> ")
ch2 = get_data("Введите вторую дробь: \n-> ")
print("Сложение")
result = addition(ch1, ch2)
print_data(result)
addition_fractions(ch1, ch2)
print("Умножение")
result = multiplication(ch1, ch2)
print_data(result)
multiplication_fractions(ch1, ch2)