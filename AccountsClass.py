from abc import ABC, abstractmethod

class Customer: 

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        
    
class Account:

    def __init__(self, balance, acc_number):
        self.__number = acc_number
        self.__balance = balance

    def check_balance(self):
        pass 

    def withdraw(self):
        pass

    def deposit(self):
        pass


    