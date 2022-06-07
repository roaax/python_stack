from os import access
from user import User
from Bank_Account import BankAccount

Roaa= User( "Roaa")
Fidaa = User(" Fidaa")

cheack = BankAccount("Checking", 0.01)
save = BankAccount("Saving", 0.004)


print(" ROAA --- BankAcount Information:")
Roaa.make_deposit(100,cheack).make_deposit(100,cheack).make_deposit(100,cheack).make_withdrawal(100,save ).account.yield_interest()
Roaa.display_user_balance()
# # print("")
print(" Fidaa --- BankAcount Information:")
Fidaa.make_deposit(500,cheack).make_deposit(200,cheack).make_deposit(400,cheack).make_withdrawal(150,save ).account.yield_interest()
Fidaa.display_user_balance()