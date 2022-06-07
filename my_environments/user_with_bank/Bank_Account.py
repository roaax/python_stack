
class BankAccount:
    def __init__(self,name, int_rate=0.01, balance=0): 
        #         don't forget to add some default values for these parameters!
        # 		your code here! (remember, this is where we specify the attributes for our class)
        self.name=name
        self.rate=int_rate
        self.account_balance=balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount, name):
		# your code here (increases the account balance by the given amount)
        self.account_balance += amount
        return self

    def withdraw(self, amount,name):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $" ,self.account_balance)
        return self

    def yield_interest(self):
        self.account_balance *= (1+self.rate)
        return self

