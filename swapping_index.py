import pandas as pd

# creating a multi-index object
index= pd.MultiIndex.from_tuples([('A', 'One'), ('A', 'Two'),  ('A', 'Three'),
                                  ('B', 'One'), ('B', 'Three'), ('B', 'Two')]) 
# Create a dataframe
data = [[1, 2], [3, 4], [1, 1], [5, 6], [7, 8], [2, 2]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])


# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n',df)

# Swap the levels of the original DataFrame
swapped_df = df.swaplevel(0, 1, axis=0)

print('\nDataFrame After Swapping Levels:\n', swapped_df)