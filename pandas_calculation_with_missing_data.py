import  pandas as pd
import  numpy as np

'''
When performing arithmetic operations between Pandas objects, 
missing values (NaN) are propagated by default. For example, when you add two series with NaN values, 
the result will also have NaN wherever there was a missing value in any of series.'''

# Creating a dataframe with 5 rows and 3 columns with missing values
df = pd.DataFrame(np.random.randint(0,100,size=(5, 3)), columns=list('ABC'))
df.loc[0,'A'] = np.nan
df.loc[1,'B'] = np.nan
df.loc[2,'C'] = np.nan
# Create another dataframe with 5 rows and 3 columns with missing values
df2 = pd.DataFrame(np.random.randint(0,100,size=(5, 3)), columns = list('ABC'))
df2.loc[2,'A'] = np.nan
df2.loc[3,'B'] = np.nan

# Output the dataframe
print(df)
print('\n a new dataframe \n ', df2)

result = df + df2
print("\nResult of adding df and df2:\n", result)