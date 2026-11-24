#dataframe :
# A DataFrame is a two-dimensional data structure in Pandas. It stores data in rows and columns, like an Excel spreadsheet or a SQL table.

import pandas as pd

data = {
    "Name": ["Ram", "Sam", "John"],
    "Age": [21, 22, 23],
    "Marks": [80, 90, 85]
}
df = pd.DataFrame(data)
print(df)
#output:
#    Name  Age  Marks
# 0   Ram   21     80
# 1   Sam   22     90
# 2  John   23     85

print(df.shape)#it shows the dimensions of the data

#for creating data frame  from list
data = [
    ["Ram", 21, 80],
    ["Sam", 22, 90],
    ["John", 23, 85]
]

df = pd.DataFrame(data, columns=["Name", "Age", "Marks"],index = ["a","b","c"])#for custom index )

print(df)

#working in pandas using numpy 
import pandas as pd
import numpy as np

arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

df = pd.DataFrame(arr, columns=["A", "B"])

print(df)
#output :
#     A   B
# 0  10  20
# 1  30  40
# 2  50  60

# .loc[]
# We use .loc[] to select rows based on their index labels.
df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John"],
    "Marks": [80, 90, 85]
}, index=["A", "B", "C"])

print(df.loc["C", "Name"])#john

#iloc defines the position value
df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [40, 50, 60]
}, index=["X", "Y", "Z"])

print(df.iloc[1, 0])#here it represents the 2nd position 1st element @20

# Multiple Rows using .iloc[]
df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John", "Raj"],
    "Marks": [80, 90, 85, 70]
})

print(df.iloc[[0, 2]])#here we uses 2 square braces for multiple values
#output:
#    Name  Marks
# 0   Ram     80
# 2  John     85


#here we can also able to slicing 
df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John", "Raj", "Tom"],
    "Marks": [80, 90, 85, 70, 95]
})

print(df.iloc[1:4])#when we use iloc in sliicng we can,t able to get the last value

df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John"],
    "Age": [21, 22, 23],
    "Marks": [80, 90, 85]
})

print(df.iloc[:, 1])
#output:
# 0    21
# 1    22
# 2    23
# Name: Age, dtype: int64

# inclusive parameter
# We can control whether boundary values are included.
df[df["Marks"].between(50, 90, inclusive="neither")]#by using this we can excluede the metioned values


# query()
# Pandas query() lets us filter rows using a string expression.
# df.query("Marks > 50")#we can use  multiple query conditions here

# &	AND
# \|	OR
# ~	NOT
# isin()	Check membership in a list
# between()	Filter within a range
# query()	Filter using a string expression


df["City"] = ["Hyderabad", "Bangalore", "Chennai"]

print(df)#here by using this we are adding this column to the normal values


#Adding a column using a condition
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)
#output:
# Ram	80	Pass
# Sam	45	Fail
# John	90	Pass


# Deleting a column using drop()
# We use drop() to remove a column.
#df.drop("Marks", axis=1)#axis 1 = column




#sorting
df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John"],
    "Marks": [80, 45, 90]
})
print(df.sort_values("Marks", ascending=False))#for getting the sorted values in descending values



df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John", "Ravi"],
    "Marks": [80, 80, 90, 80],
    "Age": [22, 20, 21, 19]
})

print(df.sort_values(["Marks", "Age"]))
# First, sort by Marks in ascending order.
# If marks are equal, sort by Age in ascending order.


# sort_index() sorts the index labels in ascending order by default.
#df.sort_index(axis=1)
# axis=0 → sort row index labels.
# axis=1 → sort column labels.
# ascending=True → alphabetical order (A to Z).


#ffill() means Forward Fill. It fills a missing value using the previous available value.
#Example: [80, NaN, 90] becomes [80, 80, 90].
#bfill() means Backward Fill. It fills a missing value using the next available value.
#Example: [80, NaN, 90] becomes [80, 90, 90].

#dropna() drops the missing values in the data

#df.dropna(how="all")
#how="any" → remove if at least one value is missing.
#how="all" → remove only if all values are missing.


# #DataFrame creation and properties
# Row and column selection (loc, iloc)
# Filtering (isin, between, query)
# Adding, updating and deleting rows/columns
# Sorting (sort_values, sort_index)
# Missing values (isnull, fillna, dropna)@topics we covered upto now


#apply() on a DataFrame column
# We can apply a function to every value in a column.
df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John"],
    "Marks": [80, 45, 90]#output : marks became 85 ,50,95
})

df["Marks"] = df["Marks"].apply(lambda x: x + 5)


#map()
# map() is useful for transforming values in a Series, such as replacing category names.
df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John"],
    "Grade": ["A", "B", "A"]#output : Excellent , Good ,Excellent
})

df["Grade"] = df["Grade"].map({
    "A": "Excellent",
    "B": "Good"
})

#replace()
# replace() replaces specific values in a Series or DataFrame.
df = pd.DataFrame({
    "Name": ["Ram", "Sam", "John"],
    "Grade": ["A", "B", "A"]
})

df["Grade"] = df["Grade"].replace("A", "Excellent")
# #output :
# Ram	Excellent
# Sam	B
# John	Excellent

# map() → maps values using a function or dictionary.
# replace() → replaces specified values.
# apply() → applies a function to values.

#value_counts()
# value_counts() counts how many times each unique value appears.
df = pd.DataFrame({
    "Grade": ["A", "B", "A", "C", "B", "A"]
})

print(df["Grade"].value_counts())
#output : 
# A    3
# B    2
# C    1

# groupby() introduction
# groupby() groups rows based on a common value.

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [30000, 20000, 40000, 25000]
})
df.groupby("Department")["Salary"].sum()
#output:
# Department
# HR    45000
# IT    70000

#aggregate functions
# sum()	Total
# mean()	Average
# count()	Number of non-missing values
# min()	Minimum
# max()	Maximum
# median()	Middle value



#Multiple aggregations using agg() -> when we want to use multiple aggregate functions at a time 
df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "max", "min", "count"]
)


# # as_index:
# With as_index=False, the Department remains a normal column instead of becoming the index.


# reset_index()
# Sometimes after grouping, we want to convert the index back into a normal column.

#updating:
#.loc[] uses index labels, not necessarily row positions.
# df.loc[1, "City"] = "Hyderabad"
# df.loc[df["Marks"] < 40, "Result"] = "Fail" for updating multiple rows
#for columns df.loc[0, ["Marks", "City"]] = [95, "Delhi"]


#Inserting a column at a specific position:
df.insert(1, "Age", [20, 21, 22])
# 1 → position where the column should be inserted.
# "Age" → new column name.
# [20, 21, 22] → column values.


# Removing rows using a condition:
df = df[df["Marks"] >= 40]
#This keeps only students whose marks are 40 or above. Students scoring below 40 are excluded.

#for deleting with using index df.drop(index=[1, 3])

# df.drop(index=[...]) → removes rows.
# df.drop(columns=[...]) → removes columns.


#drop() using a condition:
#df.drop(df[df["Marks"] < 40].index)
