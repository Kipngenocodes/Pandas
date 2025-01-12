import pandas as pd
import numpy as np


'''
Transformation functions apply a mathematical
operation to each element in the Series, returning a transformed Series−
    1. diff() Computes the difference between elements in the object, over the specified number of periods.
    2. pct_change() : Computes the percentage change between the current and a prior element.
    3. rank() :computes the rank of values in the given object.
'''

# create a sample series
s = pd.Series([11, 22, 33, 44, 55])

# using diff() function
print(s.diff())  # Output: 11 11 11 11 11
# using pct_change() function
print(s.pct_change())  # Output: NaN 100.000000 100.000
# using rank() function
print(s.rank())  # Output: 1.0 2.0 3.0
