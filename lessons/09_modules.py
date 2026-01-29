import match_utils

print(match_utils.PI)
print(match_utils.add(9, 8))

# You take the whole box, and you must say which toy you want.
"""
Technical explanation
---------------------

Module is loaded once

Stored in sys.modules

Access via module_name.identifier
"""

from lessons.match_utils import add, PI

print(add(9, 7))
print(PI)


# Rename module or items (aliasing)

import match_utils as mu

print(mu.add(9, 7))
print(mu.PI)

"""
🧠 How Python finds modules (IMPORTANT)

When you do:

import my_module


Python searches in this order:

1️⃣ Current folder
2️⃣ Installed packages
3️⃣ Python standard library

This search path is called sys.path.
"""


# module = a file containing code you want to include in your program use 'import' to include a module (*built-in or your own) useful to break up a large program reusable separate files

# print(help("modules"))
#
# print(help("math"))

import math

print(math.pi)

import math as m
print(m.pi)

from math import pi
print(pi )