#BSCIT-01-0031/2026
# Parent class
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def displayEmployee(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)


# Child class
class Lecturer(Employee):
    def __init__(self, name, employee_id, subject):
        super().__init__(name, employee_id)
        self.subject = subject

    def displayLecturer(self):
        self.displayEmployee()
        print("Teaching Subject:", self.subject)


# Main section
lecturer1 = Lecturer("Rose Maina", "EMP101", "Computer Science")

lecturer1.displayLecturer()
