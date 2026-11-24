#set concept
a={10,20,30,40,54,40,50}
print(a)#@output:{10,20,30,40,50,54}
#it won't allow duplicate so 40 won't print 2 times
# List → duplicates allowed
# Set  → duplicates not allowed
#empty_set = set() for creating empty set 
# it also don't allow indexing
a.add(45)#add() function is used to add new element in to set
a.update((445,554))#update() is used to add multiple values to set 
a.remove(445)#reomve() is used to remove a value from set ,if the removed value doesn't exist it gives error
a.discard(554)#if we use this if data dosen't exist also we don't get any error
b = a.pop()#if we use pop and add it to any variable the element was removed and the variable get that value
a.clear()# clears all values 
# Union A | B → everything from both sets
# Intersection A & B → common elements
# Difference A - B → elements in A but not B both commen elements will be removed and remaining value only gives 
# A.issubset(B) → Is A inside B?
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))#TRUE
# A.issuperset(B) → Does A contain B?
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
print(A.issuperset(B))#TRUE
# isdisjoint() checks whether two sets have no common elements
A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))#@TRUE

