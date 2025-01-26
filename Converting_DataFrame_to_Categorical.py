import  pandas as pd
import  numpy as np

# Create a DataFrame 
df = pd.DataFrame({"Col_a": list("aeeioou"), "Col_b": range(7)})

# Display the Input DataFrame
print('Input DataFrame:\n',df)
print('Verify the Data type of each column:\n', df.dtypes)

# Convert the Data type of col_a to categorical
df['Col_a'] = df["Col_a"].astype("category")

# Display the Input DataFrame
print('Converted DataFrame:\n',df)
print('Verify the Data type of each column:\n', df.dtypes)