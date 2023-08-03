# Задача: Расчет финансовых показателей портфеля акций
#
# Описание задачи:
# Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля акций.
# Создайте модуль Python под названием "portfolio.py", который будет содержать функции для выполнения следующих операций:
import datetime


# Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float
# принимает два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.),
# и значениями - количество акций каждого символа. prices - словарь, где ключами являются символы акций,
# а значениями - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля акций на
# основе количества акций и их текущих цен.
# Пример: Input
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
# OUT
# 16410,25
#
# Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float
# принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость
# портфеля акций. Функция должна вернуть процентную доходность портфеля.
# Пример:
# Пришло:
# 10000.0
# 15000.0
# Вышло:
# 50%
#
# Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str
# принимает два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами.
# Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.
# Начальная стоимость - первый вызов calculate_portfolio_value,
# данные из этого вызова следует сохранить в защище    нную переменную на уровне модуля.
# Пример:
# Пришло:
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
# Вышло:
# MSFT
#
#
# Тестирование модуля:
#
# Напишите небольшую программу, которая импортирует модуль "portfolio.py" и демонстрирует использование всех трех функций.
# Создайте словари для акций и цен, запустите функции и выведите результаты.
# Примечание:
# В реальном мире вы можете использовать API для получения актуальных данных о ценах акций. В данной задаче можно использовать фиктивные данные для тестирования и обучения.
#

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    res = []
    for elem in zip(stocks.values(), prices.values()):
        # print(f"{elem} {elem[0]*elem[1]}")
        res.append(elem[0] * elem[1])
    # print(res)
    return sum(res)


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    # print((current_value-initial_value)/initial_value)
    return round(((current_value-initial_value)/initial_value)*100, 2)

def get_most_profitable_stock(stocks: dict, prices: dict):
        # -> str:
    res = dict()
    for elem1, elem2 in zip(stocks.items(), prices.items()):
        # print(f"{elem1=}, {elem2=}")
        res[elem1[0]] = elem1[1]*elem2[1]
    # print(res)
    return max(res)


if __name__ == '__main__':
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
    prices2 = {"AAPL": 265.25, "GOOGL": 2605.75, "MSFT": 802.50}
    print(calculate_portfolio_value(stocks, prices))
    print(calculate_portfolio_return(TEST_ELEM1, TEST_ELEM2))
    print(get_most_profitable_stock(stocks,prices))