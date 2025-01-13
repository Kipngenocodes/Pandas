import pandas as pd
import numpy as np

'''
Pandas has full-featured, high performance in-memory 
join operations idiomatically very similar to relational databases like SQL.
Pandas provides a single function, merge, 
as the entry point for all standard database join operations between DataFrame objects −
'''
'''
syntax: pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)
'''

# create two dataframes to be used in the merge operation
left_dataframe = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right_dataframe = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

# output the original dataframes
print("Original Left DataFrame: \n", left_dataframe)
print("\nOriginal Right DataFrame: \n", right_dataframe)

# merging the two dataframes on 'id' column
r= pd.merge(left_dataframe, right_dataframe, on='id')
print("\nMerged DataFrame: \n", r)