import pandas as pd
import numpy as np

# Create DataFrame with missing values
df = pd.DataFrame({"a": list(range(4)), "b": list("ab.."), "c": ["a", "b", np.nan, "d"]})

# Display the original DataFrame with missing values
print("Original DataFrame:\n",df)

# Replace the missing values with regular exp
result = df.replace(r"\.", 10, regex=True)

print("\nResultant DataFrame after filling the missing values using regex:\n", result)