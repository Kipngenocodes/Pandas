import pandas as pd
import numpy as np

'''
Ordered categorical data in Pandas have a meaning, 
and allowing you to perform certain operations like sorting, min(), max(), and
comparisons. Pandas will raise a TypeError when you try to apply min/max operations 
on unordered data. The Pandas .cat accessor provides
the as_ordered() method to convert a categorical data type into an ordered one.'''
# creating a pandas dataframe
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

df = pd.DataFrame(data).astype(pd.CategoricalDtype())
print("Original DataFrame: \n", df)

# Convert the categorical series into ordered using the .cat.as_ordered() method 
order_df = df.cat.as_ordered()
print("\nDataFrame after converting categorical series into ordered: \n", order_df)