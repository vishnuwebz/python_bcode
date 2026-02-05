"""
@property = Decorator used to define a method as a property (it can be accessed like an attribute)
Benefit:  Add additional logic when read, write, or delete attributes

Gives you getter, setter and deleter methods

"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        # Delete the private attribute, not the property
        if hasattr(self, '_width'):
            del self._width
            print("Width has been deleted")
        else:
            print("Width doesn't exist")

    @height.deleter
    def height(self):
        # Delete the private attribute, not the property
        if hasattr(self, '_height'):
            del self._height
            print("Height has been deleted")
        else:
            print("Height doesn't exist")

# Test the corrected code
rectangle = Rectangle(3, 4)

# Access properties
print(f"Initial width: {rectangle.width}")  # 3.0cm
print(f"Initial height: {rectangle.height}")  # 4.0cm

# Set new values
rectangle.width = 7
rectangle.height = 9
print(f"After setter - width: {rectangle.width}")  # 7.0cm
print(f"After setter - height: {rectangle.height}")  # 9.0cm

# Delete properties
del rectangle.width
del rectangle.height

# Try to access deleted properties
try:
    print(rectangle.width)
except AttributeError as e:
    print(f"Cannot access width: {e}")

try:
    print(rectangle.height)
except AttributeError as e:
    print(f"Cannot access height: {e}")