class Bank:
    balance=0
    def __init__(self,accountno,name):
        self.accountno=accountno
        self.name=name
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def display(self):
        print("Account No.:",self.accountno,"Name:",self.name,"Balance:",self.balance)
b1=Bank(1,"Shaiju")
b1.deposit(1000)
b1.withdraw(500)
b1.display()
b2=Bank(2,"Paul")
b2.deposit(2000)
b2.withdraw(1000)
b2.display()
