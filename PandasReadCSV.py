# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

import pandas as pd
csv = pd.read_csv('data.csv')
print(csv.to_string()) #to_string() to print entire dataframe
print(csv)

# max_rows
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.

print(pd.options.display.max_rows)

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

# can update this number
pd.options.display.max_rows = 9999