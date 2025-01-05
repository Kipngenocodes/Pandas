import pandas as pd
import numpy as np
'''
Method	Description
to_list()	Converts the Series into a Python list.
to_numpy()	Converts the Series into a NumPy array.
to_dict()	Converts the Series into a dictionary.
to_frame()	Converts the Series into a DataFrame.
to_string()	Converts the Series into a string representation for display.
'''

'''
        Converting Series to List
The Series.to_list() method converts a Pandas Series to a Python list,
where each element of the Series becomes an element of the returned list. 
And the type of each element in the list is types as those in the Series.'''
# Example
# create a series
s = pd.Series([1, 2, 3, 4, 5])

# convert the series to a list
list_s = s.to_list()
print(list_s)  # Output: [1, 2, 3, 4, 5]