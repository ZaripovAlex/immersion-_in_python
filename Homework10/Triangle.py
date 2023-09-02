class Triangle:
	side_a: int = 0
	side_b: int = 0
	side_c: int = 0
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def exist(self) -> bool:
		if (self.side1 + self.side2 > self.side3
				and self.side1 + self.side3 > self.side2
				and self.side3 + self.side2 > self.side1):
			print("Существует!")
			return  True

		else:
			print("Несуществует!")
			return False
	def __str__(self):
		if self.exist():
			return f"Треугольник со сторонами {self.side1 =}, {self.side2 =}, " \
				   f"{self.side3 =} существует. Треугольник {self.triangle_type()}"
		else:
			f"Треугольник со сторонами {self.side1 =}, {self.side2 =},{self.side3 =} несуществует."

	def triangle_type(self) -> str:
			if (self.side1 == self.side2 == self.side3):
				return "Равносторонний"
			elif (self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3):
				return "Равнобедренный"
			else:
				return "Разностронний"


if __name__ == '__main__':
		tr1 = Triangle(side1= 5, side2= 5, side3= 5)
		print(tr1)
