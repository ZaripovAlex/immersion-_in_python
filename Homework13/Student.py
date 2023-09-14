import csv
import random
import  my_exceptions


class F_i_o_ver:
	def __init__(self, min_value: int = None, max_value: int = None):
		self.min_value = min_value
		self.max_value = max_value

	def __set_name__(self, owner, name):
		self.param_name = '_' + name

	def __get__(self, instance, owner):
		return getattr(instance, self.param_name)

	def __set__(self, instance, value):
		self.validate(value)
		setattr(instance, self.param_name, value)

	def validate(self, value: str):
		if not value.isalpha():
			raise ValueError(f"В {value} нельзя использовать ничего, кроме букв! ")
		if not value == value.capitalize():
			raise ValueError(f"В {value} слово должно начинаться с заглавной буквы")


class Student:
	surname = F_i_o_ver()
	name = F_i_o_ver()
	patronymic = F_i_o_ver()
	lesson = dict()
	tests = dict()
	scores = dict()

	def __init__(self, surname, name, patronymic):
		self.surname = surname
		self.name = name
		self.patronymic = patronymic
		self.lesson, self.tests, self.scores = self.load_dict_from_csv()



	def load_dict_from_csv(self):
		lst = []
		try:
			with open("lesson.csv", "r", encoding='utf-8', newline='') as f:
				tmp = csv.reader(f)
				for i in tmp:
					for j in i:
						lst.append(j)
		except my_exceptions.MyExceptionFile('Такого файла не существует!'):
				print()

		for i in lst:
			self.lesson[i] = []
			self.scores[i] = []
			self.tests[i] = []
		return self.lesson, self.tests, self.scores


	def test_scores(self):
		for key, val in self.lesson.items():
			tmp = self.tests[key]
			num = int(input(f'Введите оценку за тест по {key} в диапозоне от 0 до 100: '))
			if 0 < num < 100:
				tmp.append(num)
			else:
				raise my_exceptions.MyExceptionRange("Таких оценок не бывает! :( ")
			self.tests[key] = tmp

	def scores_(self):
		for key, val in self.lesson.items():
			tmp = self.scores[key]
			num = int(input(f'Введите оценку по {key}  в диапозоне от 2 до 5: '))
			if 2 < num < 5:
				tmp.append(num)
			else:
				raise my_exceptions.MyExceptionRange("Таких оценок не бывает! :( ")
			self.scores[key] = tmp

	def test_scores_gen(self, val):
		for _ in range(val):
			for key, val in self.lesson.items():
				tmp = self.tests[key]
				tmp.append(random.randint(0,101))
				self.tests[key] = tmp

	def scores_gen(self, val):
		for _ in range(val):
			for key, val in self.lesson.items():
				tmp = self.scores[key]
				tmp.append(random.randint(2,5))
				self.scores[key] = tmp
	def avg_(self):

		for key, values in self.lesson.items():
			tmp = self.lesson[key]
			tmp.append(sum(self.tests[key])/len(self.tests[key]))
			tmp.append(sum(self.scores[key]) / len(self.scores[key]))
			self.lesson[key] = tmp
		return self.lesson

	def __str__(self):
		return f"{self.surname} {self.name} {self.patronymic} {self.lesson} \n{self.tests}\n{self.scores}"


if __name__ == '__main__':
	st1 = Student(surname="Иванов", name="Иван", patronymic="Иванович")
	# print(st1)
	st1.test_scores()
	st1.scores_gen(val=10)
	st1.avg_()
	print(st1)
