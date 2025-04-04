import os

file_path = "output.txt"

if os.path.exists(file_path):
    file1 = open(file_path, "r+")
    writing_file = file1.write(input("Enter text to write in the file: "))
    print("Data sucessfully added to the file")
    file1.close()
else:
    print(f"File doesn't exists, so creating {file_path} file")
    with open(file_path, "w") as f:
        f.write(input("Enter text to write in the file: "))
        print("Data sucessfully added to the file")

file1 = open(file_path, "a")
appending_file = file1.write(input("Enter additional data to the file: "))
file1.close()

file1 = open(file_path, "r+")
reading_file = file1.read()
print(reading_file)
file1.close()