import pandas as pd
import numpy as np

# Create DataFrame with missing values
df = pd.DataFrame([[9, -3, -2], [-5, 1, 8], [6, 4, -8]], 
index=['a', 'c', 'd'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'd', 'e', 'f'])

# Display the original DataFrame with missing values
print("Original DataFrame:\n",df)

# Forward Fill the missing values with limit
result = df.ffill(limit=1)
print("\nResultant DataFrame after Forward fill:\n", result)