# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя.
# Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа.
# А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

from  task4 import  User
import task3
class Project():
	def __init__(self):
		self.users = User(level=7, user_id=121212, user_name="Duke").load("test")
		self.entered_user = None
	def reload_users(self):
		self.users = User(level=7, user_id=121212, user_name="Duke").load("test")

	def enter(self, id: int, name: str):
		u1 = User(user_id=id, user_name=name, level=None)
		if u1 not in self.users:
			raise task3.MyExceptionAccess
		for i in self.users:
			if i == u1:
				self.entered_user = i

	def add_user(self, id, level, name):
		if self.entered_user.level <level:
			raise task3.MyExceptionLevel
		self.users.add(User(user_id= id,level=level, user_name=name ))


if __name__ == '__main__':
	p1 = Project()
	p1.enter(id=111111, name="Fedor")
	p1.add_user(id=787878, level=1, name="User")
	print(p1.users)