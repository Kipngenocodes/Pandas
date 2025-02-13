import pandas as pd
import numpy as np


# Filling the missing data 
''' Filling missing data is a process of replacing the missing (NaN) values with meaningful alternatives.
        Replacing missing values with a scalar.
        Forward and backward filling.
        Using a specified limit for filling.
        Replacing Data with the replace() method.
        Replacing values with regular expressions.
'''
# Creating a dataframe 
data = {'Name': ['Tom', 'Nick', 'John', np.nan],
        'Age': [20, 21, 19, np.nan],
        'Score': [90, 85, 88, np.nan]}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'], columns=['Name', 'Age', 'Score'])
print("Original DataFrame:\n", df)
# Replacing missing values with a scalar
'''
The fillna() method in Pandas is used to fill missing values (NA or NaN) with a scalar value,
such as any specific number.'''
# df.fillna(0, inplace=True)
# print("\nDataFrame after replacing missing values with 0:\n", df)

#  Forward and backward filling.
'''You can also propagate the last valid observation forward or backward to fill gaps using the ffill() and bfill() methods respectively.
        The ffill() method fills the missing values with the value from the previous row.	
        The bfill() method fills the missing values with the value from the next row.
'''
# Forward filling
df.ffill(inplace=True)
print("\nDataFrame after forward filling:\n", df)

# Backward filling
df.bfill(inplace=True)
print("\nDataFrame after backward filling:\n", df)