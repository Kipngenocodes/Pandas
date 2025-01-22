import pandas as pd
import numpy as np

# Creating a DataFrame
data = { 'Name': ['Tom', 'Nick', 'John', 'Peter'], 
        'Age': [20, 21, 19, 18],
        'Score': [90, 85, 88, 92] }
df = pd.DataFrame(data)

print(df)

'''
Boolean masking in Pandas is a useful technique to filter data based on specific conditions. 
It works by creating a boolean mask and applying it to a DataFrame or
Series to select data that meets the given condition. 
A boolean mask is a DataFrame or Series where each element is represented with either True or False.
When you apply this boolean mask to your data, 
it will select only the rows or columns that meet the defined condition.'''

# Create a boolean mask
mask = (df['Age'] > 20 ) | (df['Score'] > 90)
# Apply the boolean mask to the DataFrame
filtered_df = df[mask]

# Output the filtered DataFrame
print(filtered_df)