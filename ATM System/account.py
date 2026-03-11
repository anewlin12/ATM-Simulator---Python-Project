#This script holds the Account class is imported into the account_data script for handling the CSV data.
#This script holds the logic for the Check Balance, Deposit, and Withdraw methods.
class Account:
    def __init__(self, account, pin, name, balance):
        self.account = account
        self.pin = pin
        self.name = name
        self.balance = balance
        
#This method returns the balance for the current user.
    def check_balance(self):
        print(f"TEST Your balance is {self.balance:.2f}")
        return self.balance
    
#This method checks to see if the amount the user entered is greater than 0.01.
#If True, the amount is added to the user's balance saved in the data.csv file.
#If False the method returns false.
    def deposit(self, amount):
        if amount < 0.01:
            print(f"TEST Please enter an amount greater than .01")
            return False
        print(f"TEST You have deposited {amount}, Your new balance is: {(self.balance + amount):.2f}")
        self.balance += amount
        return True

#This method checks to see if the amount the user entered is greater than 0.01.
#If True, the amount is subtracted from the user's balance saved in the data.csv file.
#If False the method returns False.
#It also checks if the amount entered is greater than the available balance. If True, it will return false.
    def withdraw(self, amount):
        if amount < 0.01:
            print(f"TEST Please enter an amount greater than .01")
            return False
        if amount > self.balance:
            print(f"TEST You do not have enough funds for this withdrawal")
            return False
        print(f"TEST You have withdrawn {amount}, your new balance is {(self.balance - amount):.2f}")
        self.balance -= amount
        
        return True


        
