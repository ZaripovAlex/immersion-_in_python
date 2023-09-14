# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
import json


class User:
	def __init__(self, user_id: int, level: int, user_name: str) -> None:
		self.__user_id = user_id
		self.level = level
		self.user_name = user_name
	def __repr__(self):
		return f"ID:{self.__user_id} Уровень доступа {self.level} имя {self.user_name}"

	def __eq__(self, other:"User"):
		return self.user_name == other.user_name and self.__user_id == other.__user_id

	def __hash__(self):
		return int(hash(self.__user_id))
	def load(self, file_name):
		with open(f"{file_name}.json", "r", encoding="utf-8") as f:
			data = json.load(f)
		users:set = set()
		for user in data:
			users.add(User(*user.values()))
		return users


if __name__ == '__main__':
	u1 = User(level=222, user_id="121212", user_name="Duke")
	print(u1.load("test"))