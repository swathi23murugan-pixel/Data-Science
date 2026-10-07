class InsufficientFundsError(Exception):
    pass
class NegativeAmountError(Exception):
    pass
class BankAccount:
    def __init__(self,id,balance):
        self.id=id
        self.__balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise NegativeAmountError()
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<=0:
            raise NegativeAmountError()
        if amount>self.__balance:
            raise InsufficientFundsError()
        self.__balance-=amount
    def get_balance(self):
        return self.__balance
acc=BankAccount("ACC1001",500.0)
acc.deposit(200.0)
acc.withdraw(300.0)
print(acc.get_balance())