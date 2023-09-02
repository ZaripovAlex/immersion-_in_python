import math
class Fractions:
	ch: int = 0
	zn: int = 0

	def __init__(self, ch, zn):
		self.ch = ch
		self.zn = zn

	def __str__(self):
		return f"{self.ch}/{self.zn}"

	def __add__(self, other: "Fractions"):
			rez_ch = None
			rez_zn = None
			if self.ch == other.ch:
				rez_ch = self.ch + other.ch
				rez_zn = self.zn
				return Fractions(rez_ch, rez_zn)
			else:
				rez_zn = math.lcm(self.zn, other.zn)
				rez_ch = (self.ch * int(rez_zn / self.zn + other.ch * int(rez_zn / other.zn)))
				tmp = Fractions(rez_ch, rez_zn)
				# result = self.reduction(tmp)
			return tmp.reduction()

	def __mul__(self, other) -> "Fractions":
			tmp = (Fractions(self.ch * other.ch, self.zn*other.zn))
			return  tmp.reduction()


	def reduction(self) -> "Fractions":
		temp = math.gcd(self.ch, self.zn)
		tmp_ch = int(self.ch / temp)
		tmp_zn = int(self.zn / temp)
		tmp = Fractions(tmp_ch, tmp_zn)
		return tmp


if __name__ == '__main__':
	f1 = Fractions(1,2)
	f2 = Fractions(2,3)
	print(f1+f2)
	print(f1*f2)



