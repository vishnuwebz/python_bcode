# super() = function used in child class to call methods from a parent class (super class).
# Allows you to extend the functionality of the inherited methods.

class Shape:
    # constructor     # attribute
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)

        self.radius = radius

    # method overriding
    def describe(self):
        print(f"It is a circle with an area of {31.4 * self.radius * self.radius} cm^2")
        # accessing the method from parent by calling super() method
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


    # method overriding
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width} cm^2")
        # accessing the method from parent by calling super() method
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


    # method overriding
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2} cm^2")
        # accessing the method from parent by calling super() method
        super().describe()

# objects :
circle = Circle(color="red", is_filled=True,  radius=5)
square = Square(color="green", is_filled=True, width=5)
triangle = Triangle(color="blue", is_filled=True, width=5, height=5)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print(triangle.color)

circle.describe()
square.describe()
triangle.describe()