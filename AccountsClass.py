from abc import ABC, abstractmethod

class Customer: 

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        self.account = []
        
    
class Account(ABC):

    def __init__(self, acc_number):
        self.__number = acc_number
        self.__balance = 0

    def check_balance(self):
        pass

    def withdraw(self):
        pass

    def deposit(self):
        pass

    @abstractmethod
    def print(self):
        pass

class SavingsAccount(Account):
    def __init__(self, acc_number, interest_rate):
        super().__init__(acc_number)
        self.__interest = interest_rate

    def calculate_return(self):
        pass 

    def print(self):
        pass


class CheckingAccount(Account):
    def __init__(self, acc_number):
        super().__init__(acc_number)
    def transaction(self):
        pass

    def print(self):
        pass 