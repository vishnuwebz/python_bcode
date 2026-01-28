# membership operator = used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)

"""
in
not in
"""

word = "APPLE"

letter = input("Guess a letter in the secret word: ").lower()

if letter not in word:
    # print(f"These is a {letter}")
    print(f"{letter} was not found")

else:
    # print(f"{letter} was not found")
    print(f"These is a {letter}")

print("SETS")
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")


print("DICTIONARY")
print()

grades = {
    "Sandy" : "A",
    "Squidward": "B",
    "Spongebob": "C",
    "Patrick": "D",
          }

student_dict = input("Enter the name of a student: ")

if student_dict in grades:
    print(f"{student_dict}'s grade is {grades[student_dict]}")
else:
    print(f"{student_dict} is not a student")

"""
Enter the name of a student: Spongebob
Spongebob's grade is C
"""

email = input("Enter your email adress: ")

if "@" in email and '.' in email:
    print(f"{email} is a valid email")
else:
    print(f"{email} is not a valid email")