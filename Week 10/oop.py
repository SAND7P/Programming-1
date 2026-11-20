class BankingOperation:
    def __init__(self,ID,name,balance):
        self.ID = ID
        self.name = name
        self.balance = balance

    def open_account(self):
        print("Account opened as: ",self.name)

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit successful")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdraw Successfull New balance is: ",self.balance)
        else:
            print("Insufficient funds")

Client1=BankingOperation(20400,"Sandip",5000)
Client2=BankingOperation(6666,"Abdullah",5000)
Client1.withdraw(100)
Client2.open_account()