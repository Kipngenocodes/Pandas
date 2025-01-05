import pandas as pd
import numpy as np
'''
A Series in Pandas is a one-dimensional labeled array capable of holding data of any type,
including integers, floats, strings, and
Python objects. It consists of two main components −
        Data: The actual values stored in the Series.
        Index: The labels or indices that correspond to each data value.
'''
# series is similar to a one-dimensional array, list, 
# or column in a table but wit the lable called indices

''' creating a pandas series
class pandas.Series(data, index, dtype, name, copy)
'''
# Series can be created from a list, numpy array, scalar/ constant or dictionary

# creating an empty series
new_series = pd.Series()
# displaying the series result
print("Empty Series:", new_series)

# creating series from ndarray
data = np.array(['a', 'b', 'c', 'd'])
series = pd.Series(data)
print("Series from ndarray:\n", series)


# creating series from ndarray with index
data = np.array(['a', 'b', 'c', 'd'])
series = pd.Series(data, index=[101, 102, 103, 104])
print("Series from ndarray with index:\n", series)

# creating series from  dictionary
data = {'a': 0., 'b': 1., 'c': 2.}
series = pd.Series(data)
print("Series from dictionary:\n", series)

# creation of series from scalar
series = pd.Series(5, index=[0, 1, 2, 3])
print("Series from scalar:\n", series)