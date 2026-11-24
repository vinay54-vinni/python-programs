# Series in Pandas :
# A Series is a one-dimensional labelled data structure in Pandas.

# In simple words, a Series stores multiple values with their corresponding index labels.
#Vectorization means performing an operation on an entire collection of values without explicitly writing a loop.
# Think of it like a single column in Excel.
#Works with data in Python using Series and DataFrames, including data loaded from CSV, Excel, databases and other sources.

# For example:
# Index	Marks
# 0	     85
# 1	     90
# 2	     75
# 3	     95

# Creating series:
import pandas as pd

marks = pd.Series([85, 90, 75, 95])

print(marks)
# output:
# 0    85
# 1    90
# 2    75
# 3    95
# dtype: int64@it indicates about which type of data

import pandas as pd

marks = pd.Series(
    [85, 90, 75],
    index=["Rahul", "Priya", "Arun"]
)

print(marks)
#output:
# Rahul    85
# Priya    90
# Arun     75
# dtype: int64

# Series Arithmetic Operations:

import pandas as pd

marks = pd.Series([10, 20, 30, 40])

print(marks + 5)
# output:
# 0    15
# 1    25
# 2    35
# 3    45
# dtype: int64

# Accessing Multiple Values (Slicing):
import pandas as pd

marks = pd.Series([85, 90, 75, 95, 80])

print(marks[1:4])
# output:
# 1    90
# 2    75
# 3    95
# dtype: int64

#Using conditions:
import pandas as pd

marks = pd.Series([45, 80, 90, 35, 70])

print(marks[marks > 60])
#output:
# 1    80
# 2    90
# 4    70
# dtype: int64

# if we use marks>60 we get outptu in boolean 

# series functions:
import pandas as pd

marks = pd.Series([85, 90, 75, 95, 80])

print(marks.sum())
print(marks.mean())
print(marks.max())
print(marks.min())
print(marks.count())
print(marks.describe())

# # Handling Missing Values (NaN):
# NaN means Not a Number. In Pandas, it commonly represents a missing numerical value.
# we get outptu dtype in float cause Because the traditional NumPy-backed integer dtype cannot represent NaN directly, so Pandas converts the values to floating-point numbers.

import pandas as pd

marks = pd.Series([85, 90, None, 75, 95])

print(marks)
print(marks.isna())#if the vlaue is present we get false we get true
print(marks.isna().sum())#it count true values and give sum from above it is 1
print(marks.dropna())#fro dropping missing values

#Filling missing values:
import pandas as pd

marks = pd.Series([85, 90, None, 75, None])

result = marks.fillna(0)

print(result)
# #output:
# 0    85.0
# 1    90.0
# 2     0.0
# 3    75.0
# 4     0.0
# dtype: float64

# dropna()	Removes missing values
# fillna()	Replaces missing values

# Sorting a Series:
# sort_values() -Sorts based on values.
# sort_index() -Sorts based on index labels
import pandas as pd

marks = pd.Series([85, 60, 95, 70, 80])

print(marks.sort_values())#for sorting values
print(marks.sort_values(ascending=False))

#index:
import pandas as pd

s = pd.Series(
    [90, 80, 70],
    index=["C", "A", "B"]
)

print(s.sort_index())

# Unique Values and Duplicate Values:
import pandas as pd

marks = pd.Series([80, 90, 80, 70, 90, 100])

print(marks.unique())
print(marks.nunique())#output:4
print(marks.value_counts())
# #output:
# 80     2
# 90     2
# 70     1
# 100    1
# Name: count, dtype: int64

#for setting index values after sorting values:
import pandas as pd

s = pd.Series([40, 10, 30, 20])

result = s.sort_values().reset_index(drop=True)

print(result)

# Accessing Values using iloc and loc:
#iloc accesses values based on their numerical positions.
import pandas as pd

marks = pd.Series(
    [85, 90, 75],
    index=["Rahul", "Priya", "Arun"]
)

print(marks.iloc[0])#output:85
print(marks.iloc[1])#output:90

# #loc – Label Location
# loc accesses values using their actual index labels.
print(marks.loc["Priya"])#output:90

#Adding New Values to a Series:
# here we uses loc for adding values
import pandas as pd

marks = pd.Series(
    [85, 90, 75],
    index=["Rahul", "Priya", "Arun"]
)

marks.loc["Vinay"] = 95

print(marks)

#here we can also use concat for mixing two series 

# here w ecan use drop for deleting data 

#Converting Series into Python List and Dictionary:
import pandas as pd

marks = pd.Series([85, 90, 75, 95])

result = marks.tolist()#if we use .todict() it convert into dictionary

print(result)
print(type(result))

# #- .tolist() → converts values into a list.
# - .to_dict() → converts index labels and values into a dictionary

#get_loc("z") is used to get index position 

#head first five elements returns like head(3) first 3
#Tail returns last five like taile(3) last 3

import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s.memory_usage())
#Output will be a number of bytes
print(s.memory_usage(index=False))#onlycalculates the data memory

# s.memory_usage()	Values + index
# s.memory_usage(index=False)	Values only
# s.memory_usage(deep=True)	More detailed memory estimate

#is_unique – Checking Duplicate Values

#between() – Filtering Values Within a Range:
import pandas as pd

marks = pd.Series([35, 55, 65, 75, 85, 95])

result = marks.between(60, 90)
res = marks( marks.between(60, 90))#we get values in here
print(result)
# #output:
# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
# 5    False
# dtype: bool

# "both"	Includes both boundaries
# "neither"	Excludes both boundaries
# "left"	Includes left boundary only
# "right"	Includes right boundary only


#abs() converts negative into positive

#round:
# s.round()	Zero decimal places
# s.round(1)	One decimal place
# s.round(2)	Two decimal places

#clip() in Pandas Series
# The clip() method restricts values to a specified minimum and maximum.

# Values below the minimum become the minimum, and values above the maximum become the maximum.
import pandas as pd

s = pd.Series([10, 25, 50, 75, 100])

print(s.clip(20, 80))
#output:
# 0    20
# 1    25
# 2    50
# 3    75
# 4    80
# dtype: int64

#cumsum = cumulative sum (sum of all numbers)
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s.cumsum())
#output:
# 0     10
# 1     30
# 2     60
# 3    100 #cumsum is 40
# dtype: int64

#cummax :cummax() returns the maximum value seen so far at each position
import pandas as pd

s = pd.Series([10, 30, 20, 50, 40])

print(s.cummax())
#output:
# 0    10
# 1    30
# 2    30
# 3    50
# 4    50
# dtype: int64

#cummin() gives minimum numbers in the series it reverse to max
#cumprod()
import pandas as pd

s = pd.Series([2, 3, 4, 5])

print(s.cumprod())
#output:
# 0      2
# 1      6
# 2     24
# 3    120
# dtype: int64

#diff :diff() calculates the difference between the current value and the previous value
import pandas as pd

s = pd.Series([10, 25, 40, 30])

print(s.diff())
#OUTPUT:
#0     NaN
# 1    15.0
# 2    15.0
# 3   -10.0
# dtype: float64

#pct_change() in Pandas Series:pct_change() calculates the percentage change between the current value and the previous value
import pandas as pd

s = pd.Series([100, 120, 150])

print(s.pct_change() * 100)

# percentage change = (cureent-Previous/previous) it is normal formula if in ans they give *100 we want to multiply by 100
#  #ouput:
# 0     NaN
# 1    20.0
# 2    25.0
# dtype: float64

# shift() in Pandas Series
# shift() moves values up or down by a specified number of positions.
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s.shift(1))
#output:
# 0     NaN
# 1    10.0
# 2    20.0
# 3    30.0
# dtype: float64

# rank() in Pandas Series
# rank() assigns a rank to each value based on its position in sorted order.

import pandas as pd

s = pd.Series([50, 20, 80, 40])

print(s.rank()) #print(s.rank(ascending=False)) we get in reverse
#output:
# 0    3.0
# 1    1.0
# 2    4.0
# 3    2.0
# dtype: float64

#if we have any duplicate values we get 2.5 ,2.5 next value became skip like 3

#mode() in Pandas Series
# mode() returns the most frequently occurring value.

# mode() in Pandas Series
# mode() returns the most frequently occurring value.

import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])

print(s.quantile(0.5))#output 30 

# 0.5 means the 50th percentile.
# The 50th percentile is the median.
# The middle value here is 30.

# corr() — Correlation between Series
# corr() measures how two numerical Series are related.
# - 1 → Perfect positive correlation.
# - -1 → Perfect negative correlation.
# - 0 → No linear correlation.

import pandas as pd

a = pd.Series([10, 20, 30, 40])
b = pd.Series([20, 40, 60, 80])

print(a.corr(b))#output:1 cause the order is increasing rapidly 

# cov() — Covariance between Series
# cov() measures how two numerical Series vary together.
# - Positive covariance: values tend to increase together.
# - Negative covariance: one tends to increase when the other decreases.
# - Zero covariance: no linear co-variation.

import pandas as pd

a = pd.Series([10, 20, 30])
b = pd.Series([20, 40, 60])

print(a.cov(b))#output:200

# apply() in Pandas Series
# apply() allows us to apply a function to every value in a Series.
import pandas as pd

s = pd.Series([10, 20, 30])

result = s.apply(lambda x: x * 2)

print(result)
#output:
# 0    20
# 1    40
# 2    60
# dtype: int64


# map() in Pandas Series
# map() is used to transform each value using a dictionary, function, or another mapping.

import pandas as pd

s = pd.Series(["A", "B", "C"])

result = s.map({
    "A": "Apple",
    "B": "Banana",
    "C": "Cherry"
})

print(result)
#output:
# 0     Apple
# 1    Banana
# 2    Cherry
# dtype: object

# where() in Pandas Series
# where() keeps values that satisfy a condition and replaces values that don't satisfy it.
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s.where(s > 20))#if we want we can replace the value @ print(s.where(s > 20, 0))
#output:
# 0     NaN
# 1     NaN
# 2    30.0
# 3    40.0
# dtype: float64
# where() replaces values when the condition is False.

# mask() replaces values when the condition is True.

#replace() directly replaces specific values with new values
import pandas as pd

s = pd.Series([10, 20, 10, 30])#output 100,20,100,30
print(s.replace(10, 100))

# duplicated() in Pandas Series
# duplicated() checks whether a value has appeared before.
import pandas as pd
s = pd.Series([10, 20, 10, 30, 20])#it gives output in boolean values
print(s.duplicated())#for drop duplicates print(s.drop_duplicates())
#drop_duplicates() in Pandas Series
# drop_duplicates() removes repeated values and keeps only unique occurrences.

# na_position.

# It controls where missing values (NaN) appear when sorting.
import pandas as pd
s = pd.Series([30, None, 10, 20])
print(s.sort_values(na_position="first"))
#output:
# 1     NaN
# 2    10.0
# 3    20.0
# 0    30.0
# dtype: float64
# na_position="first"	NaN appears first
# na_position="last"	NaN appears last (default)
