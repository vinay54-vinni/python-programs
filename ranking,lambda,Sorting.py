# Sorting in Python:

# Sorting means arranging elements in a particular order.
# - Ascending order: smallest to largest.
# - Descending order: largest to smallest.

# Using sorted():
# sorted() returns a new sorted list without changing the original list.

a = [40, 10, 30, 20]
b = sorted(a)
print(b)#output:[10, 20, 30, 40]
print(a)#output:[40, 10, 30, 20]

# Using sort():
# sort() sorts the original list directly.

a = [40, 10, 30, 20]
a.sort()
print(a)#output:[10, 20, 30, 40]
#it is not possible for us to intialize the sort value into another variable
#Example:
a = [5, 2, 8, 1]
b = a.sort()
print(b)
#Output:None

# a.sort() → sorts the original list and returns None.
# sorted(a) → returns a new sorted list



# Ascending vs. descending:

#If we keep reverse=True it prints the order in descending order

a = [40, 10, 30, 20]
print(sorted(a, reverse=True))
#output:
# [40, 30, 20, 10]

# Sorting with key:

words = ["apple", "kiwi", "banana"]
result = sorted(words, key=len)#this is for ascending for descending @result = sorted(words, key=len, reverse=True)
print(result)#output:['kiwi', 'apple', 'banana']

# Sorting a list of dictionaries:
employees = [
    {"name": "Ravi", "salary": 30000},
    {"name": "Aman", "salary": 45000},
    {"name": "Priya", "salary": 35000}
]

result = sorted(employees, key=lambda x: x["salary"], reverse=True)

print(result[0]["name"])#output:Aman




# Lambda functions:
#For writing hole function in one line we use lambda function and it automatically contains return method

# #syntax:
# lambda n: n * n

double = lambda x: x * 2
print(double(6))#output:6*2 = 12

#work flow:
# lambda creates a small function.
# x is the input variable.
# x * 2 is the calculation.
# double(6) passes 6 into x.


# What happens with two arguments:
add = lambda a, b: a + b
print(add(10, 20))#output:30

#worrkflow:
# The important point is that the number of parameters must match the arguments you pass, unless you use special parameter features.
# - lambda a: a * 2 → one parameter.
# - lambda a, b: a + b → two parameters.
# - add(10, 20) → passes two arguments, 10 and 20.
# The names a and b are just variable names. You could use x and y instead.


#Lambda with sorted() — a key interview concept:
numbers = [23, 15, 42, 31]

result = sorted(numbers, key=lambda x: x % 10)
print(result)#output:[31, 42, 23, 15]


#lambda functions using sorting:
students = [("Ravi", 75), ("Priya", 92), ("Aman", 68)]

result = sorted(students, key=lambda x: x[1], reverse=True)#here  x[0]=names ,x[1]=numbers

print(result)#output:[('Priya', 92), ('Ravi', 75), ('Aman', 68)]


# # What is the difference between key=len and key=lambda x: len(x):
# sorted(words, key=len),sorted(words, key=lambda x: len(x)) both are same but fr function creation we use lambda


# Sorting dictionaries using lambda:
marks = {
    "Ravi": 75,
    "Priya": 92,
    "Aman": 68
}
result = sorted(marks.items(), key=lambda x: x[1], reverse=True)

print(result)#output:[('Priya', 92), ('Ravi', 75), ('Aman', 68)]

# How does it work?
# # Step 1: marks.items() provides the key-value pairs as tuples.
# [("Ravi", 75), ("Priya", 92), ("Aman", 68)]
# step 2: lambda x: x[1] selects the second element of each tuple — the mark.
# - ("Ravi", 75) → 75
# - ("Priya", 92) → 92
# - ("Aman", 68) → 68
# Step 3: reverse=True places the highest marks first.

# Remember that sorted() returns a list of tuples here, not a dictionary.

# Lambda with max():
employees = [
    {"name": "Ravi", "salary": 30000},
    {"name": "Aman", "salary": 45000},
    {"name": "Priya", "salary": 35000}
]

top = max(employees, key=lambda x: x["salary"])

print(top["name"])#output:Aman

# max() finds the item with the highest value.
# key=lambda x: x["salary"] tells Python to compare employees by salary.
# Aman earns 45000, the highest salary.
# max() finds the item with the highest key value.
# min() finds the item with the lowest key value.
# sorted() returns all items in sorted order.

numbers = [12, 45, 23, 9]

print(sorted(numbers, reverse=True)[0])#we can also get in one value in sorting 
print(max(numbers))#output:both prints 45




#Ranking:
#For Ranking we use ranking it uses enumerate for ranking 

# enumerate() doesn't sort the list. It simply adds a counter to each item.
# - enumerate(names) starts at 0.
# - enumerate(names, start=1) starts at 1.

students = [("Ravi", 75), ("Priya", 92), ("Aman", 68), ("Sara", 85)]

ranked = sorted(students, key=lambda x: x[1], reverse=True)

for rank, student in enumerate(ranked, start=1):
    print(rank, student[0], student[1])

#output:
# 1 Priya 92
# 2 Sara 85
# 3 Ravi 75
# 4 Aman 68

# enumerate(ranked, start=1) gives each student a rank beginning at 1.
# student[0] accesses the name, while student[1] accesses the marks.

#example for list:
numbers = [30, 10, 20]

ranked = sorted(numbers, reverse=True)

for rank, num in enumerate(ranked, start=1):
    print(rank, num)

#output:
# 1 30
# 2 20
# 3 30



students = [("Ravi", 90), ("Aman", 90), ("Priya", 85)]

ranked = sorted(students, key=lambda x: (-x[1], x[0]))

print(ranked)#output:[('Aman', 90), ('Ravi', 90), ('Priya', 85)]

# key=lambda x: (-x[1], x[0]) uses two criteria:
# - -x[1] — marks in descending order (highest first).
# - x[0] — names in alphabetical order if marks are equal.
# Ravi and Aman have equal marks, so Python compares their names. Since Aman comes before Ravi alphabetically, Aman is placed first.


# Python Sorting, Lambda Functions and Ranking — Progress:
# sorted() vs .sort()
# Ascending and descending order
# Sorting with key=
# Lambda functions and lambda-based sorting
# Sorting tuples and dictionaries
# Sorting by multiple criteria
# enumerate() and ranking
# Selecting the top N items
# Finding the second-highest distinct value
# Using max() and min()
# Ranking ties and stable sorting

# key:key parameter specifies a custom function that determines the sorting criteria.