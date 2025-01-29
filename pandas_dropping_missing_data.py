import pandas as pd
import numpy as np


'''
Missing data is a common issue when working with real-world datasets. 
The Python Pandas library provides an easy way for removing rows or columns
that contain missing values (NaN or NaT) from a dataset using the dropna() method.
'''
# Create a dataframe with random data and include missing data 
df = pd.DataFrame(np.random.randint(0,20,size=(20, 4)), columns=list ('ABCD'))
df.loc[0:5, 'A'] = np.nan
df.loc[6:9, 'B'] = np.nan
df.loc[16:19, 'D'] = np.nan

# output the dataframe
print('\n Original Dataframe: \n', df)

# Dropping the missing values from the dataframe
df_dropped = df.dropna()
# output the dataframe
print('\n Dataframe after dropping missing values: \n', df_dropped)
