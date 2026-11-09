#BSCIT-01-0031/2026
import logging

# Configure logging to save errors in a file
logging.basicConfig(
    filename="bank_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define a custom exception
class InsufficientFundsError(Exception):
    pass


# Banking withdrawal function
def withdraw_money(balance):

    try:
        # Ask the user to enter withdrawal amount
        amount = float(input("Enter amount to withdraw: "))

        # Check if amount is positive
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Check if balance is sufficient
        if amount > balance:
            raise InsufficientFundsError(
                "Insufficient funds in your account."
            )

    except ValueError as e:
        print("Invalid input. Please enter a valid number.")
        logging.error("ValueError occurred: %s", e)

    except InsufficientFundsError as e:
        print(e)
        logging.error("InsufficientFundsError occurred: %s", e)

    else:
        # Executes when no exception occurs
        balance = balance - amount
        print("Withdrawal successful!")
        print("Amount withdrawn:", amount)
        print("Remaining balance:", balance)

    finally:
        # Executes whether an exception occurs or not
        print("Thank you for using our banking application.")
        print("Goodbye!")


# Main program
account_balance = 10000

print("WELCOME TO THE BANKING APPLICATION")
print("Account Balance:", account_balance)

withdraw_money(account_balance)
