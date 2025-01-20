import pandas as pd

'''
In Pandas, MultiIndex or hierarchical indexing allows 
you to work with data structures that have multiple
levels of indexing for rows and columns. 
When dealing with these type of structured datasets, 
advanced reindexing with MultiIndex becomes essential 
for reshaping and aligning data across different levels.

Advanced reindexing and alignment in MultiIndex DataFrames
enables flexible data manipulation and reshaping in Pandas.
By using methods like reindex(), swaplevel(), and reorder_levels() 
you can easily perform the data manipulation and restructuring tasks in Pandas.'''

# Reindexing DataFrame with MultiIndex
index = pd.MultiIndex.from_tuples([ ("A", "One"), ("A", "Two"), ("B", "One"), ("B ", "One") ],
                                  names=["Main", "Section"])

data = {'Value1': [1, 2, 3, 4], 'Value2': [5, 6, 7, 8]} 
df = pd.DataFrame(data,  index= index, columns= ['Value1', 'Value2'])
print(df)

# New Index for reindexing 
new_index = ([ ("A", "One"), ("A", "Queen"), ('foo', 'Two'), ("B", "King"), ("B", "Queen")])

# reindexing the dataframe
df_reindexed = df.reindex(new_index)

# output
print('\nReindexed DataFrame:\n', df_reindexed )