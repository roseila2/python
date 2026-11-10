#BSCIT-01-0031/2026
# Create an employees dictionary
employees = {
    "John": 30000,
    "Mary": 35000,
    "Peter": 40000,
    "Jane": 32000,
    "David": 45000
}

# Display all employee names and salaries
print("Employee Salary Records:")

for name, salary in employees.items():
    print(name, ":", "KSh", salary)

# Update the salary of one employee
employees["John"] = 35000

# Add a new employee and salary
employees["Grace"] = 38000

# Calculate total salary payable
total_salary = sum(employees.values())

# Display updated employee records
print("\nUpdated Employee Records:")

for name, salary in employees.items():
    print(name, ":", "KSh", salary)

# Display total salary
print("\nTotal Salary Payable: KSh", total_salary)
