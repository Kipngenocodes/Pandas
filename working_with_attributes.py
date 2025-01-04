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

'''
Attribute & Description
1. dtype: Returns the data type of the elements in the Series or DataFrame.
2. index: Provides the index (row labels) of the Series or DataFrame.
3. values: Returns the data in the Series or DataFrame as a NumPy array.
4. shape: Returns a tuple representing the dimensionality of the DataFrame (rows, columns).
5. ndim: Returns the number of dimensions of the object. Series is always 1D, and DataFrame is 2D.
6. Size:Gives the total number of elements in the object.
7. Empty:Checks if the object is empty, and returns True if it is.
8. Name:Returns the name of the Series or DataFrame.'''

# Example of DataFrame object
import pandas as pd
import numpy as np

# Create a DataFrame with random numbers
df = pd.DataFrame(np.random.randn(3, 4), columns=list('ABCD'))
print("DataFrame:")
print(df)

print("Results:")
print("Data types:", df.dtypes)
print("Index:", df.index)
print("Columns:", df.columns)
print("Values:")
print(df.values)
print("Shape:", df.shape)
print("Number of dimensions:", df.ndim)
print("Size:", df.size)
print("Is empty:", df.empty)
