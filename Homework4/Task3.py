# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


PERCENTAGE_FOR_WITHDRAWAL = 0.015
OPERATION_ADDED = 3
PERCENTAGE_FOR_REPLENISHMENT = 0.03
MIN_PERCENTAGE = 30
MAX_PERCENTAGE = 600
MIN_BANKNOTE = 50
MIN_TAX = 5_000_000
LUXURY_TAX = 0.1

operation_log = []


def logging(operation: str):
    """Логирование"""
    operation_log.append(operation)


def show_log():
    """Отображение лога операций"""
    print("-- ЛОГ ОПЕРАЦИЙ --")
    for o in operation_log:
        print(o)


def tax_pay(summ: float) -> float:
    """Удержание налога"""
    tax = summ * LUXURY_TAX
    print(f"Налог: {tax:.2f}")
    summ -= tax
    return summ


def push_cash(balance: float) -> (bool, float):
    """Положить деньги на счет
    """
    summ = float(input("Сумма для пополнения: "))
    result = False
    if balance > MIN_TAX:
        balance = tax_pay(balance)
    if summ % 50 == 0:
        balance += summ
        print(f"Баланс пополнен: {summ:.2f}")
        result = True
    else:
        print("Недоступная сумма!")
    show_balance(balance)
    return result, balance


def pull_cash(balance: float) -> (bool, float):
    """Снятие денег со счета
    """
    result = False
    show_balance(balance)
    summ = float(input("Сумма для снятия: "))
    if balance > MIN_TAX:
        balance = tax_pay(balance)
    if summ % 50 == 0:
        percent_summ = summ * PERCENTAGE_FOR_WITHDRAWAL
        if percent_summ > MAX_PERCENTAGE:
            percent_summ = MAX_PERCENTAGE
        if percent_summ < MIN_PERCENTAGE:
            percent_summ = MIN_PERCENTAGE
        if balance - summ - percent_summ < 0:
            print("Недостаточно средств!")
        else:
            balance -= (summ + percent_summ)
            print(f"Выдано {summ:.2f}, комиссия {percent_summ:.2f}")
            result = True
    else:
        print("Недоступная сумма!")

    return result, balance


def show_balance(summ: float):
    """Отображение баланса"""
    print(f"Баланс счета: {summ:.2f}")


def show_menu(menu: dict[int, str]) -> int:
    """Отображение меню."""
    for k, v in menu.items():
        print(f"{k} - {v}")
    result = int(input("> "))
    return result if result in menu.keys() else 0


def main():
    balance: float = 0
    operation_counter = 0
    menu_bank: dict = {
        1: "снять",
        2: "пополнить",
        3: "баланс",
        0: "выход",
    }


    while True:
        action = show_menu(menu_bank)
        match action:
            case 1:
                success, balance = pull_cash(balance)
                if success:
                    operation_counter += 1
                logging(f"СНЯТИЕ - {'Ok' if success else 'ERROR'}")
            case 2:
                success, balance = push_cash(balance)
                if success:
                    operation_counter += 1
                logging(f"ПОПОЛНЕНИЕ - {'Ok' if success else 'ERROR'}")
            case 3:
                show_balance(balance)
            case _:
                show_log()
                quit("Приходите еще :) ")

        if operation_counter == OPERATION_ADDED:
            operation_counter = 0
            summ_add = balance * PERCENTAGE_FOR_REPLENISHMENT
            print(f"Начисление %: {summ_add:.2f}")
            balance += summ_add
            show_balance(balance)
            show_log()

if __name__ == "__main__":
    main()
