import pandas as pd
import numpy as np
'''
The pandas library offers tools like the HDFStore class 
and read/write APIs to easily store, retrieve, 
and manipulate data while optimizing memory usage and retrieval speed.
HDF5 is stands for Hierarchical Data Format version 5,
is an open-source file format designed to store large, complex,
and heterogeneous data efficiently. 
It organizes the data in a hierarchical structure similar to a file system,
with groups acting like directories and datasets functioning as files.
HDF5 file format can store different types of data
(such as arrays, images, tables, and documents) in a hierarchical structure,
making it ideal for managing heterogeneous data.
'''

# create a store using the HDF5 Class
store = pd.HDFStore('data.h5')
# Displaying the store 
print(store)
# Closing the store before use
store.close()