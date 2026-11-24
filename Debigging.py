#Debugging the Decision Engine:
#Debigging:
# Debugging means finding and fixing errors (bugs) in a program.
# Three common types of bugs
# - Syntax error: The code breaks Python's grammar rules.
# - Runtime error: An error occurs while the program is running.
# - Logical error: The program runs, but produces the wrong answer.(in notes)

#Debugging with a breakpoint concept:
# A breakpoint is a point where execution pauses so you can inspect variable values. Python's built-in breakpoint() function can help with this.

# What it does
# • Pauses execution: When Python hits breakpoint() in your code, it stops right there and opens a (Pdb) prompt in your terminal.
# • Inspects and modifies: While paused, you can check variable values, evaluate expressions, or step through your code line by line.
# • Replaces older syntax: It acts as a cleaner, built-in shortcut for the older import pdb; pdb.set_trace().
#Debugging with pdb — Python's debugger:

import pdb
a = 10
b = 5
pdb.set_trace()
result = a + b
print(result)

# Command	Meaning
# n	Execute the next line
# s	Step into a function call
# c	Continue execution
# p a	Print the value of a
# q	Quit the debugger

#Debugging with assert:

# Python's assert statement checks whether a condition is true. If it is false, Python raises an AssertionError.
def square(n):
    return n * n

assert square(3) == 9
assert square(4) == 20

print("Success")#output:assertion error 
#workflow:
# Step 1: square(3) returns 9. The first assertion passes.
# Step 2: square(4) returns 16, but the code checks whether it equals 20.
# assert 16 == 20
# This condition is false, so Python raises an AssertionError.
# Step 3: print("Success") never executes because the assertion stops normal execution.


#Debugging with logging:
#we will discuss later


#Debugging with type() and isinstance():
age = input("Enter your age: ")

print(type(age))#output:<class 'str'>

#isinstance() is uses to check a value's type
age = 21
print(isinstance(age, int))#output:True
