import os

file1 = "sample.txt"

if os.path.exists(file1):
    file1 = open("sample.txt", "r+")
    reading_file = file1.read()
    print("This is a sample text file\n",reading_file)
else:
    print("Sample file doesn't exist")