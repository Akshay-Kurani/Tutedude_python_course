students = {"Akshay":99 ,"Rajveer": 58,"Prem": 75,"Roshan": 47, "Manu":90}

name = (input("Enter a student's name: "))

if name in students:
    print(f"{name}'s marks are {students[name]}")
else:
    print("Student name not found")