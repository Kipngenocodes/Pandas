import pandas as pd

# Creating a dataframe 
df = pd.DataFrame([[1, 3], [5,37], [21, 31], [12, 45], [9, 11]], columns=['A', 'B'])

# Displaying the dataframe 
print(df)

# Creating a boolean index on a dataframe
df_bool_index = df >10

# output the boolean
print(df_bool_index)

# Filtering Data using the Boolean Index with .loc
s = (df['A'] > 2)

# Filter DataFrame using the Boolean Index with .loc
print('Output Filtered DataFrame:\n',df.loc[s, 'B'])