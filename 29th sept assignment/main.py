from bank.account import SavingsAccount, CheckingAccount
from bank.transaction import deposit, withdraw, check_balance

# Example usage
savings_account = SavingsAccount("SA123", "Alice", 1000, 2.5)
checking_account = CheckingAccount("CA456", "Bob", 500, 100)

print(deposit(savings_account, 500))
print(withdraw(checking_account, 200))
print(check_balance(savings_account))
print(check_balance(checking_account))