import pandas as pd
import numpy as np

'''
Stacking and unstacking in Pandas are the useful techniques for 
reshaping DataFrames to extract more information in different ways. 
It works efficiently with multi-level indices also. 
Whether it's compressing columns into row levels or expanding rows into columns, 
these operations are crucial for handling complex datasets.
Pandas library provides two main methods for this stacking and 
unstacking operations which are stack() and unstack().'''

# Create MultiIndex
tuples = [["x", "x", "y", "y", "", "f", "z", "z"],["1", "2", "1", "2", "1", "2", "1", "2"]]

index = pd.MultiIndex.from_arrays(tuples, names=["first", "second"])

# Create a DataFrame
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

# Display the input DataFrame
print('Input DataFrame:\n', df)

# Stack columns
stacked = df.stack()
print('\nOutput Reshaped DataFrame:\n', stacked)