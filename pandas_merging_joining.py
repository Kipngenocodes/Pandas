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

# Merge Using 'how' Argument
'''The how argument to merge specifies how to determine which 
keys are to be included in the resulting table. If a key combination
does not appear in either the left or the right tables, 
the values in the joined table will be NA.

left	LEFT OUTER JOIN	- Use keys from left object
right	RIGHT OUTER JOIN - Use keys from right object
outer	FULL OUTER JOIN	 - Use union of keys from both objects
inner	INNER JOIN	- Use intersection of keys'''

# using 'left' argument to perform left outer join
left_outer_join = pd.merge(left_dataframe, right_dataframe, how='left', on='id')

# using 'right' argument to perform right outer join
right_outer_join = pd.merge(left_dataframe, right_dataframe, how='right', on='id')
# using 'outer' argument to perform full outer join
full_outer_join = pd.merge(left_dataframe, right_dataframe, how='outer', on='id')
# using 'inner' argument to perform inner join
inner_join = pd.merge(left_dataframe, right_dataframe, how='inner', on='id')

print("\nLeft Outer Join: \n", left_outer_join)
print("\nRight Outer Join: \n", right_outer_join)
print("\nFull Outer Join: \n", full_outer_join)
print("\nInner Join: \n", inner_join)
