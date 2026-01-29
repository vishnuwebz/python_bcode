"""
if __name__ == __main__: (this script can be imported OR run standalone)
                        Functions and classes in this module can be reused without the main block of code
"""


def main():
    print("Program started")

if __name__ == "__main__":
    main()

"""
inside my_file.py:

print(__name__)

Output:
__main__

(python says: You are the main program.)

case2: import the file

import the file

print(__name__)

output: 
my_file

python says: ou are NOT the main program, you are a helper
"""