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


'''
Exploring Basic Methods in Pandas
Pandas offers several basic methods in both the data structures, 
that makes it easy to quickly look at and understand your data.
These methods help you get a summary and explore the details without much effort.'''

'''
Method & Description
1. head(n):Returns the first n rows of the object. The default value of n is 5.
2. tail(n):Returns the last n rows of the object. The default value of n is 5
3. info():Provides a concise summary of a DataFrame, including the index dtype and column dtypes, 
non-null values, and memory usage.
4. describe():Generates descriptive statistics of the DataFrame or Series, such as count, mean, std, min, and max.
5. max():Returns the maximum value in the DataFrame or Series.'''

# creating a series and see workingof series basic methods
import pandas as pd
import numpy as np

# create a series with random numbers
s = pd.Series(np.random.randn(10))
print("Series:")
print(s)

# Using basic methods
print('first 5 rows of the series:', s.head())
print('last 5 rows of the series:', s.tail())
print("description of the series:", s.describe())
print("maximum value in the series:", s.max())
print("minimum value in the series:", s.min())
print("information of the series:", s.info())


# example and understand working of the basic methods on a DataFrame object.
import pandas as pd
import numpy as np

#Create a Dictionary of series
data = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]), 
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
 
#Create a DataFrame
df = pd.DataFrame(data)
print("Our data frame is:\n")
print(df)

# Using basic methods
print("\nFirst 5 rows of the DataFrame:\n", df.head())
print("\nLast 3 rows of the DataFrame:\n", df.tail(3))
print("\nInfo of the DataFrame:")
df.info()
print("\nDescriptive statistics of the DataFrame:\n", df.describe())
