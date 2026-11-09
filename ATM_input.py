#BSCIT-01-0031/2026
try:
    amount = int(input("Enter the withdrawal amount:"))
    print("withdrawal amount:",amount)
except ValueError:
    print("invalid amount. please enter a number.")
