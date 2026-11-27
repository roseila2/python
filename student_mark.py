#BSCIT-01-0031/2026
#student final mark calculation program
student_name = input("enter student name:")
coursework_mark = input("enter coursework mark (out of 30):")
examination_mark = input("enter examination mark (out of 70):")

coursework_mark = float(coursework_mark)
examination_mark = float(examination_mark)

total_mark = coursework_mark + examination_mark

has_passed = total_mark >=40

print("\n----- student results -----")
print(f"student name : {student_name}")
print(f"coursework mark : {coursework_mark}")
print(f"examination mark : {examination_mark}")
print(f"total mark : {total_mark}")
print(f"passed : {has_passed}")
