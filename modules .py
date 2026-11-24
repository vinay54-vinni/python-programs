#modules   @single line comments 
"""A module is simply a Python file (.py) containing code such as functions, variables, or classes 
that we can reuse in another Python program"""#@multi line comments
import math#math module is imports for using mathematical operations
print(math.sqrt(25))
# if we want to import sepcific function 
#example
from math import sqrt#here we are importing sqrt function from math module. At a time we can also imports many functions
print(sqrt(49))
# Module aliases
import math as m#here m is aliases instead of using math we use m as short cut form

print(m.sqrt(36))


#package : package is nothing but collecctions of modules
# calculations/
# ├── __init__.py
# ├── addition.py
# └── subtraction.py

# - 📁 calculations/ → Package
# - 📄 addition.py → Module
# - 📄 subtraction.py → Module
# - 📄 __init__.py → helps define/initialize the package (especially in traditional package layouts)
# from calculations.addition import add @ if we want to call a module from package we write like this
