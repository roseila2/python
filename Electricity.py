def calculate_bill(units_consumed, cost_per_unit):
    bill = units_consumed * cost_per_unit
    return bill

# v. Prompt the user for input
units = float(input("Enter units consumed: "))
rate = float(input("Enter cost per unit: "))

# vi. Call the function with user inputs
total_bill = calculate_bill(units, rate)

# vii. Display the calculated electricity bill formatted to 2 decimal places
print(f"\nTotal Electricity Bill: ${total_bill:.2f}")
