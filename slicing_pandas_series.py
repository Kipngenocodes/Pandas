import pandas as pd 
import numpy as np
'''
Series slicing can be done by using the [:] operator, 
which allows you to select subset of elements from the series object by specified start and end points.
        Syntax for slicing a Series:
        Series[start:stop:step]
        start: This is the starting index of the slice. It is inclusive by default.
        stop: This is the ending index of the slice. It is exclusive by default.
        step: This is the increment between elements in the slice. It defaults to 1.
        Series[start:stop:step]: It selects elements from start to end with specified step value.

Series[start:stop]: It selects items from start to stop with step 1.

Series[start:]: It selects items from start to the rest of the object with step 1.

Series[:stop]: It selects the items from the beginning to stop with step 1.

Series[:]: It selects all elements from the series object.
'''

# slicing a pandas series by position
# Slicing range of values from a Series
series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original Series:")
print(series)
# Slicing a range of values from a Series
print("\nSlicing a range of values from a Series:")
print(series[2:8])  # Slicing from index 2 to 7
print(series[::2])  # Slicing every other element
print(series[1::2])  # Slicing every other element starting from index 1
print(series[:5])  # Slicing from the beginning to index 4
print(series[-5:])  # Slicing the last 5 elements
print(series[:-5])  # Slicing all elements except the last 5
print(series[:])  # Slicing all elements

'''Slicing a Series by Label
A Pandas Series is like a fixed-size Python dict in that you can get and set values by index labels.
'''
# Example retrieves multiple elements with slicing the label of a Series.
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

# Slice multiple elements
print(s['a':'d'])

'''
Modifying Values after Slicing
After slicing a Series, you can also modify the values, 
by assigning the new values to those sliced elements.
'''