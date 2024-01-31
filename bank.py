from decimal import Decimal

class Account:
    def __init__(
            self,
            account_number,
            account_type, 
            balance,
            account_holder):
        
        self.account_number = account_number
        self.account_type = account_type
        self.balance = Decimal(str(balance))
        self.account_holder = account_holder

    def deposit(self, amount):
        
        self.balance += Decimal(str(amount))
        print(f"Deposited {amount} ")
        return
    
    def withdraw(self, amount):
        if amount <= self.balance and self.balance > 0:
            self.balance -= Decimal(str(amount))
        else: 
            raise ValueError("Insufficient balance to withdraw")
        print(f"Withdrawn {amount} ")
        return 
    def get_balance(self):
        return {
            "Your Balance: " : f"{self.balance}"
        }
    def get_account_number(self):
        return {
            "Account Number" : f"{self.account_number}"
        }
    
    def get_account_type (self):
        return {
            "Message" : f"Your Account type is {self.account_type}"
        }
    def get_account_details(self):
        return {
            "Message" : f"Name of the account is: {self.account_holder},Account number is: {self.account_number} and your, Balance is :  {self.balance} " 
        }
    
class SavingsAccount(Account):
   
    def __init__(self, 
                 account_number, 
                 balance, 
                 account_holder,
                 limit):
        super().__init__(
            account_number = account_number,
            account_type = "Savings Account", 
            balance = balance,
            account_holder = account_holder
             )
        #Encourage using keyword arguments
        self.limit = limit

    def __str__(self) -> str: #represents the class
        return f"Account : {self.account_number}\n holder : {self.account_holder}\n balance : {self.balance}"
    
    def get_account_limit(self):
        if self.limit <= 500000:
            return(f"{self.account_holder} You are using a student Account and your Account limit is 500000!!")
        else:
            return(f"Reach out to your Account manager at our local office to you to upgrade your daily limit to 5m")
        

class CurrentAccount(Account):
    def __init__(self, account_number, balance, account_holder):
        super().__init__(account_number = account_number,
                          account_type = "Current Account", 
                          balance = balance,
                         account_holder = account_holder)

    def get_account_details(self):
        return {
            "Account Holder" : self.account_holder,
            "Account Number": self.account_number,
            "Balance" : self.balance,
            "Extra" : "We wish you a succesful Business week!!"
        }

 
account1 = Account(
    account_number='00000',
    account_type='savings',
    balance=0.00,
    account_holder="Saver"
)
account2 = SavingsAccount(
    account_number='00000',
    balance=0.00,
    account_holder="Savings Saver",
    limit=1000000
)

account3 = CurrentAccount(
    account_number='00000',
    balance=0.00,
    account_holder="Current Saver"
)


# Event driven Achitecture (QUEING REQUEST)
# OOP is encapsulating behaviors
# Absstract class is use in design patterns

print (account2)

# print(account2.get_account_details())
# print(account2.get_account_limit())
# print(account1.get_balance())
# account1.deposit(50)
# print(account1.get_balance())
# account1.withdraw(30.453)
# print(account1.get_balance())
# account1.withdraw(30.0)







# Mike= SavingsAccount(402434542, "Savings", 0.00, " Mike Adereti", account_holder=" ")
# print (SavingsAccount) # Returns an obeject memory space without the str dunder method
# Mike.deposit(50.34)
# Mike.withdraw(30.4)
# print (Mike.get_balance())
# Mike.withdraw(30)
# print(Mike.get_balance())




#Money should be proccessed with Decimal not float
# Floats are unstable

