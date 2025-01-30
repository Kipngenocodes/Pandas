import pandas as pd
import numpy as np


'''
If a dataset contains the repeated index labels then we call it as duplicated labels, 
it can lead to unexpected results in some operations such as filtering, aggregating, or slicing.
'''
# Create a DataFrame with duplicated index labels
df = pd.DataFrame({'A': [1, 2, 3], 'B': [ 1, 2, 6]}, index=[1, 1, 2])
print(df)

# Checking for duplicate labels 
'''
Use the pandas Index.is_unique attribute. 
If it returns False, then it means there are duplicate labels in your Index.
'''
# Check if the row index is unique
print("Is row index is unique:",df.index.is_unique)  

# Check if the column index is unique
print('Is column index is unique:',df.columns.is_unique) 


# Detecting the duplicate labels
'''
The Index.duplicated() method is used to detect duplicates labels of Pandas object, 
it returns a boolean array indicating whether each label in the Index is duplicated.
'''
# Identify duplicated row labels
print('Duplicated Row Labels:', df.index.duplicated())