class BankAccount:
    
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds. A $5 overdraft fee has been charged to your account.")
            self.balance -= 5.00
        
        return self

    def display_account_info(self):
        print("Account Interest Rate:", self.int_rate)
        print("Balance:", self.balance)

        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Insufficient balance. Interest could not be applied.")
        
        return self


class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

        return self

user1 = User("Zoro", "bestswordsman@gmail.com")
user1.make_deposit(100)

user1.account.display_account_info()
