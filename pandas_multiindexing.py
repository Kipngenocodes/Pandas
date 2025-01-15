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

# create a multiindex series 
series = pd.Series(np.random.randint(0, 100, 6), index = multi_index)

print('\n the series is \n', series)

print('\n')

# creation of the multiindexing from tuples
tuple_list = [('Kipngeno', 'a'), ('Samuel', 'b'), ('Robert', 'c'), ('Fancy', 'd'),  ('Sammy', 'K')]

# create a multiindex from the tuple list
multi_index = pd.MultiIndex.from_tuples(tuple_list, names = ['Name', 'Letter'])
# create a multiindex dataframe
df = pd.DataFrame(np.random.randint(0, 100, (5, 2)), index = multi_index, columns = ['Score1', 'Score2'])
print('\n the dataframe is \n', df)



# Create a multiindex from the product of iterables
iterables = [['a', 'b', 'c'], [1, 2, 3], ['Green', 'Red', 'Yellow']]
multi_index = pd.MultiIndex.from_product(iterables, names=['Letter', 'Number', 'Colors'])

# Create a DataFrame from the multiindex
df = pd.DataFrame(np.random.randn(27, 3), index=multi_index, columns=["A", "B", "C"])

# Output the DataFrame
print('\nThe DataFrame is:\n', df)