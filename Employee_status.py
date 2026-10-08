# BSCIT-01-0031/2026 MAINA ROSE WANGARI

# Assign initial values
emp_name = "rose maina"
emp_age = 24
emp_salary = 50000
is_active = True

# Display information using f-string
print(f"Employee Name: {emp_name}")
print(f"Age: {emp_age}")
print(f"Salary: ${emp_salary:.2f}")
print(f"Active Status: {is_active}")

# Demonstrate explicit str() conversion and string concatenation
age_str = str(emp_age)
concatenated_info = "Employee Age String: " + age_str
print(concatenated_info)
