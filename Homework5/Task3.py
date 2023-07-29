# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacci(n):

    if n >= 0:
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    else:
        a, b = 0, -1
        for _ in range(abs(n)):
            yield a
            a, b = b, a - b


print(*fibonacci(10))
print(*fibonacci(-10))