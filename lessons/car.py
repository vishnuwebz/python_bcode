class Car:
    # function
    def __init__(self, model, year, color, for_sale): # functions with parameters
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

# methods
    def drive(self): # method
        print(f"You drive the {self.model} car!")


    def stop(self):
        print(f"You stop the {self.model} car!")


    def describe(self):
        print(f"The {self.model} car is {self.year} years old")