import pandas as pd
import numpy as np

# creating a pandas series 
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], dtype= 'category')
print('\n Original series:\n ', series)

#Changing back to object type
series = series.astype('object')
print('\n Series after changing to object type:\n ', series)
