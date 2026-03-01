from abc import ABC, abstractmethod

class Customer: 

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        
    
class Account(ABC):

    def __init__(self, balance, acc_number):
        self.__number = acc_number
        self.__balance = balance

    def check_balance(self):
        

    def withdraw(self):
        pass

    def deposit(self):
        pass

    @abstractmethod
    def print(self):
        pass

class SavingsAccount(Account):
    def __init__(self, interest_rate):
        self.__interest = interest_rate

    def calculate_return(self):
        pass 

    def print(self):
        pass