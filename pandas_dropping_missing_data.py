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

'''
Syntax:
DataFrame.dropna(*, axis=0, how=<no_default>, 
thresh=<no_default>, subset=None, inplace=False, ignore_index=False)

where:
    axis: 0 or 'index' (default) to drop rows; 1 or 'columns' to drop columns.
    how: By default it is set to 'any', which drops that row or column if any missing values are present. If set to 'all', then it drops that row or column if all the missing values.
    thresh: Require a minimum number of non-NA values to retain the row or column.
    subset: List of specific columns (if dropping rows) or rows (if dropping columns) to consider.
    inplace: Modify the DataFrame in place (default is False).
    ignore_indexReset the index of the result (default is False).
'''


