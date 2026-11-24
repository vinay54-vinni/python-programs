# Inheritance:
# Inheritance means one class can acquire the properties and methods of another class.

# work flow
# Parent Class
#      ↓
#  Child Class

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

d = Dog()
d.eat()

# Animal → Parent class
# Dog → Child class
# Dog inherits eat() from Animal

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def display(self):
        print("Child")

c = Child()
c.show()
c.display()
#Here we are using only child method for displaying both methods like display() and show()
# in  normal conditions it leads to error but by using this inheritance we can able to acess paraent class method by using children's object 


class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

c = Child()
c.show()
#from above in both parent and child class having same method_name when we try to print c.show() 
# it checks in the object Like, it belongs to parent class or child class so form above it belongs to child class so it  first checks in child classs for that method
# If that dosen't exist in that method then it checks and print the data in parents class like before code when we call c.show()
# the method which was calling is not in that object so it prints the method from the parent

# If Child has it → use Child's version.
# If Child doesn't have it → look in Parent.

# super():
# super() is used to access the parent class from the child class

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        super().show()#if we use it after the child like 
        print("Child")#Example:print("child")
                    #    super().show()   #@output:"child\n","parent",

c = Child()
c.show()#@output:"parent\n","child"

# So execution is:
# 1. c.show() → Child's show()
# 2. super().show() → Parent's show() → prints Parent
# 3. print("Child") → prints Child

# when we use __init__() constructor:
class parent:
    def __init__(self):
        print("hello hi")

class child(parent):
    print("hei hi")# we can use super().__init__()then we get output like 
c = child()#when we dosen't call any method 
#@output:
# hei hi
# hello hi


class parent:
    def __init__(self):
        print("hello hi")

class child(parent):
    
        print("hei hi")
        # super().__init__()#if we execute like this we get error because we can't able to call a method inside a class 

c = child()


#Example:

class parent:
    def __init__(self):
        print("hello hi")

class child(parent):
    def vinay(self):
        print("hei hi")
        super().__init__()#if we write this or we dosen't also it no matters

c = child()#@output:"hello hi" cause because when a method called in a class it checks for init method so it checks for
#it found that in parent so it prints only parent method after it dosen't consider remaining print statements


class parent:
    def __init__(self):
        print("hello hi")

class child(parent):
    def __init__(self):
        print("hei hi")
        super().__init__()

c = child()#@output: hei hi \n , hello hi


# WORK FLOW:
# Child constructor starts
#         ↓
# super().__init__()
#         ↓
# Parent constructor runs
#         ↓
# Parent
#         ↓
# back to Child
#         ↓
# Child

# | Child has `__init__()`?       | What runs? |

# | ❌ No                         | Parent constructor |
# | ✅ Yes                        | Child constructor |
# | ✅ Yes + `super().__init__()` | Child + Parent constructor |


# TYPES OF INHERITANCE :
# a) Multiple inheritance
# b) Multilevel inheritance
# c) Single inheritance 
# d) Hierarchical inheritance


# Single → one parent → one child
# Multilevel → Grandparent → Parent → Child
# Multiple → multiple parents → one child
# Hierarchical → one parent → multiple children


# a)Multiple inheritance:
class Father:
    def skills(self):
        print("Father")

class Mother:
    def talent(self):
        print("Mother")

class Child(Father, Mother):
    pass

# Father ──┐
#          ↓
#        Child
#          ↑
# Mother ──┘

#b_)multilevel:
class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

# Grandparent
#      ↓
#   Parent
#      ↓
#    Child


# 3)Hierarchical inheritance:
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

    #    Animal
    #    /    \
    #   ↓      ↓
    # Dog     Cat


# # MRO (Method Resolution Order) challenge:
# he complexity Python faces when determining the exact sequence or "order" 
# it should follow to search for a method or attribute in multiple inheritance scenarios.

#Example:
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()#@output:D → B → C → A