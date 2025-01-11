import pandas as pd
import numpy as np

'''
Concatenation in Pandas refers to the process of joining
two or more Pandas objects (like DataFrames or Series) along a specified axis.
This operation is very useful when you need to merge data from different sources or datasets.
The primary tool for this operation is pd.concat() function, which can useful for Series, 
DataFrame objects, whether you're combining rows or columns. Concatenation in Pandas 
involves combining multiple DataFrame or Series objects either row-wise or column-wise.'''

# The pandas.concat() function is the primary method used for concatenation in Pandas.
# pandas.concat(objs, *, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=None)
# creating the first dataframe
df1 = pd.DataFrame({ 'Name': ['Tom', 'Nick', 'John', 'Peter', 'Jack',  'Sam', 'Rahul'],
                    'Age': [20, 21, 19, 18, 22,56, 73],
                    'City': ['New York', 'Paris', 'Berlin', 'London', 'Sydney', 'Tokyo', 'Mumbai'],
                    'Country': ['indonesia', 'Palau', 'Britain', 'Brazil', 'Australia', 'Japan', 'India']
})

df2 = pd.DataFrame({
    'Name': ['Alice', 'Emily', 'Chris', 'David', 'Sophia', 'Ethan', 'Priya'],
    'Age': [25, 24, 30, 35, 28, 60, 70],
    'City': ['Chicago', 'Madrid', 'Rome', 'Toronto', 'Melbourne', 'Seoul', 'Delhi'],
    'Country': ['USA', 'Spain', 'Italy', 'Canada', 'Australia', 'South Korea', 'India']
})

# Concatinating the two dataframes along the row axis (axis=0)
df_concat = pd.concat([df1, df2], axis=0)
print(df_concat)
print('\n')
# Concatenating with Keys to help differentiating between the two dataframes
df_concat_with_keys = pd.concat([df1, df2], keys=['df1', 'df2'])
print(df_concat_with_keys)

print('\n')
# Ignoring Indexes During Concatenation
print(pd.concat([df1,df2],keys=['x','y'],ignore_index=True))

print('\n')
# Concatenating Along Columns
df_concat_columns = pd.concat([df1, df2], axis=1)
print(df_concat_columns)