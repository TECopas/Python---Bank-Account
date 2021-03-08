class User:# declare a class and give it name User
    def __init__(self, first_name, email):# dunder init function
        self.name = first_name#code copied from cdj site needs to be indented, black space will produce anerror
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def transferMoney(self, amount, otheruser):
        self.account_balance -= amount
        otheruser.account_balance += amount
        return self
    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.account_balance}")
        return self
class BankAccount:
    def __init__(self, int_rate=.01, account_balance=0): # don't forget to add some default values for these parameters!
        self.int_rate = int_rate
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f"Account Balance: {self.account_balance}")
        return self
    def yield_interest(self):
        self.account_balance = (self.account_balance)*(1+self.int_rate)
        return self
michael = User('Michael','mike@cdj.com')#items have to be strings for it to work.
anna = User('Anna',"anna@cdj.com")
guido = User('Guido', 'guido@cdj.com')
monty = User('Monty', 'monty@cdj.com')
guido.make_deposit(100).make_deposit(175).make_deposit(125).make_withdrawal(100).display_user_balance()
michael.make_deposit(42).make_deposit(99).make_withdrawal(77).make_withdrawal(21).display_user_balance()
anna.make_deposit(40000).make_withdrawal(1111).make_withdrawal(2222).make_withdrawal(3333).display_user_balance()
guido.transferMoney(50,anna)
anna.display_user_balance()
guido.display_user_balance()
A123 = BankAccount()
B123 = BankAccount(.10)
A123.display_account_info().deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()
B123.display_account_info().deposit(5000).deposit(9000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()
