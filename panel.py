'''
A panel is a 3D container of data.
The term Panel data is derived from econometrics and
is partially responsible for the name pandas − pan(el)-da(ta)-s.
it has be deprecated in pandas 0.25.0 and removed in pandas 0.25.0.'''
# panel data is generally 3D data.
'''
The names for the 3 axes are intended to give some semantic meaning to describing operations involving panel data. They are −
items: 
    axis 0, each item corresponds to a DataFrame contained inside.
    major_axis: axis 1, it is the index (rows) of each of the DataFrames.
    minor_axis: axis 2, it is the columns of each of the DataFrames.
'''
# How to create a panel
'''
# A Panel can be created using the following constructor −
# pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
'''
# Example of creating an empty panel from ndarrays
import pandas as pd
import numpy as np

data ={'item1': pd.DataFrame(np.random.randn(4, 3)),
       'item2': pd.DataFrame(np.random.randn(4, 2))}

p = pd.Panel(data)
print(p)
