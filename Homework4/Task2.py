# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def kvarg_to_dict(**kwargs):
    result = dict()
    for key, value in kwargs.items():
        if check_hash(value):
            result[value] = key
        else:
            result[str(value)] = key
    return result


def check_hash(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False


a = kvarg_to_dict(res=1, reverse=[1, 2, 3], a=2, b=3)
print(a)
