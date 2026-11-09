#BSCIT-01-0031/2026
try:
    file = open("employees.txt","r")
    contents = file.read()
    print(contents)
    file.close()
except FileError:
    print("The employee file was found.")
finally:
    print("file processing comleted.")
