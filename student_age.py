#BSCIT-01-0031/2026
try:
    age = int(input("Enter your age:"))
    print("Age successfully recorded")
except ValueError:
    print("Invalid age entered")
