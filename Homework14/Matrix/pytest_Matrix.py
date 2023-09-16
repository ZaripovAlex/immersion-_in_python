from Homework14.Matrix.Matrix import Matrix
import pytest


def test_matrix_add():
	m1 = Matrix(3, 3)
	m1.matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
	m2 = Matrix(3, 3)
	m2.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	res = m1 + m2
	sum_matrix = [[2, 4, 6], [5, 7, 9], [8, 10, 12]]
	assert (res.matrix == sum_matrix), 'Сложение не прошло'


def test_matrix_eq():
	m1 = Matrix(3, 3)
	m1.matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
	m3 = Matrix(3, 3)
	m3.matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
	m2 = Matrix(3, 3)
	m2.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	assert (m1 == m3)
	assert (m1 != m2)


if __name__ == '__main__':
	pytest.main(['-v'])

