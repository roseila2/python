#BSCIT-01-0031/2026
#employee salary calculation program
employee_name = input("enter employee name: ")
basic_salary = input("enter basic salary: ")
monthly_deduction = input("Enter monthly deduction:")

basic_salary = float(basic_salary)
monthly_deduction = float(monthly_deduction)

housing_allowance = 0.10 * basic_salary

gross_salary = basic_salary = housing_allowance

net_salary = gross_salary - monthly_deduction

print("\n---- salary details ----")
print(f"employee name : {employee_name}")
print(f"basic salary : {basic_salary:.2f}")
print(f"house allowance : {housing_allowance:.2f}")
print(f"gross salary : {gross_salary:.2f}")
print(f"deduction : {monthly_deduction:.2f}")
print(f"net salary : {net_salary:.2f}")
