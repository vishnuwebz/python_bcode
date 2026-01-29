"""
variable  scope = where a variable is visible and accessible

scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
"""

def func1():
    print(x)

def func2():
    print(x)

x = 7

func1()
func2()


