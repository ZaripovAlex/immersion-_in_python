# Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.
from functools import wraps
def param(count: int):
    def deco(func):
        my_list = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list
        return wrapper
    return deco



@param(3)
def sum_(a: int, b:int) :
    return a+b



print(sum_(2,5))