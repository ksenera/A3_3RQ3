from abc import ABC, abstractmethod

class Customer: 

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        
    
class Account:

    amount = 0

    def __init__(self, balance, acc_number):
        self.number = acc_number

    def check_balance():
        pass

    def withdraw():
        pass

    def deposit():
        pass


    