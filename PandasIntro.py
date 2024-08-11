# What is Pandas?
# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.

# Why Use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Relevant data is very important in data science.

# What Can Pandas Do?
# Pandas gives you answers about the data. Like:
# Is there a correlation between two or more columns?
# What is average value?
# Max value?
# Min value?
# Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

import pandas

myDataSet = {
    'cars':['BMW','Maruti','Ford'],
    'passings':[3,4,5]
}

myvar = pandas.DataFrame(myDataSet)
print(myvar)

# Now the Pandas package can be referred to as pd instead of pandas.

import pandas as pd

myDataSet = {
    'cars':['BMW','Maruti','Ford'],
    'passings':[3,4,5]
}

myvar = pd.DataFrame(myDataSet)
print(myvar)