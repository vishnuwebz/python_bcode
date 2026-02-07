# Python reading files (.txt, .json, .csv)
print("################ TXT ##############")

file_path = "output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"file '{file_path}' not found")
except PermissionError:
    print(f"file '{file_path}' is read-only")


print("################ JSON ##############")

import json

file_path = "employees.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print(f"file '{file_path}' not found")
except PermissionError:
    print(f"file '{file_path}' is read-only")


print("################ CSV ##############")


import csv

file_path = "employees.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)

except FileNotFoundError:
    print(f"file '{file_path}' not found")
except PermissionError:
    print(f"file '{file_path}' is read-only")

