import pandas as pd
import numpy as np

# create a multindex array 
my_arrays = [["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
["one", "two", "one", "two", "one", "two", "one", "two"]]

# create a list of tuples from array 
my_tuples = list(zip(*my_arrays))

# Creating a MultiIndex from tuples
index = pd.MultiIndex.from_tuples(my_tuples, names=["first", "second"])

# Creating a Series with MultiIndex
s = pd.Series([2, 3, 1, 4, 6, 1, 7, 8], index=index)
print("MultiIndexed Series:\n", s)

# Indexing the MultiIndexed Series using .loc[]
print("\nSelecting data at index ('baz', 'one') and column 'A':")
print(s.loc[('bar', 'one')])