import pandas as pd
import numpy as np
'''
A DataFrame in Python's pandas library is a two-dimensional labeled data structure
that is used for data manipulation and analysis. 
It can handle different data types such as integers, floats, and strings.
Each column has a unique label, 
and each row is labeled with a unique index value, which helps in accessing specific rows.
DataFrame is used in machine learning tasks which allow the users
to manipulate and analyze the data sets in large size.
It supports the operations such as filtering, sorting, merging, grouping and transforming data.'''

'''
Creating a DataFrame suing constructor:
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
A pandas DataFrame can be created using various inputs like:
        Lists
        Dictionary
        Series
        Numpy ndarrays
        Another DataFrame
        External input iles like CSV, JSON, HTML, Excel sheet, and more.
'''
# create an empty DataFrame
df = pd.DataFrame()
print(df)

# create a DataFrame from a list
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data, columns=['A'])
print(df)

'''
Create a DataFrame from Dict of ndarrays / Lists
All the ndarrays must be of same length. If index is passed, 
then the length of the index should equal to the length of the arrays.
If no index is passed, then by default, index will be range(n), 
where n is the array length.
'''
data = {'A': [1, 2, 3, 4, 5],  'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)
print(df)

'''
Create a DataFrame from List of Dicts
List of Dictionaries can be passed as input data to create a DataFrame.
The dictionary keys are by default taken as column names.
'''
data = [{'A': 1, 'B': 2}, {'A': 5, 'B': 10, 'C': 20}]
df = pd.DataFrame(data)
print(df)

'''
Create a DataFrame from Dict of Series
Dictionary of Series can be passed to form a DataFrame. 
The resultant index is the union of all the series indexes passed.'''

data = {'A': pd.Series([1, 2, 3]), 'B': pd.Series([4, 5, 6])}
df = pd.DataFrame(data)
print(df)
