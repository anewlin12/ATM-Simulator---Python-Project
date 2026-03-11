#This script holds the account data functions used in the atm_gui script used for reading and writing the data to the CSV file.
import csv
from account import Account

#This function is used for appending all of the account information saved in data.csv into the empty account list "accounts".
def load_accounts():
    accounts = []
    with open('data.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            account = Account(
                account=row['ACCOUNT'],
                pin=row['PIN'],
                name=row['NAME'],
                balance=float(row['BALANCE']))
            accounts.append(account)
    return accounts

#this function is used for writing the accounts data back to the CSV file.
def save_accounts(accounts):
    with open('data.csv', 'w', newline='') as file:
        fieldnames = ['ACCOUNT', 'PIN', 'NAME', 'BALANCE']
        writer = csv.DictWriter(file, fieldnames=fieldnames)        
        writer.writeheader()
        for account in accounts:
            writer.writerow({
                'ACCOUNT': account.account,
                'PIN': account.pin,
                'NAME': account.name,
                'BALANCE': account.balance
            })
    return True

#This function is used for finding the account in the list accounts.
#If the input is valid and verified then it will return the accounts information.
def find_account(account_number, pin):
    accounts = load_accounts()
    for account in accounts:
        if account.account == account_number and account.pin == pin:
            return account
    return None


#This function is used for updating the users account balance variable.
def update_account_balance(account_number, new_balance):
    accounts = load_accounts()
    account_found = False
    for account in accounts:
        if account.account == account_number:
            account.balance = new_balance
            account_found = True
            break
    if not account_found:
        return False
    return save_accounts(accounts)