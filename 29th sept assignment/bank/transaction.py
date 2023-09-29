# bank/transaction.py

def deposit(account, amount):
    return account.deposit(amount)

def withdraw(account, amount):
    return account.withdraw(amount)

def check_balance(account):
    return account.get_balance()
