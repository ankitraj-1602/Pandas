# What is a Series?
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

import pandas as pd

arr=[1,2,3,'ankit',False]
ser = pd.Series(arr)
print(ser)

# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.

print(ser[0])

# Create Labels
# With the index argument, you can name your own labels.

ser = pd.Series(arr,index=['a','b','c','d','e'])
print(ser)

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

calories = {"day1": 420, "day2": 380, "day3": 390}
ser = pd.Series(calories)
print(ser)

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

ser = pd.Series(calories,index=['day1','day2'])
print(ser)

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)