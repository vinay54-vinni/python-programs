#exception
# An exception is an error that occurs while a program is running and interrupts the normal flow of the program
x = 10
y = 0

# print(x / y)#Here exception happens and the remaining rogram will stops excecutig

print("Hello")

try:
    print(10 / 0)
except:
    print("Something went wrong")

# try → "Try running this code."

# except → "If an exception happens, handle it here."
try:
    print(10 / 0)
except:
    print("Error handled")#Example program

print("Program continues")

# flow:
# try
#  ↓
# Exception occurs
#  ↓
# except
#  ↓
# Handle exception
#  ↓
# Program continues

try:
    print("A")        # ✅ runs
    print(10 / 0)     # ❌ exception occurs
    print("B")        # ❌ skipped
except:
    print("C")        # ✅ runs
# Once an exception occurs inside a try block, Python immediately leaves the try block and moves to the matching except


# - ValueError → invalid value
# - TypeError → incompatible types
# - IndexError → invalid list index
# - KeyError → missing dictionary key
# - NameError → undefined name
# - AttributeError → object doesn't have that method/attribute
# - ZeroDivisionError → division by zero
def demonstrate_exceptions():
    # 1. ValueError: Passing a valid type but an invalid value
    try:
        print("--- Testing ValueError ---")
        number = int("banana")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    # 2. TypeError: Performing an operation on incompatible types
    try:
        print("--- Testing TypeError ---")
        result = "Hello" + 5
    except TypeError as e:
        print(f"Caught TypeError: {e}\n")

    # 3. IndexError: Trying to access a non-existent list index
    try:
        print("--- Testing IndexError ---")
        my_list = [10, 20, 30]
        print(my_list[5])
    except IndexError as e:
        print(f"Caught IndexError: {e}\n")

    # 4. KeyError: Trying to access a missing key in a dictionary
    try:
        print("--- Testing KeyError ---")
        my_dict = {"name": "Alice"}
        print(my_dict["age"])
    except KeyError as e:
        print(f"Caught KeyError: Missing key {e}\n")

    # 5. NameError: Accessing a variable that has not been defined
    try:
        print("--- Testing NameError ---")
        print("undefined_variable")
    except NameError as e:
        print(f"Caught NameError: {e}\n")

    # 6. ZeroDivisionError: Attempting to divide a number by zero
    try:
        print("--- Testing ZeroDivisionError ---")
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    
    try:
        print("-- Testing AttributError")
        a = [1,2,3]
        a.upper()
    except AttributeError as a:
        print(f"upper not possible in list:{a}\n")


if __name__ == "__main__":
    demonstrate_exceptions()



try:
    x = 0
    print(10 / x)
#Python checks the first exception and try checks for it's suitable handling method example if they occcur ValueError it checks for value error 
#and execute only the block of code inside that remaining exception handlings were skipped and continues the remaining program
except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

print("Finished")
# try
#  ↓
# 10 / 0
#  ↓
# ZeroDivisionError occurs
#  ↓
# except ZeroDivisionError
#  ↓
# "Cannot divide by zero"
#  ↓
# try/except is finished
#  ↓
# "Finished"



# except Exception
# Exception is a general parent class for most normal runtime exceptions
#Example program
try:
    print(10 / 0)
except Exception:#if we don't know what exception occur if we write this Exception also it handles
#if they have both this Exception and occured exception the program executes the block which thta exception belongs to it they dosen't have that 
#then it Executes the normal Exception block
    print("Error handled")



#example
try:
    print(10 / 0)
#Here it occurs Zero Division error so only executes that block of code only 
except ZeroDivisionError:
    print("Zero division")
#it dosen't execute this exception 
except Exception:
    print("General error")



# finally
# The finally block is used for code that should run whether an exception occurs or not.
try:
    print(10 / 0)
except:
    print("Error")
finally:
    print("Finally")#@output:Error ,finally


#WorkFLow
# | Situation | `try` | `except` | `else` | `finally` |
# |---|---|---|---|---|
# | No exception | ✅ | ❌      | ✅     | ✅       |
# | Exception occurs | ✅  | ✅ | ❌     | ✅       |


# # raise — Manually Creating an Exception
# But sometimes we want to create an exception ourselves when a condition is not acceptable.
# For that, Python provides the raise keyword.
# Example:
try:
    age = 15
    if age < 18:
        raise Exception("Age must be 18 or above")
except Exception:
    print("exception occur")
finally:
    print("age must be greater than 18")

# raise doesn't just display a message—it raises an exception and interrupts normal execution, unless something handles that exception.
try:
    marks = -5

    if marks < 0:
        raise ValueError("Marks cannot be negative")

except ValueError:
    print("Invalid marks")

print("Program continues")
# marks = -5#@output:Invalid marks → Program continues
#      ↓
# marks < 0 → True
#      ↓
# raise ValueError
#      ↓
# Leave the try block
#      ↓
# except ValueError catches it
#      ↓
# "Invalid marks"
#      ↓
# Continue after try-except
#      ↓
# "Program continues"



#Custom Exceptions
#For creating our own exception we use this 

class InvalidMarksError(Exception):#This is custom exception here we are creating our own exception
    pass
#InvalidAgeError → our custom exception name
#(Exception) → it inherits from Python's Exception
try:
    marks = 105

    if marks > 100:
        raise InvalidMarksError("Marks cannot exceed 100")

    print("Valid marks")

except InvalidMarksError:
    print("Invalid marks")

print("Finished")

#flow
# Create custom exception
#         ↓
# class InvalidAgeError(Exception)
#         ↓
# Raise it
#         ↓
# raise InvalidAgeError(...)
#         ↓
# Handle it
#         ↓
# except InvalidAgeError


