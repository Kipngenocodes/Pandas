import pandas as pd
import numpy as np

# Creating a dataframe with 5 rows and 3 columns
data =  np.random.randn(5, 3)
index = ['a', 'b', 'c', 'd', 'e']
columns = ['x', 'y', 'z']
df = pd.DataFrame(data, index=index, columns=columns)

# output the dataframe 
print(df) 

Reindexing_df = df.reindex(index=['a', 'c', 'e', 'b', 'd'])

# Making a summation after reindexing the dataframe
print(Reindexing_df.sum())  # Output: x         -1.41421356