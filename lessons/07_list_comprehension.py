"""
list comprehension = a concise way to create lists in python. Compact and easier to read than traditional loops
[expression for value in iterable if condition]
"""
# Only expression and for are mandatory.

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

demo = [x * 2 for x in range(1, 11)]

print(demo)

numbers = [1, 2, 3, 4, 5, 6]

squares = [s * s for s in numbers]

print(squares)


even = [e for e in numbers if e % 2 == 0]

print(even)

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]

print(labels)

demo_2 = [c if c % 2 == 0 else 0 for c in numbers]
print(demo_2)

# list comprehension with strings

word = "hello"

letters = [char.upper() for char in word]
print(letters)

# nested list comprehension

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [num for row in matrix for num in row]

print(flat)