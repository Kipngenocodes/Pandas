import pandas as pd
import numpy as np

# Creating a pandas DataFrame
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

df = pd.DataFrame(data)

# Convert the 'Name' column to a categorical type
df['Name'] = df['Name'].astype('category')

print("Original DataFrame: \n", df)

# Convert the categorical 'Name' column into an ordered categorical type
df['Name'] = df['Name'].cat.as_ordered()

print("\nDataFrame after converting 'Name' to ordered categorical: \n", df)

# Demonstrate sorting by the ordered categorical column
sorted_df = df.sort_values(by='Name')
print("\nSorted DataFrame by 'Name': \n", sorted_df)