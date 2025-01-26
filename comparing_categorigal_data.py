import pandas as pd
from pandas.api.types import CategoricalDtype

# Comparing categorical data
'''
Equality comparison (== and !=).
All comparisons (==, !=, >, >=, <, and <=).
Comparing categorical data to a scalar value.
Comparing categorical data is an essential task for getting insights 
and understanding the relationships between different categories of the data.
'''

# Non-equality comparisons between categorical data with different categories 
# between a categorical Series and a list-like object will raise a TypeError. 

# Creating categorical series for equality comparison
data1 = ['3', '2', '1', '1', '2', '2', '3', '2', '1', '4', '2', '2', '5', '4']
series1 = pd.Series(data1).astype(CategoricalDtype(categories=['1', '2', '3', '4', '5'], ordered=True))

# Creating another categorical Series for comparison
data2 = ['2', '4', '3', '1', '2', '1', '4', '3', '1', '4', '1', '2', '5', '4']  # Same length as data1
series2 = pd.Series(data2).astype(CategoricalDtype(categories=['1', '2', '3', '4', '5'], ordered=True))

# Equality comparison
print("Equality comparison (series1 == series2):")
print(series1 == series2)

# Inequality comparison
print("\nInequality comparison (series1 != series2):")
print(series1 != series2)

# Greater than comparison (works because categories are ordered)
print("\nGreater than comparison (series1 > series2):")
print(series1 > series2)

# Less than comparison (works because categories are ordered)
print("\nLess than comparison (series1 < series2):")
print(series1 < series2)

# Comparing categorical data to a scalar value
print("\nComparison with scalar value (series1 > '2'):")
print(series1 > '2')

# Creating another categorical Series for comparison
data3 = ['2', '2', '2', '1', '1', '3', '1', '2', '1', '4', '2', '2', '5', '4']  # Same length as data1
series3 = pd.Series(data3).astype(CategoricalDtype(categories=['1', '2', '3', '4', '5'], ordered=True))

# Attempting to compare differently ordered two Series objects
try:
    print("\nAttempting to compare differently ordered two Series objects:")
    print(series1 > series3)
except ValueError as e:
    print("ValueError:", str(e))