# Python Decorators:
# A decorator allows us to add extra functionality to an existing function without changing its original code.
# Imagine you already have a function that prints a welcome message. You want to print a message before it runs, but you don't want to modify its original code.

def first():
    print("Python")

def second(func):
    func()

second(first)#output:Python


# Execution happens like this:
# 1. first is defined, but it is not called yet.
# 2. second(func) is defined to accept a function.
# 3. second(first) passes the first function into second.
# 4. Inside second, func refers to first.
# 5. Therefore, func() executes first() and prints Python.
# Remember this difference:
# - second(first) → passes the function.
# - second(first()) → calls the function immediately and passes its return value.

#EXAMPLE :
def welcome():
    print("Welcome")

def decorator(func):
    def wrapper():
        print("Starting...")
        func()
    return wrapper

result = decorator(welcome)
result()
# #output :
# Starting...
# Welcome

# Understand @decorator syntax:

def decorator(func):#cause of the below info we are also using the func here without parentheses.
    def wrapper():
        print("Starting...")
        func()
    return wrapper # here we got confuse about function calling cause we are not using parentheses() then how we are calling the inside function
# for that when it is possible for us to use functions has like both with parentheses and without it .
#if we use () so inside the function they dosen't have any return statements so after giving output againg we get none.
#if we dosen't use() we are dosen't asking it to give whole we want what it has only so if we use func without() we dosen't get any error
@decorator#here it works as welcome = decorator(welcome)
#we can use whatever name we want to but it same as the main function here this decorator(func) so we used here decorator.
def welcome():
    print("Welcome")

welcome()#output : starting....\n welcome

# That means the original welcome function is passed to decorator, and the returned wrapper replaces the name welcome.
# When we call welcome(), we're now calling the wrapper function.
# Remember this important rule:
# @decorator is shorthand for function_name = decorator(function_name).


def decorator(func):
    def wrapper(*args, **kwargs):#instead of 
        print("Starting...")
        func(*args, **kwargs)
    return wrapper

@decorator
def greet(name):
    print("Hello", name)

greet("Vinay")#we can use arguments also here


# Stacking multiple decorators:
def first(func):
    def wrapper():
        print("First")
        func()
    return wrapper

def second(func):
    def wrapper():
        print("Second")
        func()
    return wrapper

@first
@second
def greet():
    print("Hello")

greet()
# output :
# First
# Second
# Hello

# @first
# @second
# def greet():
#     here it equal to 
# greet = first(second(greet))

# first prints First.
# It calls the function it received, which is the wrapper created by second.
# second prints Second.
# It calls the original greet function.
# The original function prints Hello.

# Decorators that accept arguments:
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")

greet()#output: hello\n hello \n hello

# Real-world use of decorators
# Decorators aren't just for printing messages. They're useful in real Python applications, too.

# Common uses include:
# - Logging: Recording when a function runs.
# - Timing: Measuring how long a function takes.
# - Authentication: Checking whether a user is allowed to perform an action.
# - Caching: Reusing previously calculated results.
# - Validation: Checking inputs before running a function.

#two topics still pending

