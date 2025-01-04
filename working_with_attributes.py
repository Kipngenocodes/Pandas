'''
        Working with Attributes in Pandas
Attributes in Pandas allow you to access metadata about your Series and DataFrame objects.
By using these attributes you can explore and easily understand the data.'''


# Example
# Let's create a Pandas Series and explore these attributes operation.
import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(5))
# Exploring attributes
print("Data type of Series:", s.dtype)
print("Index of Series:", s.index)
print("Values of Series:", s.values)
print("Shape of Series:", s.shape)
print("Number of dimensions of Series:", s.ndim)
print("Size of Series:", s.size)
print("Is Series empty?:", s.empty)