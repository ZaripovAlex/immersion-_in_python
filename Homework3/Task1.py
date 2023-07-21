# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

from random import randint

START_LIMIT = 0
STOP_LIMIT = 10


def list_generator(length) -> list:
    result = []
    for _ in range(length):
        result.append(randint(START_LIMIT, STOP_LIMIT))
    return result


def func(lst: list) -> list:
    result = set()
    for i in lst:
        if lst.count(i) > 1:
            result.add(i)

    return list(result)


lst = list_generator(10)
print(f'Исходный список: {lst}')
rez = func(lst)
print(f'Результирующий список: {rez}')
