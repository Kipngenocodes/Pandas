import pandas as pd
import numpy as np

# Create a pandas series with random values and a date index
my_series = pd.Series(np.random.random(20), index=pd.date_range('2022-01-01', periods=20))
print("Original Series:")
print(my_series)

# Set values from index 2 to index -2 (exclusive) to NaN
my_series[2:-2] = np.nan
print("\nSeries after setting values to NaN:")
print(my_series)

# Convert the series to a sparse series using SparseArray
my_sparse_series = pd.Series(pd.arrays.SparseArray(my_series))
print("\nSparse Series:")
print(my_sparse_series)