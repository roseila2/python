#BSCIT-01-0031/2026
# Parent class
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Child class
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculateInterest(self):
        interest = self.balance * self.interest_rate / 100
        return interest


# Main section
account1 = SavingsAccount("ACC1001", 50000, 5)

account1.displayAccount()

print("Interest Rate:", account1.interest_rate, "%")
print("Calculated Interest:", account1.calculateInterest())
