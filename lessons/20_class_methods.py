"""
Class methods = Allow operations related to the class itself

Take (cls) as the first parameter, which represents the class itself.

Instance methods = Best for operations on instances of the class (objects)

Static methods = Best for utility functions that do not need access to class data

Class methods = Best for class-level data or require access to the class itself
"""

class Student:

    # class variables
    count = 0
    total_gpa = 0

    # constructor (blue print)
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # clss method
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {(cls.total_gpa / cls.count):.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 4.2)
student3 = Student("Patan", 5.0)


print(Student.get_count())

print(student1.get_info())

print(Student.get_average_gpa())