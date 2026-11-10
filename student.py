#BSCIT-01-0031/2026
#create a student dictionary
student = {
    "registration number": "BSCIT-01-0031/2026",
    "student name":"Rose Maina",
    "course":"information technology",
    "year of study": 3
}

#display student name and course
print("student name:", student["student name"])
print("course:", student["course"])

#change the year of study
student["year of study"] = 2

#add an email address
student["email"] = "maina@gmail.com"

#display the updated disctionary
print("\n updated student record:")
print(student)
