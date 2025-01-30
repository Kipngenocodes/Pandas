import pandas as pd
import numpy as np

'''
Working with Duplicate data in pandas
The Python Pandas library offers two primary methods duplicated() and drop_duplicates() 
for managing the duplicated data efficiently.'''

# Identifying Duplicates in a DataFrame
# Create a dataframe with a duplicate data in it
df = pd.DataFrame({ 'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
                   'Age': [20, 21, 19, 20, 19],
                   'Score': [90, 85, 88, 90, 88]})
# Output original dataframe
print("Original DataFrame:\n", df)