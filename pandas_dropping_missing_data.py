import pandas as pd
import numpy as np


'''
Missing data is a common issue when working with real-world datasets. 
The Python Pandas library provides an easy way for removing rows or columns
that contain missing values (NaN or NaT) from a dataset using the dropna() method.
'''
# Create a dataframe with random data and include missing data 
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list ('ABCD'))
df.loc[10:20, 'A'] = np.nan
df.loc[30:40, 'B'] = np.nan
df.loc[50:60, 'C'] = np.nan
df.loc[70:80, 'D'] = np.nan

# output the dataframe
print('\n Original Dataframe: \n', df)