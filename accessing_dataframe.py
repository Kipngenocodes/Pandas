import pandas as pd
'''Pandas DataFrame slicing is a process of extracting specific rows, columns,
or subsets of data based on both position and labels.
DataFrame slicing uses the [] operator and 
specific slicing attributes like .iloc[] and .loc[] to retrieve data efficiently.

Pandas DataFrame slicing is performed using two main attributes, which are −
    iloc[]: For slicing based on position (integer-based indexing).
    loc[]: For slicing based on labels (index labels or column labels).
'''

'''
 Syntax for slicing a DataFrame by position: 
 DataFrame.iloc[row_start:row_end, column_start:column_end]'''

# Slicing DataFrame Rows by Position
# create a DataFrame
df =pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'])

# display the DataFrame
print("Original DataFrame:")
print(df)

# slicing the first two rows based on position
results = df.iloc[0:2, :]
print("\nSlicing the first two rows:")
print(results)

'''
Slicing a DataFrame by Label
The Pandas DataFrame.loc[] attribute
used to slice a DataFrame based on the labels of rows and columns.
syntax for slicing a DataFrame by label:
DataFrame.loc[row_label_start:row_label_end, column_label_start:column_label_end]
'''

# Create a DataFrame with labeled indices
df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']],
                  columns=['col1', 'col2'], index=['r1', 'r2', 'r3', 'r4'])

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Slice rows and columns by label
result = df.loc['r1':'r3', 'col1']
print("Output:")
print(result)

'''
Modifying Values After Slicing
After slicing a DataFrame, you can modify the sliced values directly.
This can be done by assigning new values to the selected elements.'''

# create a DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'])
# display the DataFrame
print("Original DataFrame:")
print(df)
# slicing and  modifying the values of the first two rows
df.iloc[0:2, :] = [[10, 20, 30], [40, 50, 60]]
print("\nDataFrame after modifying the first two rows:")
print(df)


