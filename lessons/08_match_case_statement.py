# old style
status = 400

if status == 200:
    print("OK")
elif status == 400:
    print("Bad Request")
elif status == 401:
    print("Unauthorized")
elif status == 402:
    print("Unauthorized")
elif status == 403:
    print("Forbidden")
elif status == 404:
    print("Not Found")
elif status == 405:
    print("Method Not Allowed")
elif status == 406:
    print("Not Acceptable")
elif status == 407:
    print("Proxy Authentication Required")
elif status == 408:
    print("Proxy Authentication Required")
elif status == 409:
    print("Conflict")
elif status == 410:
    print("Gone")
elif status == 411:
    print("Length Mismatch")

# new

match status:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case _:
        print("Unknow Status")

grade = "B"

match grade:
    case "A" | "B":
        print("Good Job")
    case "C":
        print("Average")
    case _:
        print("Needs improvement")


point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case(0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case _:
        print("Somewhere else")

data = [1, 2, 3]

match data:
    case [a, b, c]:
        print(a, b, c)
    case _:
        print("Not a 3-item list")


age = 20

match age:
    case x if x < 18:
        print("Minor")
    case x if x > 18:
        print("Adult")


"""
Match-Case statement (switch): An alternative to using many 'elif' statements Execute some code if  a value matches a 'case' 
Benefits: cleaner and syntax is more readable
"""

def day_of_week(day):
    match day:
        case 1:
            return "It is Monday"
        case 2:
            return "It is Tuesday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is Saturday"
        case 7:
            return "It is Sunday"
        case _:
            return "Not a valid day"

print(day_of_week(3))
