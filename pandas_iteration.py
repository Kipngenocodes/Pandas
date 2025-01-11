import pandas as pd
import numpy as np

'''
The iteration behavior in pandas varies between Series and DataFrame objects −
    Series: Iterating over a Series object yields the values directly, 
            making it similar to an array-like structure.
    DataFrame: Iterating over a DataFrame follows a dictionary-like convention,
                where the iteration produces the column labels (i.e., the keys).
To iterate over the rows of the DataFrame, we can use the following methods −
    items(): to iterate over the (key,value) pairs
    iterrows(): iterate over the rows as (index,series) pairs
    itertuples(): iterate over the rows as namedtuples
'''

# Iterate Over Column Pairs
'''
The items() method allows you to iterate over each column as a key-value pair, 
with the label as the key and the column values as a Series object. 
This method is consistent with the dictionary-like interface of a DataFrame
'''
# creating a dataframe
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19],
        'Score': [90, 85, 88],
        'Grade': ['A', 'B', 'C'],
        'Address': ['New York', 'Los Angeles', 'Chicago'],
        }



# printing the original dataframe
df = pd.DataFrame(data)
print(df)

# Iterate Through DataFrame rows
print("Iterated Output:")
for key,value in df.items():
   print(key,value)

print('\n')
# iterating over the rows of the DataFrame using iterrows()
for row_index,row in df.iterrows():
   print(row_index,row)