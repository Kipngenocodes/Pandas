import pandas as pd

# Create a DataFrame with duplicate column labels
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'A': [7, 8, 9]  # Duplicate column label 'A'
}

df = pd.DataFrame(data)

# Set the flag to disallow duplicate labels
df = df.set_flags(allows_duplicate_labels=False)

# Attempt to display the DataFrame
try:
    print(df)
except pd.errors.DuplicateLabelError as e:
    print(f"Error: {e}")