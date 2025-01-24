import pandas as pd
import numpy as np
import datetime

''''
Pivoting in Python Pandas is a powerful data transformation
technique that reshapes data for easier analysis and visualization.
It change the data representation from a "long" format to a "wide" format,
making it simpler to perform aggregations and comparisons.'''

# Creating a Dataframe
df = pd.DataFrame({"Col1": range(12),"Col2": ["A", "A", "A", "B", "B","B", "C", "C", "C", "D", "D", "D"],
"date": pd.to_datetime(["2024-01-03", "2024-01-04", "2024-01-05"] * 4)})

# output the  following dataframe:
print('\n Original DataFrame:\n', df)

# Pivoting the Dataframe with pivot()
pivoted_df =  df.pivot(index="date", columns="Col2", values="Col1")

# Display the output
print('\nPivoted DataFrame:\n', pivoted_df)

'''
The pivot() method requires that the index and columns specified have unique values. 
If your data contains duplicates, you should use the pivot_table() method instead.
'''
# Creating a Dataframe with duplicate values and  pivoting it
df = pd.DataFrame({"A": [1, 1, 2, 3] * 6,
"B": ["A", "B", "C"] * 8,
"C": ["x", "x", "x", "y", "y", "y"] * 4,
"D": np.random.randn(24),
"E": np.random.randn(24),
"F": [datetime.datetime(2013, i, 1) for i in range(1, 13)] +[datetime.datetime(2013, i, 15) for i in range(1, 13)]})

# Display the Input DataFrame
print('\nOriginal DataFrame:\n', df)

# Pivot the DataFrame
pivot_table = pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])

# Display the output
print('\nPivoted DataFrame:\n', pivot_table)