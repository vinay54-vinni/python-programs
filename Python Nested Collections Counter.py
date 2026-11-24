# #nested collections:
# A nested collection is a collection that contains another collection inside it.

#example :
marks = [[80, 90], [70, 85], [95, 88]]

print(marks[0])
print(marks[0][1])#output:[80, 90]


# Nested List Indexing:
data = [[10, 20], [30, 40], [50, 60]]

print(data[1][0])#output:30

#Nested Dictionary:
student = {
    "name": "Ravi",
    "marks": {
        "Python": 85,
        "SQL": 90
    }
}

print(student["marks"]["SQL"])#output:90

#Updating Nested Collections:
data = [[10, 20], [30, 40]]

data[0][1] = 99

print(data)#output:[[10, 99], [30, 40]]

#Nested Loops:
data = [[1, 2], [3, 4]]

for row in data:
    for value in row:
        print(value, end=" ")#output:1,2,3,4,






# #Counter Class:
# Python provides Counter through the collections module. It helps us count how many times each element appears.

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

result = Counter(numbers)

print(result)#output:Counter({3: 3, 2: 2, 1: 1})
#if you want count of one item also it possibl like print(result[2])

# #Counter with most_common():
# it helps identify the most frequent elements.
from collections import Counter

numbers = [4, 4, 2, 2, 2, 7]

count = Counter(numbers)

print(count.most_common(1))#output:2

# most_common(1) returns one element.
# most_common(2) returns two elements.
# most_common() returns all elements, ordered by frequency

# Counting Characters in a String:
from collections import Counter

text = "banana"

count = Counter(text)

print(count["a"])#output:3

#Nested Dictionary and Counter:
from collections import Counter

students = {
    "A": ["Python", "SQL", "Python"],
    "B": ["Java", "SQL"]
}

count = Counter(students["A"])

print(count["Python"])#output:2

#Counter — Missing Keys:
from collections import Counter

count = Counter(["apple", "banana", "apple"])

print(count["orange"])#output:0
#In counter if any item is missing instead of keyerror it shows 0

#Counter — Subtracting Frequencies:
from collections import Counter

a = Counter(["x", "x", "y"])
b = Counter(["x", "y", "y"])

print(a - b)#output:Counter({'x': 1})
#Counter subtraction keeps only positive counts. Compare the frequency of each element in a with its frequency in b.

# Counter — Updating Counts:
from collections import Counter

count = Counter("aab")

count.update("bc")

print(count)#output:Counter({'a': 2, 'b': 2, 'c': 1})






