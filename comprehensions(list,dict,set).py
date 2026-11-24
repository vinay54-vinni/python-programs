# List, Set and Dictionary Comprehensions:

# # List Comprehension:
# A list comprehension creates a new list in a single line of code

# in general the code was:
numbers = [1, 2, 3, 4, 5]
result = []

for i in numbers:
    result.append(i * 2)

print(result)

#By Using comprehension:
numbers = [1, 2, 3, 4, 5]
result = [i * 2 for i in numbers]

print(result)

# The general syntax is:

# [expression for item in iterable]

# - expression: what you want to store.
# - item: each value taken from the iterable.
# - iterable: the list or other collection you iterate over

# List Comprehension with Transformation:
numbers = [1, 2, 3, 4]
result = [i * i for i in numbers if i > 2]
print(result)#output : 9,16

# work flow:
# 1. > 2 filters the numbers, keeping only 3 and 4.
# 2. i * i squares those numbers: 3 * 3 = 9 and 4 * 4 = 16.
# Output: [9, 16]


# List Comprehension with if-else:
numbers = [1, 2, 3, 4]
result = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(result)#output :["Odd", "Even", "Odd", "Even"]

#Nested List Comprehension:
result = [i * j for i in [1, 2] for j in [3, 4]]
print(result)#[3, 4, 6, 8]

                                  #set


#Set Comprehension:
numbers = [1, 2, 2, 3, 3, 4]
result = {i for i in numbers}
print(result)
#explanation:
# - {i for i in numbers} creates a set comprehension.
# - Sets automatically remove duplicate values.
# - Therefore, each number appears only once.
# Output: {1, 2, 3, 4}

#Set Comprehension with a Condition:
numbers = [1, 2, 3, 4, 5, 6]
result = {i * i for i in numbers if i % 2 == 0}
print(result)#output:{4, 16, 36}


                                           #dictionary 

# Dictionary Comprehension:
numbers = [1, 2, 3, 4]
result = {i: i * i for i in numbers}
print(result)#output:{1: 1, 2: 4, 3: 9, 4: 16}

#Dictionary Comprehension with a Condition:
marks = {"Vinay": 85, "Ravi": 92, "Anu": 78}
result = {name: score for name, score in marks.items() if score >= 85}
print(result)#output:{"Vinay": 85, "Ravi": 92}

#Transforming Dictionary Values:
marks = {"Vinay": 80, "Ravi": 90}
result = {name: score + 5 for name, score in marks.items()}
print(result)#output : {"Vinay": 85, "Ravi": 95}


#Dictionary Comprehension with range():
result = {i: i * 2 for i in range(1, 5)}
print(result)#output:{1: 2, 2: 4, 3: 6, 4: 8}



                                        #three difference


# Type	                                Example           result
# List	                        [i * i for i in nums]	[1, 4, 9]
# Set	                            {i * i for i in nums}	{1, 4, 9}
# Dictionary	                   {i: i * i for i in nums}	{1: 1, 2: 4, 3: 9}