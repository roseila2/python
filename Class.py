#BSCIT-01-0031/2026
# Base class: Person
class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    def display_details(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived class: Student (inherits from Person)
class Student(Person):
    def __init__(self, person_id, name, age, course, marks):
        super().__init__(person_id, name, age)
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 70:
            return "Grade A"
        elif self.marks >= 60:
            return "Grade B"
        elif self.marks >= 50:
            return "Grade C"
        else:
            return "Grade D"

    def display_details(self):
        super().display_details()
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")


# Derived class: Lecturer (inherits from Person)
class Lecturer(Person):
    def __init__(self, person_id, name, age, department, monthly_salary):
        super().__init__(person_id, name, age)
        self.department = department
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
        print(f"Monthly Salary: {self.monthly_salary}")
        print(f"Annual Salary: {self.calculate_annual_salary()}")


# --- Testing the implementation with sample data ---
if __name__ == "__main__":
    print("--- Student Details ---")
    student1 = Student("S101", "Ann Thing", 20, "Computer Science", 78)
    student1.display_details()

    print("\n--- Lecturer Details ---")
    lecturer1 = Lecturer("L202", "Roo Nice", 45, "Information Technology", 5500.0)
    lecturer1.display_details()
