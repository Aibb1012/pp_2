# bank_account
class Bank_account():
    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Name of account owner: {self.owner}| Current Balance: {self.balance}"
    
    def deposit(self , number):
        self.balance +=number
        return "Deposit has done."        

    def withdraw(self , numberw):
        if(numberw <= self.balance):
            self.balance -= numberw
            return "Withdrawal from the account has been processed"
        else:
            return "There is not enough money in the balance"
        
account = Bank_account("Andrew ", 10000)

print(account)
print(account.deposit(100))
print(account)
print(account.withdraw(1110))
