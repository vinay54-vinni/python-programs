# Iterators & Generators :
# An iterator is an object that allows us to access elements one at a time
# Normally, we can access its elements using indexes:
# But Python also lets us access elements one at a time using an iterator

a = [10, 20, 30]

it = iter(a)
print(next(it))#10
print(next(it))#20
print(next(it))#output : 10,20,30#30

# iter() — creates an iterator from an iterable, such as a list.
# next() — retrieves the next element from the iterator



# Iterable vs. Iterator:
# Iterable:
# An iterable is an object whose elements we can go through one by one.
# Lists, tuples, strings, and sets are all iterables.
a = [10, 20, 30]
b = (1, 2, 3)
c = "Python"
d = {1, 2, 3}

# Iterator
# An iterator is an object that gives us the next element whenever we call next().
a = [10, 20, 30]
it = iter(a)
print(next(it))#10
print(next(it))#20

# Iterable — a
# The original collection of elements, such as [10, 20, 30].

# Iterator — it
# Keeps track of the current position and produces the next element.

# Easy way to remember:
# - iter(a) → gets an iterator from an iterable.
# - next(it) → gets the next value from the iterator.


# StopIteration in Python:
a = [10, 20]
it = iter(a)

print(next(it))
print(next(it))
# print(next(it))#from above list we have only 2 elements in the list but when we try to access third element that raises an exception
# Python raises an exception called StopIteration

#output:
# 10
# 20
# StopIteration

#we can stop that error by using try and except block
a = [10, 20]
it = iter(a)

print(next(it))
print(next(it))

try:
    print(next(it))
except StopIteration:
    print("No more elements")

#     #@output:10
# 20
# No more elements


#__iter__() and __next__():

# __iter__() — returns the iterator object itself.
# __next__() — returns the next value whenever Python requests one.
class MyNumbers:
    def __iter__(self):# if we use another method instead of __iter__ & __next__ we can't able to get output
        self.x = 1
        return self

    def __next__(self):
        if self.x <= 3:
            value = self.x
            self.x += 1
            return value
        else:
            raise StopIteration

nums = MyNumbers()
it = iter(nums)

print(next(it))
print(next(it))
print(next(it)) #output:1,2,3

# __iter__()
# Initializes self.x = 1 and returns self, the iterator object.

# __next__()
# Checks whether self.x <= 3. If true, it returns the current number and increments it.

# raise StopIteration
# When self.x becomes 4, there are no more values, so the iterator signals that it has finished.






# # What is a Generator?:
# A generator is a special kind of iterator that produces values one at a time, whenever they are requested.

# Instead of writing a custom iterator with __iter__() and __next__(), we can often create a generator using a function and the yield keyword.

def numbers():
    yield 10
    yield 20
    yield 30

for i in numbers():
    print(i)#output : 10,20,30

# How does yield work?
# First request
# The function reaches yield 10, produces 10, and pauses.

# Second request
# Execution resumes after the first yield, produces 20, and pauses again.

# Third request
# It produces 30. When another value is requested, the generator finishes.

# next() with a generator:

def numbers():
    yield 10
    yield 20
    yield 30

g = numbers()

print(next(g))
print(next(g))
print(next(g))#if we call next again it causes stopiterartion error
#output : 10,20,30

# return vs. yield
# return	                                                    yield
# Returns a value and ends the function.	    Produces a value and pauses the function.
# Usually used for a final result.	        Used to produce a sequence of values over time.
# Doesn't resume that function afterward.	    Can resume from where it paused.

#imp question:
def numbers():
    yield 1
    return 2
    yield 3

g = numbers()

print(next(g))
# print(next(g))#<- when we print this it causes error StopIterable error #output:1

# Generator expression or comprehension:
a = (x * 2 for x in range(5))
print(next(a))
print(next(a))
print(next(a))#output : 0,2,4



# Generator Functions vs. Generator Expressions:
# A generator function is a function that uses the yield keyword to produce values one at a time.
def numbers():
    yield 10
    yield 20
    yield 30

g = numbers()

print(next(g))
print(next(g))
print(next(g))
#output:10
# 20
# 30

# Generator expression:
# A generator expression creates a generator using a compact expression inside parentheses ()
g = (x * 10 for x in range(1, 4))

print(next(g))
print(next(g))
print(next(g))
#output :
# 10
# 20
# 30

# Lazy Evaluation:
# Lazy evaluation means Python calculates or produces a value only when it is needed

def numbers():
    print("Started")
    yield 10
    print("Continuing")
    yield 20

g = numbers()
print("Created")
print(next(g))
print(next(g))

#output :
# Created
# Started
# 10
# Continuing
# 20

# 1. g = numbers() creates the generator, but the function body doesn't execute yet.
# 2. print("Created") runs first.
# 3. next(g) starts the function and produces 10.
# 4. The next next(g) resumes the function and produces 20.
# Key point: A generator pauses at yield and resumes when another value is requested. This is lazy evaluation.



# Generator advantages:
# Memory efficiency: They don't need to store all generated values at once.
# Lazy evaluation: They produce each value only when requested.
# Generators can reduce memory usage because they produce values on demand rather than storing all the values at once.

# One important note: generators aren't always faster than lists. The main advantage is often memory efficiency.


g = (x for x in range(1, 4))

print(list(g))
print(list(g))
#output  :[1, 2, 3] first, then []

def numbers():
    yield 1
    yield 2
    yield 3

for x in numbers(): #we can access it by for loop also
    print(x)#OUTPUT:1,2,3


#we can use multiplte generators at a time
g = (x for x in range(1, 4))
print(list(g))

g = (x for x in range(1, 4))
print(list(g))