class BankAccount:
    def __init__(self,initiale_balance = 0):
        self.account_balance = initiale_balance

    def deposit(self,amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True
    
    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

