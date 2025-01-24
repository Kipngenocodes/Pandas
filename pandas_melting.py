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

'''
Melting with wide_to_long()
The pandas wide_to_long() function provides more control over the transformation. 
It's useful when your columns have a structured naming pattern that includes a suffix.
'''
# Creating a  dataframes
df = pd.DataFrame({'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
'ht1': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
'ht2': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]})

# Display the input DataFrame
print('Input DataFrame:\n', df)

# Melt the DataFrame using wide_to_long()
long_df = pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age')

print('Output Long Melted DataFrame:\n', long_df)