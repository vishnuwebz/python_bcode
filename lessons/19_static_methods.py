"""
Static methods : A method that belong to a class rather than any object from that class (instance)

Usually used for general utility functions

Instance methods = Best for operations on instance of the class (objects)

Static methods = Best for utility functions that do not need access to class data

"""



class Employee:

    # object from class
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # instance method
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


# objects
employee1 = Employee("Rohit", "Cook")
employee2 = Employee("Janitor", "Cook")

# calling through instance method
print(employee1.get_info())
print(employee2.get_info())

# calling through the static method
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Rocket"))
print(Employee.is_valid_position("Janitor"))
