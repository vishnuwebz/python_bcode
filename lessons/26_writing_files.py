# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"

file_path = "output.txt"

try:
    with open(file=file_path, mode="a") as file:
        file.write(txt_data)
        print(f"text file {file_path}")
except FileExistsError:
    print(f"text file {file_path} already exists")

#############################################################
print("#####LIST#####")
print()
employees = ["adam", "john", "trump"]

file_path = "employees.txt"

try:
    with open(file=file_path, mode="w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"employees txt file {file_path} was created")
except FileExistsError:
    print(f"employees file {file_path} already exists")

###############################################################
print()
print("#####JSON#####")
print()

import json

employee = {
    "name": "Spongebob",
    "age": 20,
    "jon": "cook"
}

file_path = "employees.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"employees json file {file_path} was created")
except FileExistsError:
    print(f"employees json file {file_path} already exists")


###############################################################

print()
print("#####CSV#####")
print()

import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "employees.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print(f"csv file {file_path} already exists")