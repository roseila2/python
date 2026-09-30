def calculate_grade(mark):
    if mark >= 70 and mark <= 100:
        return "A"
    elif mark >= 60 and mark < 70:
        return "B"
    elif mark >= 50 and mark < 60:
        return "C"
    elif mark >= 40 and mark < 50:
        return "D"
    elif mark >= 0 and mark < 40:
        return "F"
    else:
        return "Invalid Mark (Must be between 0 and 100)"

# v. Prompt the user to enter the student's mark
student_mark = float(input("Enter student's mark (0-100): "))

# vi. Call the calculate_grade function and display the returned grade
grade = calculate_grade(student_mark)
print(f"Grade: {grade}")
