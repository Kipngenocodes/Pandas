import pandas as pd
import numpy as np


'''
Boolean functions return boolean values based on logical operations across the Series −
1. all() :Returns True if all elements are True, potentially along an axis.
2.	any() : Returns True if any element is True, potentially along an axis.
3. between() :returns True for each element if it is between the left and right bounds.
'''

# create a series 
Series_data = pd.Series([1, 2, 3, 4, 5])
print("Original Series: \n", Series_data)
print("\n")
# create a dataframe
data_frame = pd.DataFrame({'A': [1, 2, 3, 4, 6],
                   'B': [12, 23,34, 75,96],
                   'C': [10, 20, 30, 40, 50]})

# returns True if all elements are true, potentially along the axis
print("all() function: \n", Series_data.all()) 
print("\n")
# returns True if any element is true, potentially along the axis on dataframe
print("any() function: \n", data_frame['A'].any())
print("\n")
# returns True if the element is between the left and right bounds
print("between() function: \n", Series_data.between(2, 4))  #
print("\n")

