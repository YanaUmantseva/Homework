
class Bank:
    def __init__(self):
        self.account = None

    def open_account(self):
        if self.account is None:
            self.account = 0
            print("Счет открыт, текущий баланс:", self.account)


    def close_account(self):
        if self.account is not None:
            self.account = None
            print("Счет закрыт.")


    def deposit(self, amount):
        if self.account is not None:
            if amount > 0:
                self.account += amount
                print(f"Пополнено на {amount}. Текущий баланс:", self.account)


    def withdraw(self, amount):
        if self.account is not None:
            if 0 < amount <= self.account:
                self.account -= amount
                print(f"Снято {amount}. Текущий баланс:", self.account)



bank = Bank()
bank.open_account()
bank.deposit(150)
bank.withdraw(50)
bank.close_account()