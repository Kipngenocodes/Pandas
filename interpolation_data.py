import pandas as pd
import numpy as np

# create a dataframe with 5 columns and 5 rows with random data and missing values
df = pd.DataFrame(np.random.randint(0,100,size=(5, 5)), columns=list ('ABCDE'))
df.loc[1, 'B'] = np.nan
df.loc[2, 'C'] = np.nan
df.loc[3, 'D'] = np.nan
df.loc[4, 'E'] = np.nan

# Output the dataframe
print( df)

# Using the  interpolate() method
result = df.interpolate()
print(result)