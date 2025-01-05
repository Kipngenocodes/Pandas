import pandas as pd
import numpy as np

'''
Pandas provides several methods for indexing and selecting data, such as −
    Label-Based Indexing with .loc
    Integer Position-Based Indexing with .iloc
    Indexing with Brackets []
'''

'''
            Label-Based Indexing with .loc
The .loc indexer is used for label-based indexing,
which means you can access rows and columns by their labels.
It also supports boolean arrays for conditional selection.
'''

# a basic example that selects all rows for a specific column using the loc indexer.
df = pd.DataFrame(np.random.randn(5, 4), index= range(1, 6), columns=list('ABCD'))


print("original DataFrame:\n",df)

# Selecting all rows for a specific column
print("\nSelecting all rows for column 'A':")
print(df.loc[:, 'A'])

# Example selecting all rows for multiple columns.
# import the pandas library and aliasing as pd

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select all rows for multiple columns, say list[]
print(df.loc[:,['A','C']])

# Example selects the specific rows for the specific columns.
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])

# Example selecting a range of rows for all columns using the loc indexer.
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print(df.loc['c':'e'])


'''
Integer Position-Based Indexing with .iloc
The .iloc indexer is used for integer-based indexing, which allows you to select rows and columns by their numerical position. 
This method is similar to standard python and numpy indexing (i.e. 0-based indexing).

Single Integer: Selects data by its position, e.g., df.iloc[0].
List of Integers: Select multiple rows or columns by their positions, e.g., df.iloc[[0, 1, 2]].
Integer Slicing: Use slices with integers, e.g., df.iloc[1:3].

Boolean Arrays: Similar to .loc, but for positions.
'''
#  Basic example that selects 4 rows for the all column using the iloc indexer.

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print("Original DataFrame:\n", df)

# select all rows for a specific column
print('\nResult:\n',df.iloc[:4])




