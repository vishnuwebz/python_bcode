# inheritance = Allows a class to inherit attributes and methods from another class.
# Helps with code reusability and extensibility
# class Child(Parent)  aka : sub(super)

# blueprint/class

class Animal:
    # constructor with attributes
    def __init__(self, name, is_alive):
        self.name = name # instance variable
        self.is_alive = True

    # methods

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

# inheritance from parent to child
class Dog(Animal):

    def speak(self):
        print("WOOF!")

class Cat(Animal): # inherit from parent(Animal)
    def speak(self):
        print("meow!")

class Mouse(Animal):
    def speak(self):
        print("squeek!")

# object
dog = Dog("Scooby",True)
cat = Cat("Garfield", True)
mouse = Mouse("Rattatolie",True)

print(dog.name)
print(dog.is_alive)
print(cat.name)
print(cat.is_alive)

dog.eat()
cat.sleep()


dog.speak()
#
# print(dog.is_alive)
# print(cat.is_alive)
# print(mouse.is_alive)

