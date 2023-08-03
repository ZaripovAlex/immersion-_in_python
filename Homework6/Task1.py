# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from sys import argv


date = '29.02.2004'


def _leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # print('Год високосный.')
        return True
    return False
    # print('Год не високосный.')


__all__ = ['date_check']


def date_check(date):
    list_31_days = ['01', '03', '05', '07', '08', '10', '12']
    list_30_days = ['04', '06', '09', '11']
    list_28_days = ['02']
    day, month, year = date.split('.')
    if month in list_31_days and 0 < int(day) < 32 and 0 < int(year) < 10000:
        return True
    elif month in list_30_days and 0 < int(day) < 31 and 0 < int(year) < 10000:
        return True
    elif month in list_28_days and 0 < int(day) < 30 and 0 < int(year) < 10000 and _leap_year(int(year)):
        return True
    elif month in list_28_days and 0 < int(day) < 29 and 0 < int(year) < 10000 and not _leap_year(int(year)):
        return True
    return False


if __name__ == '__main__':
    arg = argv[1:]
    print(date_check(*arg))