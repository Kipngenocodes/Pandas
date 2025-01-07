
import pandas as pd
import numpy as np
'''
The Pandas I/O API is a set of top level reader functions accessed like pd.read_csv() 
that generally return a Pandas object.
The two workhorse functions for reading text files (or the flat files) are read_csv() and read_table().
They both use the same parsing code to intelligently convert tabular data into a DataFrame object −

pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',
names=None, index_col=None, usecols=None)
or
pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',
names=None, index_col=None, usecols=None)
'''
# using the  read_csv function to read a csv file
df = pd.read_csv('employee_data.csv')
print(df)

#converting the data into a DataFrame object
df = pd.read_csv("employee_data.csv", dtype={'Salary': np.float64})
print (df.dtypes)
