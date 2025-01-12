import pandas as pd
import numpy as np


'''
These functions relate to the Series index and provide ways to manipulate and analyze index labels −
1	idxmax(): Returns the index of the first occurrence of the maximum value.
2	idxmin() :Returns the index of the first occurrence of the minimum value.
3	value_counts() :Returns a Series containing counts of unique values.
4	unique(): Returns an array of unique values in the Series elements.
'''

# create a series 
s = pd.Series([ 3, 4, 9, 6, 7, 8, 9, 1])

# output the series 
print("\n Series: \n", s)
# create a dataframe with a series as one of its columns
df = pd.DataFrame({'A': [90, 30, 59, 67, 768, 27, 647, 78],
    'B': s,  # Include the Series as one of the columns
    'C': [10, 20, 30, 40, 50, 60, 70, 80],
    'D': [5, 15, 25, 35, 45, 55, 65, 75],
    'E': ['X', 'Y', 'Z', 'W', 'V', 'U', 'T', 'S']
})

# print the dataframe
print('\n DataFrame: \n', df)

# Returns the index of the first occurrence of the maximum value
print('\n Maximum value index: \n', df['B'].idxmax())
print('\n Maximum value index: \n', df['D'].idxmax())

# Returns the index of the first occurrence of the minimum value 
print('\n Minimum value index: \n', df['B'].idxmin())
print('\n Minimum value index: \n', df['D'].idxmin())

# Returns the index of the first occurrence of the unique value
print('\n Unique value index: \n', df['E'].unique())
print('\n unique value index: \n', df['D'].unique())
