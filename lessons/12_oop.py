
from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Mercedes", 2026, "premium_black", True)

print("_____________________________________")

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.stop()

print("_____________________________________")

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()

print("_____________________________________")

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
car3.describe()
print("_____________________________________")