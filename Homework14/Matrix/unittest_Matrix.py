import unittest
from Homework14.Matrix.Matrix import  Matrix

MATRIX1 = Matrix(3,3).matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
MATRIX2 = Matrix(3,3).matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
MATRIX3 = Matrix(3,3).matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
SUM_MATRIX = Matrix(3,3).matrix = [[2, 4, 6], [7, 7, 7], [11, 13, 15]]
MUL_MATRIX = Matrix(3,3).matrix = [[30, 36, 42], [18, 24, 30], [66, 81, 96]]


class TestMatrix(unittest.TestCase):

	def test_eq(self):
		self.assertTrue(MATRIX1 == MATRIX2)
		self.assertFalse(MATRIX1 == MATRIX3)
		self.assertTrue(MATRIX1 != MATRIX3)
		self.assertFalse(MATRIX1 != MATRIX2)

	def test_add(self):
		self.assertFalse(SUM_MATRIX == (MATRIX1 + MATRIX3))
		self.assertFalse(SUM_MATRIX == (MATRIX1 + MATRIX2))








if __name__ == '__main__':
	unittest.main(verbosity=2)