from abc import ABC, abstractmethod

class Customer: 

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        self.accounts = []

    def open_savings_account(self, acc_number, interest_rate):
        savings_acc = SavingsAccount(acc_number, interest_rate)

    def open_checking_account(self, acc_number):
        checking_acc = CheckingAccount(acc_number)
    
        
    
class Account(ABC):

    def __init__(self, acc_number):
        self.__number = acc_number
        self.__balance = 0

    def check_balance(self):
        return self.__balance 

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    @abstractmethod
    def print(self):
        pass

class SavingsAccount(Account):
    def __init__(self, acc_number, interest_rate):
        super().__init__(acc_number)
        self.__interest = interest_rate

    def calculate_return(self, balance, interest_rate):
        return self.__balance * self.__interest

    def print(self):
        pass


class CheckingAccount(Account):
    def __init__(self, acc_number):
        super().__init__(acc_number)

    def transaction(self, amount):
        pass

    def print(self):
        pass 