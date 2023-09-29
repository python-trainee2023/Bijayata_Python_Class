class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposite amount."

    def withdraw(self, amount):
        if 0 <amount <= self.balance:
            self.balance -= amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Account balance for {self.holder_name}: ${self.balance}"

class SavingsAccount(Account):
        def __init__(self, account_number, holder_name, balance, interest_rate):
            super().__init__(account_number, holder_name, balance)
            self.interest_rate = interest_rate

        def apply_interest(self):
            interest_amount = self.balance * (self.interest_rate / 100)
            self.balance += interest_amount
            return f"Interest applied. New balance: ${self.balance}"
class CheckingAccount(Account):
        def __init__(self, account_number, holder_name, balance, overdraft_limit):
            super().__init__(account_number, holder_name, balance)
            self.overdraft_limit = overdraft_limit

        def withdraw(self, amount):
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            else:
                return "Withdrawal exceeds overdraft limit."

