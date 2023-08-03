import Task2

TEST_ELEM1 = 10000
TEST_ELEM2 = 12000

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
prices2 = {"AAPL": 265.25, "GOOGL": 2605.75, "MSFT": 802.50}
print(f" calculate_portfolio_value: {Task2.calculate_portfolio_value(stocks, prices)}")
print(f" calculate_portfolio_return: {Task2.calculate_portfolio_return(TEST_ELEM1, TEST_ELEM2)}")
print(f" get_most_profitable_stock: {Task2.get_most_profitable_stock(stocks, prices)}")
