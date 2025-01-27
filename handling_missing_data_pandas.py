import pandas as pd
import numpy as np

# Create a DataFrame with 20 rows and 5 columns
data = np.random.randn(20, 5)
index = pd.date_range('1/1/2000', periods=20)
columns = ['A', 'B', 'C', 'D', 'E']
df = pd.DataFrame(data, index=index, columns=columns)

# Output the original DataFrame
print("Original DataFrame:")
print(df)

# Reindexing the DataFrame with new index values
# Note: The new index values must be compatible with the original index (e.g., dates)
new_index = pd.date_range('1/1/2000', periods=25)  # Adding 5 more dates
new_df = df.reindex(new_index)

# Output the DataFrame after reindexing
print("\nDataFrame after reindexing (introducing missing values):")
print(new_df)

# Fill missing values with 0
filled_df = new_df.fillna(0)

# Output the DataFrame after filling missing values
print("\nResultant DataFrame after NaN replaced with '0':")
print(filled_df)

# Dropping the missing values 
dropped_df = new_df.dropna()
# Output the DataFrame after dropping missing values
print(dropped_df)