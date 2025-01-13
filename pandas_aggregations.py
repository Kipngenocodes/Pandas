import pandas as pd
import numpy as np

'''
Aggregating data is a key step in data analysis, especially when dealing with large datasets. In Pandas,
you can perform aggregations using the DataFrame.agg() method,
This method is flexible, enabling various operations that summarize and analyze your data. 
Aggregation operations in Pandas can be applied to either the index axis (default) or the column axis.

The DataFrame.agg() method (an alias for aggregate) is a powerful tool
that allows you to apply one or more aggregation functions to a DataFrame,
either across rows or columns, providing a summary of the data.
'''

# syntax : df.agg([func1, func2, ...], axis=0)
# axis=0 is default, it means it will be applied on columns
# axis=1 means it will be applied on rows
# you can also use axis='index' or axis='columns' for clarity
# you can also use axis=None for clarity

# create a dataframe 
df = pd.DataFrame([[1, 2, 3, 1],
                   [4, 5, 6, np.nan],
                   [7, 8, 9, 2],
                   [np.nan, 2, np.nan, 3]],
   index = pd.date_range('1/1/2024', periods=4),
   columns = ['A', 'B', 'C', 'D'])

print("Input DataFrame:\n",df)
result = df.agg(['sum', 'min'])
print("\nResults:\n",result)