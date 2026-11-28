#BSCIT-01-0031/2026
#Student marks using a list
marks = []
print("Enter marks for five subjects:")
for i in range(5):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)

print("\nAll marks:", marks)

total = sum(marks)
print("total marks:", total)

average = total / len(marks)
print("average mark:", average)

highest = max(marks)
print("highest mark:", highest)

lowest = min(marks)
print("lowest mark:", lowest)

marks[2] = float(input("\n Enter the new mark for the third subject: "))
print("updated marks list:", marks)
