import  numpy as np
import  pandas as pd

# The HDFStore is a dict-like object, 
# so that we can directly write and read the data to the HDF5 store using key-value pairs.

# create a HDF5 store
store1 = pd.HDFStore('store1.h5')

# create data to be store in the HDF5 store
index = pd.date_range('1/1/2000', periods=8)
series_data =pd.Series(np.random.randn(5), index=index['a', 'b', 'c', 'd', 'e'])
data_df =pd.DataFrame(np.random.randn(8,3), index=index, columns=['A','B','C', 'D', 'E'])

# Writing the pandas data to the HDF5 store
store1['series'] = series_data
store1['data'] = data_df
# Reading the data from the HDF5 store
from_store = store1['series']
print(from_store)

# close the HDF5 store after use
store1.close()