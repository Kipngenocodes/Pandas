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

    

