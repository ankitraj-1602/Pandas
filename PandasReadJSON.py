# Read JSON
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

import pandas as pd
json = pd.read_json("data.json")
print(json)
print(json.to_string()) #to print entire data set