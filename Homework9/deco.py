# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from functools import wraps

def root_load(func):
    res = []

    @wraps(func)
    def wrapper(file):
        with open(file, "r") as f:
            rows = csv.reader(f, delimiter=",")
            for row in rows:
                a, b, c = map(int, row)
                res.append(func(a, b, c))
            return res

    return wrapper


def res_to_json(func):
    result = []

    @wraps(func)
    def wrapper(a: int, b: int, c: int):
        res = func(a, b, c)
        result.append({"a": a, "b": b, "c": c, "res": res})
        with open(f"{func.__name__}.json", "w") as f:
            json.dump(result, f, indent=2)
        return result

    return wrapper


if __name__ == '__main__':
    root_load("coef")
