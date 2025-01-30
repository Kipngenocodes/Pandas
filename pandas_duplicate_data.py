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
'''
Pandas DataFrame.duplicated() method is used to identify duplicate rows in a DataFrame.
    False: The row is not a duplicate (i.e., it's the first occurrence).
    True: The row is a duplicate of another row in the DataFrame.
'''

# finding duplicate rows in the dataframe
results = df.duplicated()

# output the results 
print('\n Showing the duplicates in dataframe\n', results)