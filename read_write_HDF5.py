import pandas as pd
import numpy as np
'''
pandas.read_hdf(): Read data from the HDFStore.
pandas.DataFrame.to_hdf() or pandas.Series.to_hdf(): 
Write Pandas object data to an HDF5 file using the HDFStore.'''

# Writing Pandas Data to HDF5 Using to_hdf()
'''
The to_hdf() function allows you to write pandas objects such 
as DataFrames and Series directly to an HDF5 file using the HDFStore.
This function provides various optional parameters like compression, handling missing values, 
format options, and more, allowing you to store your data efficiently.'''

# create a dataframe
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list ('ABCD'))
df.to_hdf('data.h5', key='df', mode='w', format='table')

# notification upon completion of the process
print("Dataframe has been successfully written to HDF5 file")