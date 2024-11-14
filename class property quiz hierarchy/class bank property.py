class Bank:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError('Баланс не может быть отрицательным')
        self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть положительной')
        self._balance += amount
        print(f'Пополнено на {amount}. Новый баланс: {self.balance}')

    def remove(self, amount):
        if amount <= 0:
            raise ValueError('Сумма снятия должна быть положительной')
        if amount > self._balance:
            raise ValueError('Недостаточно средств для снятия')
        self._balance -= amount
        print(f"Снято {amount}. Новый баланс: {self.balance}")


bank_account = Bank(100)
print(f"Начальный баланс: {bank_account.balance}")
bank_account.deposit(50)
print(f"Баланс после пополнения: {bank_account.balance}")
bank_account.remove(30)
print(f"Баланс после снятия: {bank_account.balance}")

