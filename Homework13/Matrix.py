# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

from random import randint
import numpy as np
import my_exceptions


class Matrix:
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
				except my_exceptions.MyExceptionMatrixElemType():
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
	m1 = Matrix(2, 2)
	m1.input()
	m1.print_matrix()
	print()
	m2 = Matrix(2, 2)
	m2.input()
	m2.print_matrix()
	print()
	print(m1 == m2)
	print()
	print(m1 * m2)
	(m1+m2).print_matrix()
	

