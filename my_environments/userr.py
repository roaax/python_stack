
from Bank_Account import BankAccount

class User:
    def __init__ (self, int_rate=0.01 , balance=0 ):
        self.rate
        self.account
    def make_deposit(self, amount):
        self.deposit()
        print(self.deposit)
    def make_withdrawal(self, amount):
        self.withdraw()
        # return self
    def display_user_balance(self):
        self.display_account_info()
        # print(f" User: {self.name} ------> Your Balance is: ${self.account_balance} ")
        # return self
    # def  transfer_money(self, user, amount):
    #     self.account_balance = self.account_balance - amount
    #     user.account_balance = user.account.balance + amount
    #     print(f" User: {self.name} ------> Transfare Balance is: ${self.account_balance} User: {user.name} ------> Transfare Balance is: ${user.account_balance}  ")
Roaa=BankAccount()
Fidaa = BankAccount()



# Roaa= User("Roaa", )
# Fidaa = User("Fidaa", )
# Ajwan = User("Ajwan" , )

# print("------The First User Roaa :------")
# Roaa.display_user_balance()
# Roaa.make_deposit(3)
# Roaa.make_withdrawal(1)
# Roaa.display_user_balance()

# print("------The Seconed User Fidaa :------")
# Fidaa.display_user_balance()
# Fidaa.make_deposit(2)
# Fidaa.make_withdrawal(2)
# Fidaa.display_user_balance()

# print("------The Third User Ajwan :------")
# Ajwan.display_user_balance()
# Ajwan.make_deposit(1)
# Ajwan.make_withdrawal(3)
# Ajwan.display_user_balance()

# print(Roaa.name , Roaa.account_balance)	
# print(Fidaa.name , Fidaa.account_balance)
# print(Ajwan.name , Ajwan.account_balance)
# Roaa.make_deposit(200)
# Fidaa.make_deposit(50)
# print(Roaa.name , Roaa.make_deposit())	
# print(Fidaa.name , Fidaa.account_balance)
# print(Ajwan.name , Ajwan.account_balance)

# Roaa.transfer_money(Ajwan , 1)