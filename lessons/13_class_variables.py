# clas variables = Shared among all instances of a class ,
# defined outside the constructor
# Allow you to share data among all objects created from that class

class Student:

    class_year = 2024 # class variable
    num_students = 0

    def __init__(self, name, age):
        self.name = name # instance variable
        self.age = age
        Student.num_students += 1

# object = Constructor
student1 = Student("Vishnu", 28)
student2 = Student("Webz", 27)
student_3 = Student("John", 30)
student_4 = Student("Rafael", 31)

print(student1.name)
print(student1.age)
print(Student.class_year)


print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name)

