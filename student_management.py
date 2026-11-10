#BSCIT-01-0031/2026
# Create Student class
class Student:

    # Method to assign student details
    def setStudentDetails(self, name, reg_number, course, mark):
        self.name = name
        self.reg_number = reg_number
        self.course = course
        self.mark = mark

    # Method to calculate grade
    def calculateGrade(self):

        if self.mark >= 70 and self.mark <= 100:
            self.grade = "A"

        elif self.mark >= 60:
            self.grade = "B"

        elif self.mark >= 50:
            self.grade = "C"

        elif self.mark >= 40:
            self.grade = "D"

        else:
            self.grade = "F"

    # Method to display student details
    def displayStudentDetails(self):
        print("\n--- Student Details ---")
        print("Student Name:", self.name)
        print("Registration Number:", self.reg_number)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("Grade:", self.grade)


# Main section
student1 = Student()

student1.setStudentDetails(
    "Mary Wanjiku",
    "BIT/001/2026",
    "Information Technology",
    75
)

student1.calculateGrade()

student1.displayStudentDetails()
