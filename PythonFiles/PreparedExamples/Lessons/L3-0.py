class Account:
    def __init__(self, accountNumber, initialAmount):
        self.accountNumber = accountNumber
        self.balance = initialAmount 
        self.inDebt = False
    
    def debtupdate(self):
        """ Updates debt status """
        if self.balance < 0:
            self.inDebt = True
        else:
            self.inDebt = False

    def withdraw(self, amount):
        """ withdraws amount from account """
        self.balance -= amount
        self.debtupdate()
    
    def deposit(self, amount):
        """ deposits amount into account """
        self.balance += amount
        self.debtupdate()
 

# Now we can make accounts like this:
DwightsAccount = Account(12345, 100) # makes a new account with number 12345 and balance $100.

print("Dwight has ${} in his account".format(DwightsAccount.balance))
print("Dwight's debt status is {}".format(DwightsAccount.inDebt))

DwightsAccount.deposit(100)

print("We have added $100 to Dwight's account. His balance is now ${}".format(DwightsAccount.balance))

DwightsAccount.withdraw(1000)

print("Dwight spent $1000 on renewing his crane operating license. His balance is now ${}".format(DwightsAccount.balance))
print("Dwight's debt status is now {}".format(DwightsAccount.inDebt))


