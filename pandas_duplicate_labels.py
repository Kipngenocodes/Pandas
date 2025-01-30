import pandas as pd
import numpy as np


'''
If a dataset contains the repeated index labels then we call it as duplicated labels, 
it can lead to unexpected results in some operations such as filtering, aggregating, or slicing.
'''
# Create a DataFrame with duplicated index labels
df = pd.DataFrame({'A': [1, 2, 3], 'B': [ 4, 5, 6]}, index=[1, 1, 2])
print(df)

# Checking for duplicate labels 
'''
Use the pandas Index.is_unique attribute. 
If it returns False, then it means there are duplicate labels in your Index.
'''