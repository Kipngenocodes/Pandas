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
print(type(list_s))  # Output: <class 'list'>

'''
Convert Series to NumPy Array'''
# Example
# create a series
s = pd.Series(['Bucharest', 'Tallin', 'Budapest', 'Gorigia', 'Helsinki'])
# convert the series to a numpy array
array_s = s.to_numpy()
print(array_s)  # Output: ['Bucharest' 'Tallin' 'Budapest' 'Gorigia' 'Helsinki']
print(type(array_s))  # Output: <class 'numpy.ndarray'>

'''
Convert Series to Dictionary'''
# Example
# create a series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# convert the series to a dictionary
dict_s = s.to_dict()
print(dict_s)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(type(dict_s))  # Output: <class 'dict'>

'''
Convert Series to DataFrame'''
# Example
# create a series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# convert the series to a DataFrame
df = s.to_frame()
print(df)
print(type(df))

'''
Convert Series to String'''
# Example
# create a series
s = pd.Series(['Bucharest', 'Tallin', 'Budapest', 'Goriga', 'Helsinki'])
# convert the series to a string
string_s = s.to_string()
print(string_s)
print(type(string_s))

