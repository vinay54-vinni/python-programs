#Map:
#map() transforms every item by applying a function applies for every item
names = ["ravi", "sita", "ram"]

result = list(map(str.upper, names))

print(result)#output:['RAVI', 'SITA', 'RAM']





#Filter:
#filter() selects items that satisfy a condition , Only applies for condition applied one's.
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)#output:[2, 4, 6]

#workflow:
# filter() checks each number using x % 2 == 0.
# - 1 → False, excluded
# - 2 → True, kept
# - 3 → False, excluded
# - 4 → True, kept
# - 5 → False, excluded
# - 6 → True, kept



#reduce():
#reduce() combines multiple values into one final value by repeatedly applying a function
from functools import reduce

numbers = [2, 3, 4]

result = reduce(lambda x, y: x * y, numbers)

print(result)#output:24

#workflow:
# First: 2 * 3 = 6
# It consider first x,y values as 2,3 and do combies thoes.
# In next step the gotted value consider as x and remaining value as y the conduct operation on both
# Next: 6 * 4 = 24
