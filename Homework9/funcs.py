# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.

from random import randint
import csv
from deco import root_load, res_to_json
from Seminar.task3 import our_cash



@our_cash
@res_to_json

def quadratic_equation(a: int, b: int, c:int):
    """
    The function of solving the quadratic equation ax**2+b*x+c = 0

    """
    d= b**2-4*a*c
    if d < 0:
        return "there are no roots!"
    if d == 0:
        return round((-b+d**0.5)/2*a, 2)
    return round((-b+d**0.5)/2*a, 2), round((-b-d**0.5)/2*a, 2)


def csv_generator(count: int, minlim: int =1, maxlim:int = 100):
    """
    The function generates a file with the coefficients of the quadratic equation
    :param count: number of rows
    :param minlim: lower bound of generation
    :param maxlim: upper bound of generation
    """
    with open("coef.csv","w", newline="") as f:
        data = csv.writer(f,delimiter=",")
        for _ in range(count):
            a = randint(minlim, maxlim)
            b = randint(minlim, maxlim)
            c = randint(minlim, maxlim)
            data.writerow([a, b, c])




if __name__ == '__main__':
   csv_generator(100)
   rez = root_load(quadratic_equation)
   print(rez("coef.csv"))
