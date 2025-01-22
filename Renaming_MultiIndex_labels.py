import pandas as pd

'''
It involves the renaming specific labels, axis names, 
or index levels of the MultiIndexed objects. 
Pandas provides flexible methods like rename(), rename_axis(),
and set_names() to handle these tasks efficiently, whether you want to rename specific labels, 
change the names of the index or column axes,
or update the entire hierarchy of index levels, these methods are useful.
'''

# Renaming specific labels
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 7], 'C': [7, 8, 9]})
print("Original DataFrame:")
print(df)

new_df = df.rename(columns={'A': 'X', 'B': 'Y', 'C':'H'})
print("\nDataFrame after renaming columns:")
print(new_df)


# renaming the specific labels
index = pd.MultiIndex.from_tuples([('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')])

# Create a dataframe with the MultiIndex
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=index)
print("\nOriginal DataFrame:", df)

# Renaming specific labels
df = df.rename(index={'A': 'X', 'B': 'Y', 'C':'H', 'D':'I'})
print("\nDataFrame after renaming index labels:")
print(df)