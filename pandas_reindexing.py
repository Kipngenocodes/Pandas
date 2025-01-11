import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
Reindexing is a powerful and fundamental operation in Pandas that
allows you to align your data with a new set of labels. 
Whether you're working with rows or columns,
reindexing gives you control over how your data aligns with the labels you specify.
Reindexing in Pandas refers to the process of conforming your data to match a new
set of labels along a specified axis (rows or columns). This process can accomplish several tasks −
    Reordering: Reorder the existing data to match a new set of labels.
    Inserting Missing Values: If a label in the new set does not exist in the original data, 
    Pandas will insert a missing value (NaN) for that label.
    Filling Missing Data: You can specify how to fill in missing values that result from reindexing, 
    using various filling methods.
It allows you to modify the row and column labels of Pandas data structures.
'''
# The reindex() method is the primary tool for performing reindexing in Pandas.
# It allows you to modify the row and column labels of Pandas data structures.

# reindexing a pandas series
new_series = pd.Series([1, 2, 3, 4, 5, 6, ], index=['a', 'b', 'c', 'd', 'e', 'f'])

# print the original series
print("Original Series:\n ", new_series)

s_indexed = new_series.reindex(['b', 'a', 'f', 'd', 'c', 'e'])
# print the reindexed series
print("Reindexed Series:\n ", s_indexed)