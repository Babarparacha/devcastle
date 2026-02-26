class bankAccount:
    def __init__(self,name,balance):
        self.public_name=name
        self._account_type="saving"
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance=amount
            print("Deposited amount",amount)
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("Withdraw amount",amount)
        else:
            print("you have insuficient balance")
    def show(self):
        print("current balance",self.__balance)

account=bankAccount("babar",5000)
print(account.public_name)
# account.deposit(200)
account.withdraw(100)