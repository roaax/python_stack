
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        #         don't forget to add some default values for these parameters!
        # 		your code here! (remember, this is where we specify the attributes for our class)
        self.rate=int_rate
        self.account_balance=balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
		# your code here (increases the account balance by the given amount)
        self.account_balance += amount
        return self
    def withdraw(self, amount):
		# your code here
        if self.account_balance - amount > 0:
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    def display_account_info(self):
		# your code here
        print("Balance: $" ,self.account_balance)
        return self
    def yield_interest(self):
        # your code here
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.rate)
        else:
            print("The balance of your bank account is negative!")
        return self
Roaa= BankAccount()
Fidaa = BankAccount()
print(" ROAA --- BankAcount Information:")
Roaa.deposit(400).deposit(300).deposit(100).withdraw(240).yield_interest().display_account_info()
# print("")
print(" FIDAA -- BankAcount Information:")
Fidaa.deposit(150).deposit(500).withdraw(120).withdraw(100).withdraw(50).withdraw(10).yield_interest().display_account_info()
