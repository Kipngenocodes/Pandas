import pandas as pd
import numpy as np

# Create and write an initial DataFrame to an HDF5 file
print("Creating initial DataFrame and writing to HDF5 file...")
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)).astype('int32'), columns=list('ABCD'))
df.to_hdf('data1.h5', key='df', mode='w', format='table')  # Save with 'w' mode to overwrite if exists
print("Initial DataFrame has been successfully written to HDF5 file.")

# Create a new DataFrame with a matching structure
print("\nCreating a new DataFrame to append...")
new_data = pd.DataFrame({'A': [1, 2, 3, 9], 
                         'B': [5, 6, 7, 11], 
                         'C': [21, 22, 23, 29], 
                         'D': [31, 32, 33, 39]}).astype('int32')  # Ensure matching dtype

# Append the new data to the HDF5 file
print("\nAppending the new DataFrame to the HDF5 file...")
new_data.to_hdf('data1.h5', key='df', mode='a', format='table', append=True)
print("Data appended to existing HDF5 file successfully.")

# Read back the data from the HDF5 file to verify
print("\nReading the data from the HDF5 file to verify...")
df_read = pd.read_hdf('data1.h5', key='df')
print("Data read from HDF5 file:\n", df_read)
