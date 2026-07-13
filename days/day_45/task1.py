class BankAccount:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")


account = BankAccount(101, 500)
print(f"Current balance: {account.balance}")
try:
    account.balance = -200
except ValueError:
    print("ValueError: Balance cannot be negative")
