"""
Encapsulation
"""

# encapsulation
class BankAccount:
    def __init__(self, name, balance, account_no):
        self.name = name #public
        self._account_no = account_no #protected
        self.__balance = balance #protected
        
    def get_balance(self):
        return self.__balance

    def set_balance(self, newBalance):
        self.__balance = newBalance;
    
acc = BankAccount("Prasad", 1000000, 10)
print(acc.name, acc._account_no)
acc.set_balance(120)

print(acc._BankAccount__balance)
print(acc.get_balance())

#inheritance