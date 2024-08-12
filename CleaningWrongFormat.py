# Convert Into a Correct Format

# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:

import pandas as pd

df = pd.read_csv('data2.csv')

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# df['Date'] = pd.to_datetime(df['Date'])

print(df)

# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.

df.dropna(subset=['Date'], inplace = True)
print(df)