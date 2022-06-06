
# Update your previous assignment so that each instance's methods are chained

class User:
    def __init__ (self, name , balance=0 ):
        self.name = name
        self.account_balance = balance
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f" User: {self.name} ------> Your Balance is: ${self.account_balance} ")
        return self
    # def  transfer_money(self, user, amount):
    #     self.account_balance = self.account_balance - amount
    #     user.account_balance = user.account.balance + amount
    #     print(f" User: {self.name} ------> Transfare Balance is: ${self.account_balance} User: {user.name} ------> Transfare Balance is: ${user.account_balance}  ")

Roaa= User("Roaa", )
Fidaa = User("Fidaa", )
Ajwan = User("Ajwan" , )

print("------The First User Roaa :------")
Roaa.display_user_balance().make_deposit(3).make_withdrawal(1).display_user_balance()

print("------The Seconed User Fidaa :------")
Fidaa.display_user_balance().make_deposit(2).make_withdrawal(2).display_user_balance()

print("------The Third User Ajwan :------")
Ajwan.display_user_balance().make_deposit(1).make_withdrawal(3).display_user_balance()

# print(Roaa.name , Roaa.account_balance)	
# print(Fidaa.name , Fidaa.account_balance)
# print(Ajwan.name , Ajwan.account_balance)
# Roaa.make_deposit(200)
# Fidaa.make_deposit(50)
# print(Roaa.name , Roaa.make_deposit())	
# print(Fidaa.name , Fidaa.account_balance)
# print(Ajwan.name , Ajwan.account_balance)

# Roaa.transfer_money(Ajwan , 1)