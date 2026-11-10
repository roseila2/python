#BSCIT-01-0031/2026
# Create BankAccount class
class BankAccount:

    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited: KSh", amount)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn: KSh", amount)
        else:
            print("Insufficient balance!")

    # Method to display account details
    def displayAccount(self):
        print("\n--- Bank Account Details ---")
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Current Balance: KSh", self.balance)


# Main section
account1 = BankAccount("BSCITs01", "Rose Maina", 10000)

account1.deposit(5000)

account1.withdraw(2000)

account1.displayAccount()
