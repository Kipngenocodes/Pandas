import pandas as pd
import numpy as np

'''
Missing data is always a problem in real life scenarios.
particularly in areas like machine learning and data analysis.

Pandas uses different sentinel values to represent missing data (NA or NaN), depending on the data type.
numpy.nan: Used for NumPy data types. When missing values are introduced in an integer or boolean array,
the array is upcast to np.float64 or object, as NaN is a floating-point value.
NaT: Used for missing dates and times in np.datetime64, np.timedelta64, and PeriodDtype.
NaT stands for "Not a Time".
<NA>: A more flexible missing value representation for 
StringDtype, Int64Dtype, Float64Dtype, BooleanDtype, and ArrowDtype. 
This type preserves the original data type when missing values are introduced.'''

# Representation of Missing Data
ser1 = pd.Series([1, 2], dtype=np.int64).reindex([0, 1, 2])
ser2 = pd.Series([1, 2], dtype=np.dtype("datetime64[ns]")).reindex([0, 1, 2])
ser3 = pd.Series([1, 2], dtype="Int64").reindex([0, 1, 2])

df = pd.DataFrame({'NumPy':ser1, 'Dates':ser2, 'Others':ser3} )
print(df)


# Checking for missing Data Values 
''''
Pandas provides the isna() and notna() functions to detect missing values,
which work across different data types.
These functions return a Boolean Series indicating the presence of missing values.'''

series  = pd.Series([pd.Timestamp("2023-12-12"), pd.NaT])
print(series.isna())  # Output: [False, True]

