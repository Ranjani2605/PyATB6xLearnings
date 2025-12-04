class Bank:


    def __init__(self, account_number, balance, pin):
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = pin

    def check_balance(self):
        return self.__balance

    def show_account_number(self, pin):
        if pin == self.__pin:
            return self.__account_number
        return 'Access Denied: Wrong PIN'

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            return 'Old PIN is incorrect.'
        self.__pin = new_pin
        return 'PIN updated successfully.'

    def deposit(self, amount):
        if amount <= 0:
            return 'Deposited amount must be positive.'
        self.__balance += amount
        return f"Deposited {amount}. New balance = {self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return 'Withdraw amount must be positive.'
        if amount > self.__balance:
            return 'Insufficient balance.'
        self.__balance -= amount
        return f"Withdraw {amount}. Remaining balance = {self.__balance}"

    def account_details(self, pin):
        if pin == self.__pin:
            return f"Account: {self.__account_number}, Balance: {self.__balance}"
        return 'Access Denied: Wrong PIN.'


customer = Bank('ACC1220', 1000, 1234)
print(customer.account_details(1234))
customer.withdraw(500)
print(customer.account_details(4568))





