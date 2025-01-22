import pandas as pd

'''
Filtering data based on the index values of the DataFrame can be possible by creating the mask for the index, 
so that you can select rows based on their position or label.
'''
# Create a DataFrame with index values
df = pd.DataFrame({'A1': [10, 20, 30, 40, 50], 'A2':[9, 3, 5, 3, 2]
}, index=['a', 'b', 'c', 'd', 'e'])

# Dispaly the Input DataFrame
print('Original DataFrame:\n', df)

# Define a mask based on the index
mask = df.index.isin(['e', 'd'])

# Apply the mask
filtered_data = df[mask]

print('Filtered Data:\n',filtered_data)
