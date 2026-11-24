# #functions
#defination
# A function is a reusable block of code that performs a specific task.
# Instead of writing the same code again and again, we can put it inside a function and call it whenever we need it.
def greet():#creating a function 
    print("Hello Vinay")

greet()#calling a function
# - def → tells Python we're creating a function
# - greet → function name
# - () → parameters go here
# - : → starts the function body
# - print() → code inside the function
# - greet() → calling the function


def test(a, b=10, c=20):# The Arguments was assigned according to the position 
    print(a, b, c)
test(5, c=50)# in here 5 goes under a and here c is written as keyword argument so c value changes b value in normal as b.
# from the above a is called positional parameter or required parameter 
# b and c is called default parameters or optional parameters



def add(a, b):
    return a + b# if we doesn,t write return in function it doesn't possible for it to instialize the value to another variable
result = add(10, 20)#like if we doesn't write return in above if we print result the value appear as None
print(result * 2)


def test():
    print("A")       # executes
    return "B"       # returns B and exits the function
    print("C")       # ❌ never executes
#the code after return was never executes
result = test()
print(result)        # prints B



# #(*args)
# *args collects all positional arguments into a tuple
# # (**kwargs)
# **kwargs collects keyword arguments into a dictionary
def test(a, b=5, *args):
    return a + b + sum(args)
print(test(10, 20, 1, 2, 3))#@output : 36
# - a = 10
# - b = 20
# - args = (1, 2, 3)
# - sum(args) = 6


#positional arguments,keyword arguments in notes 

