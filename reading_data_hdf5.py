import numpy as np
import pandas as pd

# reading data from the hdf5 files using the read_hdf() function
df = pd.read_hdf('data.h5', key='df')
# Outputing the data retrieved 
print(df)