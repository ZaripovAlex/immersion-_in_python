# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

class My_dict(dict):

	def my_get(self, key_, value_=None):
		try:
			return self[key_]
		except KeyError as e:
			return value_


if __name__ == '__main__':
	d1 = My_dict()
	print(d1.my_get("key", 1))