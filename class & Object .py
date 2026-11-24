#Class & Object :


# What is a Class:
# A class is like a blueprint/template used to create objects.

#Example:
class Student:
    pass

# - class → keyword used to create a class
# - Student → class name
# - pass → means "nothing is written inside the class yet"

# Class = Blueprint

# What is an Object:
# An object is an actual thing created from a class.

class Student:
    pass

s1 = Student()

#Example:
# - Student → class
# - s1 → object
# - Student() → creates an object
# So:
# Class → blueprint
# Object → actual thing created using that blueprint

# 🏠 House blueprint → Class
# 🏠 Actual house built from blueprint → Object


#Creating Multiple Objects:
class Student:
    pass

s1 = Student()
s2 = Student()
s3 = Student()


# Student → one class
# s1 → first object
# s2 → second object
# s3 → third object

#WORKFLOW:
# Class
#   ↓
# Blueprint

# Object
#   ↓
# Actual instance created from the blueprint


#Example Program:
class Student:
    pass

s1 = Student()
s1.name = "Vinay"

s2 = Student()
s2.name = "Rahul"

print(s1.name)#vinay
print(s2.name)#Rahul


# __init__() Method also know an constructor or special method:
# __init__() is a special method that runs automatically when an object is created.

class Student:
    def __init__(self, name):# HERE name is parameter 
        self.name = name

s1 = Student("Vinay")# here vinay is argument
s2 = Student("Rahul")

print(s2.name)#Rahul
print(s1.name)#vinay

# # Instance Variables :
# The variables we create using self are called instance variables

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("vinay",21)

# self.name → instance variable
# self.age → instance variable
#self → refers to the current object her curent object was s1



# Instance Methods:

# A function defined inside a class that belongs to a specific object (instance) created from that class:


class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student("Vinay")
s1.display()#we can ddirectly acceess method using object 

# Class
#  ├── Instance Variables → self.name
#  └── Instance Methods   → display()



#Example :
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Instance variable
        self.balance = balance      # Instance variable

    # deposit is an INSTANCE METHOD
    def deposit(self, amount):
        self.balance += amount      # It modifies this specific account's balance
        return f"{self.owner}'s new balance is ${self.balance}"

# Creating two independent instances
alice_account = BankAccount("Alice", 100)
bob_account = BankAccount("Bob", 50)

# Calling the instance method
print(alice_account.deposit(50))  # Output: Alice's new balance is $150
print(bob_account.balance)       # Output: 50 (Bob's balance remains untouched)


class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
#We can give a parameter a default value
#If an argument is not provided, its default value is used


#TRICKY QUESTION:
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Vinay")
s2 = Student("Rahul")

s1.name = "Kiran"

print(s1.name)#KIRAN
print(s2.name)#Rahul



#Class Variable vs Instance Variable:
class Student:
    college = "ABC College"   # Class variable

    def __init__(self, name):
        self.name = name       # Instance variable

#CLASS VARIABLE: SHARED BY ALL OBJECTS
#INSTANCE VARIABLE: Each object has its own value

# | Variable       |     Belongs to | Example |
# 
# | Class variable | Class / shared | `college` |
# | Instance variable | Individual object | `self.name` |
        


#EXAMPLE:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def add_marks(self, value):#HERE BY USING INSTANCE METHOD WE CAN ABLE TO CHANGE INSTANCE VARIABLES
        self.marks = self.marks + value

s1 = Student("Vinay", 70)
s1.add_marks(10)

print(s1.marks)#@OUTPUT : 80


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40#IN INSTANCE VALUES DOESN'T ONLY PRINT THOSE CAN ALSO RETURN

s1 = Student("Vinay", 70)

print(s1.is_pass())#@OUTPUT:TRUE



class Student:
    def __init__(self, name):
        self.name = name

    def change(self):#This creates only a local variable called name.
        name = "Rahul"#INSTANCE VARIABLE DOSEN'T CHANGE

s1 = Student("Vinay")
s1.change()

print(s1.name)#@OUTPUT:"VINAY"


class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Vinay")
s2 = Student("Rahul")

s2 = s1

print(s2.name)
#s2 = s1 means s2 gets the reference to s1's object. It does not copy the old "Rahul" object



# s1 = Student("Vinay")
# s2 = Student("Vinay")
# s1 is s2 → False ❌ different objects
# s1 == s2 → False ❌ by default, separate objects are not considered equal




# __str__():
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return self.brand

c1 = Car("BMW")

print(c1)#@OUTPUT:BMW

#HERE WHEN WE TRY TO PRINT C1 AND WE ARE NOT INTIALIZIED FOR IT WEATHER WE WANT NAME OR SOME WHAT WHEN WE USE __STR__ IT AUTOMATICAALLY 
#GIVE STRING VALUE F WE DOSEN'T DECLARE ALSO


class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Vinay")

s1.age = 22#we can able to add or delete a variable to object 
del s1.age
print(s1.name)
#print(s1.age)#@output: error if we print this line


#class method:
# A class method works with the class itself
# A class method works with the class, not a particular object
# We use the decorator:
# @classmethod
# instead of self, we normally use:@cls  


class Student:
    college = "ABC College"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()



#example:
class Student:
    college = "ABC College"

    @classmethod
    def change(cls):
        cls.college = "XYZ College"

s1 = Student()
s1.change()

print(Student.college)



# | Method          | First parameter | Works mainly with |

# | Instance method | `self`          | Object |
# | Class method    | `cls`           | Class |
# | Static method | Nothing required  | Neither |




#Static method:
#this method is used to call a class method  directly with or without using object 
class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b

c1 = Calculator()

print(c1.multiply(4, 5))
print(Calculator.multiply(5,4))


# A static method can be called using either
# Calculator.multiply(4, 5)//class Name 
# or c1.multiply(4, 5)//by object name


# Instance method → self → object data
# Class method → cls → class data
# Static method → no automatic self or cls

#== and __eq__ :
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Vinay")
s2 = Student("Vinay")

print(s1 == s2)
#in this code if we dosen't write equ method if we print s1==s2 it gives false because both values same but different objects 
#but when we use __eq__ it tells python checks the data of both object if the data same then it prints TRUE 
#if the objects has "vinay" and "Rahul" if we use __eq__ also we get False because the data was different


#what we covered in this whole code:
# ✅ Class & Object
# ✅ __init__()
# ✅ self
# ✅ Instance variables
# ✅ Instance methods
# ✅ Class variables
# ✅ Object references
# ✅ is vs ==
# ✅ __str__()
# ✅ Adding/deleting attributes
# ✅ Class methods
# ✅ Static methods
# ✅ __eq__()




