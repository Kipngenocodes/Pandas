import pandas as pd
import numpy as np

'''
When you need to apply a function to each element individually, you can use map() function.
These methods are particularly useful when the function cannot be vectorized.
'''

# Create a sample DataFrame with 7 by 7 matrix
df = pd.DataFrame(np.random.randint(0, 100, size=(7, 7)), columns=[f'Col_{i}' for i in range(1, 8)])
print("Original DataFrame:\n", df)

# Applying a function to each element individually using map()
def square(x):
    return x ** 2


df_map = df.map(square)
print("\nDataFrame after applying map():\n", df_map)
