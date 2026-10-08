#BSCIT-01-0031/2026 MAINA ROSE WANGARI
# Accept inputs from user
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
age_input = input("Enter employee age: ")
salary_input = input("Enter basic salary: ")

# Convert types
age = int(age_input)
basic_salary = float(salary_input)

# Calculate annual salary
annual_salary = basic_salary * 12

# Display employee details
print(f"\n--- Employee Information ---")
print(f"Name: {name}")
print(f"Employee ID: {emp_id}")
print(f"Age: {age}")
print(f"Basic Salary: ${basic_salary:.2f}")
print(f"Annual Salary: ${annual_salary:.2f}")
