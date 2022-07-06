class BankAccount:
    
    all_accounts = []
    
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds. A $5 overdraft fee has been charged to your account.")
            self.balance -= 5.00
        
        return self

    def display_account_info(self):
        # your code here
        print("Account Interest Rate:", self.int_rate)
        print("Balance:", self.balance)

        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Insufficient balance. Interest could not be applied.")
        
        return self
    
    # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            print(account) # currently only prints the location in memory and not the name of the instance itself. need to debug this still.


account1 = BankAccount(0.1, 500)
account2 = BankAccount()

account1.deposit(200).deposit(300).withdraw(250).yield_interest().display_account_info()
account2.deposit(100).deposit(150).withdraw(50).withdraw(100).withdraw(50).withdraw(100).yield_interest().display_account_info()

BankAccount.all_instances()