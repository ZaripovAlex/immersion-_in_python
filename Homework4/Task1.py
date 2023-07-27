# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def print_matrix(lst: list[list[int]]):
    """
    Печатает матрицу
    """
    print()                     #для красоты
    for i in lst:
        for j in i:
            print(j, end="\t")
        print()
    print()                     #для красоты


def matrix_transposition(lst: list[list[int]]) -> list:
    """
    Транспонирует матрицу
    """
    result = []
    for i in zip(*lst):
        result.append(list(i))
    return result


matrix = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
print("Исходная матрица: ")
print_matrix(matrix)
result_matrix = matrix_transposition(matrix)
print("Транспонированная матрица: ")
print_matrix(result_matrix)
