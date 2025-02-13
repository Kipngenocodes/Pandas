import pandas as pd
# Removing Rows from a DataFrame using the .drop() method,
# removing rows based on conditions, and using index slicing.

# Dropping Rows using the drop() method
# create a dataframe
df = pd.DataFrame({ 'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3'],   
                   'D': ['D0', 'D1', 'D2', 'D3']})

print('Print the original DataFrame:')
print(df)
# Dropping Rows using the drop() method at index 3
results  = df.drop(3)
print('Dropping Rows using the drop() method at index 3:')
print(results)


# Dropping DataFrame Rows by Labels
# create a dataframe
df = pd.DataFrame({ 'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3'],
                   'D': ['D0', 'D1', 'D2', 'D3']
                   }, index=['r1', 'r2', 'r3', 'r4'])

# Displaying the original DataFrame
print('Print the original DataFrame:', df)
# Dropping Rows by Labels using the drop() method
results = df.drop(['r2', 'r4'])
print('Dropping Rows by Labels using the drop() method:')
print(results)


# removing the rows based on conditions
# create a dataframe
df = pd.DataFrame({ 'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                  'C': ['C0', 'C1', 'C2', 'C3'],
                  'D': ['D0', 'D1', 'D2', 'D3']}, index=[1, 2, 3, 4])

print("Original DataFrame:", df)

# removing rows based on conditions
# condition to remove rows where column 'A' is equal to 'A1'
results = df[(df['A'] != 'A1')]
print("Removing rows where column 'A' is equal to 'A1':")
print(results)

# remove rows using slicing of index

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8]})

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Drop the row using the index slicing
result = df.drop(df.index[2:4])

# Display the result
print("\nAfter dropping the row at 2 and 3:")
print(result)



