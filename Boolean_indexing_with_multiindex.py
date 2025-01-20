import pandas as pd
import numpy as np

# Explanation of MultiIndexed DataFrames
'''
Pandas MultiIndexed objects allow you to apply boolean indexing 
to filter data based on conditions. 
It creates a mask and applies it to the DataFrame.
'''

# Creation of MultiIndex object
index = pd.MultiIndex.from_tuples([
    ('A', 'x'), ('A', 'y'), 
    ('B', 'x'), ('B', 'y'),
    ('C', 'x'), ('C', 'y'),
    ('D', 'x'), ('D', 'y')
])

# Create a DataFrame with random data
df = pd.DataFrame(
    np.random.randint(0, 100, size=(8, 4)),  # Matching rows with the index
    index=index,
    columns=list('ABCD')
)

# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n', df)


# Select data based on the boolean indexing
print('\n Selected data:')   
mask = df['D'] > 75

print(df[mask])