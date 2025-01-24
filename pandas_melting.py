import pandas as pd
import numpy as np

# Python pandas  melting 
'''
Melting in Pandas is the process of converting a 
DataFrame from a wide format to a long format. 
In the wide format, data is spread across multiple columns. 
In simpler terms, it "unpivots" the DataFrame columns into rows,
and it is useful for visualizing and performing statistical analysis on datasets.'''

# Creating a dataframes 
dataframe = pd.DataFrame({ 'name': ['Tom', 'nick', 'krish', 'jack'],
                          'age': [20, 21, 19, 18],
                          'score': [90, 85, 88, 92],
                          'grade': ['A', 'B', 'C', 'D']})
print("\n Original DataFrame: \n", dataframe)

# Melting the DataFrame usuing melt() function
dataframe_melted = pd.melt(dataframe, id_vars=['name'], var_name='subject', value_name='marks')
print("\n Melted DataFrame: \n", dataframe_melted)