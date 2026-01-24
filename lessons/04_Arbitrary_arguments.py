def order(food, *extras, **details):
    print(f"Food: {food}") # positional argument: order:- must be in the first
    print("Extras:", extras) # *args = arbitrary positional arguments , order matters as it follows by positional argument
    print("Details:", details) # **kwargs= arbitrary keyword arguments, rule = followed by *args

order(
    "Pizza",
    "Extra Cheese",
    "Olives",
    size="Large",
    drink="Coke"
)

"""
food → positional parameter

extras → tuple of extra positional args

details → dictionary of keyword args
"""

"""
Python enforces this strict order:

def func(
    positional,
    default=10,
    *args,
    keyword_only=None,
    **kwargs
):
    pass



| Order | Type         |
| ----- | ------------ |
| 1️⃣    | Positional   |
| 2️⃣    | Default      |
| 3️⃣    | `*args`      |
| 4️⃣    | Keyword-only |
| 5️⃣    | `**kwargs`   |

"""

"""
*args = allows you to pass multiple positional(non-key) arguments
**kwargs = allows you to pass multiple keyword arguments

* unpacking operator
1. positional 2. default 3.keyword 4.ARBITRARY
"""

# def add(a, b):
#     return a + b


# print(add(1, 2 , 3)) # TypeError: add() takes 2 positional arguments but 3 were given
print()
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5, 6))
print()
# arbitrary positional argument

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Mr", "Vishnu", "Webz")

print() # space

# **kwargs

def print_address(**kwargs):
    # print(type(kwargs)) # <class 'dict'>
    for value in kwargs.values():
        print(value, end=", ") # 123 fake st., Coimbatore, TamilNadu, 555-1234, None
    print()
    for key in kwargs.keys():
        print(key, end=" ") # street city state zip_code None
    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(print_address(street="123 fake st.",
                    apt = 206,
                    city="Coimbatore",
                    state="TamilNadu",
                    zip_code="555-1234"
                    ))



