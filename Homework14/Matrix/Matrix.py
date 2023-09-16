# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

from random import randint
import numpy as np
import Homework13.my_exceptions


class Matrix:
	"""
	Класс Matrix:
	Принимает два аргумента m, n
	m - количество строк
	n - количество столбцов
	Метод Input() - Предназначен для ручного ввода матрицы
	Метод generate() - Предназначен для генерации элементов матрицы в диапазоне от 0 до 9
	Метод print_matrix() - Предназначен для вывода матрицы на экран

	>>> m1 = Matrix(3, 3)
	>>> m1.matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
	>>> m2 = Matrix(3, 3)
	>>> m2.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	>>> m3 = Matrix(3, 3)
	>>> m3.matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
	>>> m1 != m3
	False
	>>> m1 != m2
	True
	>>> m3 = m1 + m2
	>>> m3.print_matrix()
	[2, 4, 6]
	[5, 7, 9]
	[8, 10, 12]

	"""
	m: int = 0
	n: int = 0

	def __init__(self, m: int, n: int):
		self.matrix = []
		self.m = m
		self.n = n

	def input(self):
		rez = []
		num = 0
		for _ in range(self.n):
			for _ in range(self.m):
				try:
					num = int(input("Введите элемент матрицы: "))
				except Homework13.my_exceptions.MyExceptionMatrixElemType():
					print()
				rez.append(num)
			# print(rez)
			self.matrix.append(rez)
			rez = []

	def __eq__(self, other: "Matrix"):
		if (self.m != other.m) or (self.n != other.n):
			return False
		return np.array_equal(self.matrix, other.matrix)

	def __add__(self, other:"Matrix"):
		res = Matrix(self.m, self.n)
		res.matrix= [[self.matrix[i][j] + other.matrix[i][j]  for j in range
		(len(self.matrix[0]))] for i in range(len(self.matrix))]
		return res

	def __mul__(self, other):

		return np.dot(self.matrix, other.matrix)

	def print_matrix(self):
		for i in range(len(self.matrix)):
			print(self.matrix[i])

	def generate(self):
		rez = []
		for _ in range(self.n):
			for _ in range(self.m):
				rez.append(randint(1, 10))
			# print(rez)
			self.matrix.append(rez)
			rez = []


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)

	# m1 = Matrix(2, 2)
	# m1.input()
	# m1.print_matrix()
	# print()
	# m2 = Matrix(2, 2)
	# m2.input()
	# m2.print_matrix()
	# print()
	# print(m1 == m2)
	# print()
	# print(m1 * m2)
	# (m1+m2).print_matrix()


