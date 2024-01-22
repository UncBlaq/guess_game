class Account:
    def __init__(self, account_number, account_type,  balance, account_holder):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        return
    
    def withdraw(self, amount):
        self.balance -= amount
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
    def __init__(self, account_number, account_type, balance, account_holder,limit):
        super().__init__(account_number, account_type, balance, account_holder)
        self.limit = limit
    def get_account_limit(self):
        if self.limit <= 500000:
            return(f"{self.account_holder} You are using a student Account and your Account limit is 500000!!")
        else:
            return(f"Reach out to your Account manager at our local office to you to upgrade your daily limit to 5m")
        

class CurrentAccount(Account):
    def get_account_details(self):
        return {
            "Account Holder" : self.account_holder,
            "Account Number": self.account_number,
            "Balance" : self.balance,
            "Extra" : "We wish you a succesful week!!"
        }
    

Mike= CurrentAccount(402434542,"Savings", 200000, " Mike Adereti")
Mike.deposit(200000)
print(Mike.get_account_details())
