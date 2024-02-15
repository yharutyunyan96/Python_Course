class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.set_balance(balance)   # private attribute

    def get_balance(self):          # getter method
        return self.__balance

    def set_balance(self, amount):  # setter method
        if amount > 0:
            self.__balance = amount

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, new_account_number):
        self.__account_number = new_account_number

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

    def transfer(self, other_account, amount):
        if isinstance(other_account, BankAccount):
            if self.__balance >= amount:
                self.__balance -= amount
                other_account.__balance += amount


bank_account_1 = BankAccount(account_number=1111, balance=10000)
bank_account_2 = BankAccount(account_number=2222, balance=20000)

# print(bank_account_1.balance)
# bank_account_1.balance = -10000

# print(bank_account_1.__balance)
# print(bank_account_1._BankAccount__balance)     # Name mangling

# bank_account_1._BankAccount__balance = -10000
# print(bank_account_1._BankAccount__balance)

# current_balance = bank_account_1.get_balance()
# print(current_balance)
#
# bank_account_1.set_balance(-20000)
# current_balance = bank_account_1.get_balance()
# print(current_balance)

print(f"Current balance: {bank_account_1.get_balance()}")
bank_account_1.deposit(20000)
print(f"Current balance after deposit 20.000: {bank_account_1.get_balance()}")
bank_account_1.withdraw(5000)
print(f"Current balance after withdraw 5.000: {bank_account_1.get_balance():,}")

bank_account_1.transfer(bank_account_2, amount=10000)
print(f"Current balance after transfer to {bank_account_2.get_account_number()}: {bank_account_1.get_balance()}")
print(bank_account_2.get_balance())