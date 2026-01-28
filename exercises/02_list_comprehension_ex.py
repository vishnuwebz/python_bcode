triples = [x * 3 for x in range(1, 11)]
print(triples)

fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

first_letters = [fruit[0].lower() for fruit in fruits]
print(first_letters)

grades = [85, 42, 90, 90, 80]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
