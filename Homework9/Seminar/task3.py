# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

import json
from typing import Callable
from functools import wraps

def our_cash(func: Callable):
    try:
        with open(f"{func.__name__}.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        arg = str(args)+str(kwargs)
        data_res = data.get(arg)
        if data_res:
            return data_res
        rez = func(*args, **kwargs)
        data.update({arg:rez})
        with open(f"{func.__name__}.json", "w") as f1:
            json.dump(data, f1, indent=2)
        return rez
    return wrapper

@our_cash
def sum(a: int, b:int):
    return a+b

@our_cash
def mult(a:int, b: int):
    return a*b

if __name__ == '__main__':
    print(sum(2,3))
    print(mult(2,3))
    print(sum(2, 8))
    print(mult(2, 91))