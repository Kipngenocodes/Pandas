import pandas as pd
import numpy as np

# Create a dataframe
df = pd.DataFrame({
    'A': ['A0', 'A0', 'A1', 'A2', 'A2', 'A3', 'A3', 'A3', 'A4', 'A4', 'A4', 'A4'],
    'B': ['B0', 'B1', 'B1', 'B2', 'B2', 'B3', 'B3', 'B3', 'B4', 'B4', 'B4', 'B4'],
    'C': ['C0', 'C0', 'C0', 'C1', 'C1', 'C2', 'C2', 'C2', 'C3', 'C3', 'C3', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3', 'D3', 'D4', 'D4', 'D4', 'D4', 'D4', 'D4', 'D4']
})

# Display the DataFrame
print(df)

# Count unique elements in each column
unique_counts = df.nunique()
print("Number of unique elements in each column:")
print(unique_counts)

# Get unique elements in column 'A'
unique_A = df['A'].unique()
print("Unique elements in column 'A':")
print(unique_A)

# Get unique elements in column 'B'
unique_B = df['B'].unique()
print("Unique elements in column 'B':")
print(unique_B)

# Count Unique Values using the value_counts()
# Count the frequency of unique values in column 'B'
result = df['B'].value_counts()

print('\nThe unique values:')
print(result)

# Checking for the unique values in column 'C'
result = df['C'].value_counts()
print('\nThe unique values:')
print(result)