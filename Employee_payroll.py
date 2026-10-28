# BSCIT-01-0031/2026
class Employee:
    # i & ii. Constructor to initialize attributes
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    # iii. Method to calculate and return gross salary
    def calculate_gross_salary(self):
        gross_salary = self.basic_salary + (self.overtime_hours * 500)
        return gross_salary

    # v. Method to calculate and return tax (10% of gross salary)
    def calculate_tax(self):
        gross_salary = self.calculate_gross_salary()
        tax = gross_salary * 0.10
        return tax

    # iv. Method to calculate and return net salary
    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        tax = self.calculate_tax()
        net_salary = gross_salary - tax
        return net_salary


# vi. Create two employee objects and display their details
emp1 = Employee("EMP101", "Alice", 50000, 10)
emp2 = Employee("EMP102", "Brian", 65000, 6)

print("--- Employee 1 Details ---")
print(f"Name: {emp1.name} ({emp1.employee_id})")
print(f"Gross Salary: KSh {emp1.calculate_gross_salary():,.2f}")
print(f"Tax: KSh {emp1.calculate_tax():,.2f}")
print(f"Net Salary: KSh {emp1.calculate_net_salary():,.2f}\n")

print("--- Employee 2 Details ---")
print(f"Name: {emp2.name} ({emp2.employee_id})")
print(f"Gross Salary: KSh {emp2.calculate_gross_salary():,.2f}")
print(f"Tax: KSh {emp2.calculate_tax():,.2f}")
print(f"Net Salary: KSh {emp2.calculate_net_salary():,.2f}")
