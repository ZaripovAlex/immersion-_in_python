class MyException(Exception):
	pass

class MyExceptionRange(MyException):
	def __init__(self, msg:str):
		self.msg = msg
	def __str__(self):
		return f'{self.msg}! Так нельзя делать! '
class MyExceptionFile(MyException):
	def __init__(self, msg:str):
		self.msg = msg
	def __str__(self):
		return f'{self.msg}'

class MyExceptionMatrixElemType(MyException):

	def __str__(self):
		return f'Элементами матрицы могут быть только числа '
