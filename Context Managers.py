# Context Managers:
# A Python context manager is a special object that automatically handles the allocation and release of resources when you use a with statement.

#without context manager:
f = open("data.txt", "w")#open used to open the file
f.write("Hello Python")#write used to somethng iwriting in the file
f.close()# used for closing the file
# here If an error occurs before f.close(), the file might remain open



#with context manager:
with open("data.txt", "w") as f:
    f.write("Hello Python")

# with : Starts the context-managed block.

# as f : Stores the opened file object in f.

# Automatic cleanup:Closes the file when the block exits.

# with statement:
#syntax:
            with expression as variable:
                 statements

# How does a Context Manager work:

with open("data.txt", "w") as f:
    f.write("Hello Python")

print("Done")

# open("data.txt", "w") opens the file for writing.
# as f stores the file object in the variable f.
# f.write() writes "Hello Python" into the file.
# When Python exits the with block, it automatically closes the file.
# Python executes print("Done").




#__enter__() and __exit__():
# Understanding __enter__()
# - Executes when Python enters the with block.
# - Can return a value that gets assigned to the variable after as.


#  Understanding __exit__()
# - Executes when Python leaves the with block.
# - Handles cleanup, even if an exception occurs inside the block.
# - Can determine whether an exception should be suppressed.

#Example : 
class MyContext:
    def __enter__(self):#Here it enters into the block and exceutes when it enters into with bolck
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):#it executes after with block 
        print("Exiting")

with MyContext():
    print("Inside block")

# #output:
# Entering
# Inside block
# Exiting




# What does __enter__() return:

class MyContext:
    def __enter__(self):
        print("Entering")
        return "Hello Python"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

with MyContext() as result:
    print(result)#output : entering\n hello python \n exiting

# MyContext() creates the context manager object.
# __enter__() prints Entering.
# __enter__() returns "Hello Python".
# The returned value is assigned to result because of as result.In enter block what it returns that value taken as class output so when we use class and store it in result the return value of class is assigned to result
# print(result) prints Hello Python
# When the block ends, __exit__() prints Exiting.




# How does __exit__() handle exceptions:

class Demo:
    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleanup")

with Demo():
    print(10 / 0) #output : start\n cleanup


# __enter__() prints Start.
# Python tries to execute 10 / 0.
# A ZeroDivisionError occurs.
# Python calls __exit__() to perform cleanup.
# __exit__() prints Cleanup.
# The exception continues propagating, so the program reports the error.

# The three exception arguments are:
# - exc_type — the exception's type, such as ZeroDivisionError.
# - exc_value — the exception instance and its details.
# - traceback — information about where the exception occurred.




# Suppressing exceptions with __exit__():
class Demo:
    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception handled")
        return True#if we dosen't return true the exception dosen't surpasses it still propagates

with Demo():
    print(10 / 0)

print("Program continues")#output : start\n Exception handled\n Program continues

# Return value from __exit__()	Result when an exception occurs
#     True	                         Exception is suppressed
#     False	                         Exception propagates
#     None	                         Exception propagates




# Creating a Context Manager Using a Class:
class MyFile:
    def __enter__(self):
        print("Opened")
        return self#here self refers to assigns the same context manager object to obj.

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closed")
        #if we dosen't  have anything here it means it return value is Noone

    def show(self):
        print("Resource")

with MyFile() as obj:
    obj.show()#output : Opened\n Resource\n Closed


# 1. MyFile() creates a context manager object.
# 2. __enter__() runs and prints Opening resource.
# 3. return self assigns the same object to obj.
# 4. obj.show() calls the show() method.
# 5. When the block ends, __exit__() runs and prints Closing resource.
# this is a custom context manager because we created the class and implemented __enter__() and __exit__() ourselves.

# Also, __exit__() returns None here, so any exception raised inside the block would propagate after cleanup.





# Context Managers Using contextlib:
# Python provides a built-in module called contextlib that makes creating context managers easier.
# Instead of defining a class with __enter__() and __exit__(), we can use the @contextmanager decorator with a generator function.

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Opening resource")
    try:
        yield "Hello Python"
    finally:
        print("Closing resource")

with my_context() as result:
    print(result) #output : Opening resource\n Hello Python\n Closing resource

# Why do we use try and finally in a context manager:
#If any exxception occurs in the middel of the code those 2 are used to handle exception 

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Opening")
    try:
        yield
    finally:
        print("Closing")

with my_context():
    print("Working")
    raise ValueError("Something went wrong")
#output :
# Opening
# Working
# Closing
# Traceback (most recent call last):  # from here occured error were not surpassed so error still occurs 
#     ...
# ValueError: Something went wrong  

# #work flow:
# Opening is printed.
# yield pauses the generator and lets the with block executed
# Working is printed.
# raise ValueError(...) raises an exception.
# The exception is thrown back into the generator at the yield point.
# The finally block executes and prints Closing.
# The exception continues propagating because we haven't suppressed it.





# Real-world example — Managing a file:
from contextlib import contextmanager

@contextmanager
def open_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()

with open_file("data.txt") as file:
    file.write("Learning Python Context Managers")

# How this works:
# 1. open_file("data.txt") opens the file.
# 2. yield f provides the opened file object to the with block.
# 3. file.write() writes the text.
# 4. When the block exits, finally closes the file.
# 5. The file is closed even if an exception occurs inside the block.
# This is a custom context manager created using @contextmanage


# Multiple Context Managers:
with open("input.txt", "r") as source, open("output.txt", "w") as target:
    data = source.read()
    target.write(data)
#or
#we can also use nested with:
with open("input.txt", "r") as source:
    with open("output.txt", "w") as target:
        data = source.read()
        target.write(data)

#work flow:
# Python opens input.txt for reading.
# It opens output.txt for writing.
# The contents of the first file are read and written to the second.
# When the block exits, both files are closed automatically





# The closing() Context Manager:
# Python's contextlib module provides a useful helper called closing().

# It lets you use an object in a with statement when that object has a .close() method but doesn't implement the context manager protocol itself.

from contextlib import closing

class Demo:
    def close(self):
        print("Resource closed")

with closing(Demo()) as obj:
    print("Using resource")

# output:
# Using resource
# Resource closed

#workflow:
# Demo() creates an object.
# closing() makes it usable as a context manager.
# as obj receives the object.
# The block prints Using resource.
# When the block exits, closing() calls obj.close()




# contextlib.suppress():
# Python provides another helpful context manager: suppress().
# It lets us ignore specific exceptions when we intentionally decide that those exceptions don't need to interrupt execution.


from contextlib import suppress

with suppress(ZeroDivisionError): #here if we get any that specified error(zerodiv) it surpasses it  and continues the program
    print(10 / 0)
    print("Hello")

print("Done")#output : Done

#workflow:
# Python enters the with block.
# 10 / 0 raises a ZeroDivisionError.
# suppress(ZeroDivisionError) suppresses that particular exception.
# Execution continues after the block, printing hello
   



# contextlib.nullcontext():
# nullcontext() is a context manager that does nothing special. 
# It lets you use a with statement even when you don't need to manage a resource.

from contextlib import nullcontext

with nullcontext("Hello Python") as value:
    print(value)#output:hello python


# Important distinction:
# Feature	                         Purpose
# try/except	         Handles exceptions in the usual way
# finally	             Runs cleanup code
# __exit__()	         Performs context-manager cleanup and can suppress exceptions
# suppress()	         Suppresses specifically selected exception types



#topics covered in this
# Context manager fundamentals:
# with statement and automatic cleanup
# Built-in file context managers:
# Reading, writing and closing files
# Custom context managers
# __enter__() and __exit__()
# Exception handlin
# Propagation, suppression and cleanup
# Generator-based context managers
# @contextmanager and yield
# Resource management
# try/finally and closing()
# Additional contextlib helpers
# suppress() and nullcontext()
# Nested context managers
# Reverse-order cleanup
# Common mistakes  :
# Forgetting to use with
# Confusing return self with return in __enter__()
# Assuming __exit__() always suppresses exceptions
# Forgetting cleanup in a custom context manage
