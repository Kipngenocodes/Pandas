import pandas as pd
'''
 Modifying a Pandas DataFrame is an essential task for data manipulation and preprocessing.
  The common modifications includes renaming column or row labels, 
  adding or inserting new columns for additional data, updating or 
  replacing the contents of existing columns, and removing unnecessary columns.
  '''
# Renaming Column or Row Labels of a DataFrame - aims to increas the readability of the data
# example of renaming column labels of a DataFrame
# create a DataFrame
df = pd.DataFrame({'firt_name': ['John', 'Jane', 'Mary'],
                   'last_name': ['Doe', 'Smith', 'Johnson'],
                   'age': [34, 29, 42],
                   'city': ['Chicago', 'Los Angeles', 'New York'],
                   'Marital Status': ['Single', 'Married', 'Divorced']},
                  index=['A', 'B', 'C'])

# print the original DataFrame
print("Original DataFrame:")
print(df)

# rename the column labels
df =df.rename(columns={'firt_name': 'First Name', 'last_name': 'Last Name'}, inplace=True)
# print the modified DataFrame
print("\nDataFrame after renaming columns:")
print(df)

# Renaming Row Labels of a DataFrame
# example of renaming row labels of a DataFrame
# create a DataFrame
df = pd.DataFrame({'firt_name': ['John', 'Jane', 'Mary'],
                   'last_name': ['Doe', 'Smith', 'Johnson'],
                   'age': [34, 29, 42],
                   'city': ['Chicago', 'Los Angeles', 'New York'],
                   'Marital Status': ['Single', 'Married', 'Divorced']},
                  index=['A', 'B', 'C'])

# print the original DataFrame
print("Original DataFrame:")
print(df)
# rename the row labels
df = df.rename(index={'A': 'Person 1', 'B': 'Person 2', 'C': 'Person 3'}, inplace=True)
# print the modified DataFrame
print("\nDataFrame after renaming rows:")
print(df)