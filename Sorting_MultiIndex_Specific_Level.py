import pandas as pd

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples([('C', 'one'), ('C', 'two'),('B', 'one'), ('B', 'two')],
                                  names= ['First Level', 'Second Level'])

# Create a DataFrame
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])

# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n',df)

# Sort MultiIndex by the first level
sorted_df = df.sort_index(level=0)
print("Resultant DataFrame:")
print(sorted_df)

# sorting mutlindex by level names
sorted_df = df.sort_index(level='level1')
print("Resultant DataFrame:")
print(sorted_df)

