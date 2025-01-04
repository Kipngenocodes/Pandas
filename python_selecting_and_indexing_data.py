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