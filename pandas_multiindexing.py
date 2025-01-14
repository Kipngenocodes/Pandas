import pandas as pd
import numpy as np

'''
 powerful feature in pandas that allows you to work with
 higher-dimensional data in lower-dimensional structures like Series (1D) and DataFrame (2D). '''
 
#  create a MultiIndex object in pandas, including from lists of arrays, tuples, products of iterables, 
# or directly from a DataFrame
'''
MultiIndex.from_arrays()
MultiIndex.from_product()
MultiIndex.from_tuples()
MultiIndex.from_frame()'''

# Creating MultiIndex from Lists of Arrays
list_of_arrays = [['Kipngeno', 'Samuel', 'Robert',  'Fancy', 'Gina', 'Monalisa'],
                  ['a', 'b', 'c', 'd', 'e', 'f']]

# create a multiindex from the list of arrays
multi_index = pd.MultiIndex.from_arrays(list_of_arrays, names =['Name', 'Letter'])
