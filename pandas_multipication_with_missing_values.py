import pandas as pd
import numpy as np

'''
Calculating multipication with the missing data in pandas.
NAN is treated as a 1 in the process'''

# Create two sample dataframe
df1 = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, 6, 7, 8]})
df2 = pd.DataFrame({'A': [np.nan, 2, 3, 4 ], 'B': [5, 6, 7, 8]})

results =  df1.mul(df2, fill_value=1)

# Print the results
print(results)