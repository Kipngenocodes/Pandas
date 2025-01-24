import pandas as  pd
import numpy as np
import datetime

''''
The Pandas pivot_table() method can be used to specify an aggregation function. 
By default it calculates the mean, but you can also use functions like sum, count,
or even custom functions for applying aggregation to the pivoting.
'''
# creating a dataframe  and pivoting it
df = pd.DataFrame({"A": [1, 1, 2, 3] * 6,
"B": ["A", "B", "C"] * 8,
"C": ["x", "x", "x", "y", "y", "y"] * 4,
"D": np.random.randn(24),
"E": np.random.randn(24),
"F": [datetime.datetime(2013, i, 1) for i in range(1, 13)] +[datetime.datetime(2013, i, 15) for i in range(1, 13)]})

# Display the Input DataFrame
print('Original DataFrame:\n', df)

# Pivot the DataFrame with a aggregate function
pivot_table = pd.pivot_table(df, values=["D", "E"], index=["B"], columns=["A", "C"], aggfunc="sum")

# Display the output
print('Pivoted DataFrame:\n', pivot_table)