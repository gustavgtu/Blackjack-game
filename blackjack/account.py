class Account:
    def __init__(self):
        self.__balance=0

    def deposit(self, amount):
        self.__balance+=amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance-=amount
        else:
            print("You don't have enough money")

    def get_balance(self):
        return self.__balance