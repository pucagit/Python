import os
import json
import csv

# file_path = "Python/test.txt"
file_path = "test.txt"

if os.path.exists(file_path):
    print("File exists")

    if os.path.isfile(file_path):
        print(f"{file_path} is a file")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory")
else:
    print("File does not exist")

# write mode
employee = {
            "name": "Phuc",
            "age": 22,
            "job": "Software Engineer"   
            }
info = [["name", "age", "job"],
       ["Phuc", 22, "Software Engineer"],
       ["John", 30, "Data Scientist"],
       ["Jane", 25, "Web Developer"]]

with open("output.csv", "w") as file:
    writer = csv.writer(file) 
    for row in info:
        writer.writerow(row)

with open("output.json", "w") as file:
    json.dump(employee, file, indent=4)

with open("output.txt", "a") as file:
    file.write("Hello, World!\n")

# read mode
with open("output.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("output.json", "r") as file:
    data = json.load(file)
    print(data)

with open("output.txt", "r") as file:
    content = file.read()
    print(content)