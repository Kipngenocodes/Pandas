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


# Create a multiindex Object
multi_index = pd.MultiIndex.from_tuples([('A', 'Alex'), ('A', 'Amanda'), ('A', 'Billah'), ('A', 'Bilkan'),
                                  ('B', 'Alex'), ('B', 'Amanda'), ('B', 'Billah'), ('B', 'Bilkan'),
                                ('C', 'Alex'), ('C', 'Amanda'), ('C', 'Billah'), ('C', 'Bilkan')])

# Create a dataframe 
data =  {'Age': [25, 28, 30, 32, 25, 28 , 30, 32, 25, 28, 30, 32], 
         'Gender': [1, 1, 1, 1, 0, 0 , 0, 0, 0, 0, 0, 0]} 
df_dataframe = pd.DataFrame(data, index=multi_index)
print("\nOriginal MultiIndexed DataFrame:")
print(df_dataframe)

# Renaming the columns 
df_renamed  = df_dataframe.rename(columns={'X': "Year of Birth", 'Y': "BestNumber"})
print("\nDataFrame after renaming columns:")
print(df_renamed)
# Renaming the index levels
df_renamed_index = df_dataframe.rename_axis(index={'level_0': 'Category', 'level: 1': 'Name'},
                                            columns={'Age': "Age", 'Gender': "Gender"})
print("\nDataFrame after renaming index levels:")
print(df_renamed_index)
