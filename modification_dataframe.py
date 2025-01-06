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

# adding or insering a New Column to a DataFrame
# Doing it directly by assigning a new column label and values to the DataFrame
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
# add a new column to the DataFrame
df['City of Birth'] = ['San Diego', 'Pocattello', 'Boston']
# print the modified DataFrame
print("\nDataFrame after adding a new column:")
print(df)

# Inserting a New Column at a Specific Position
# create a DataFrame
new_data = {'firt_name': ['John', 'Jane', 'Mary'],
            'last_name': ['Doe', 'Smith', 'Johnson'],
            'age': [34, 29, 42],
            'city': ['Chicago', 'Los Angeles', 'New York'],
            'Marital Status': ['Single', 'Married', 'Divorced'],
            'City of Birth': ['San Diego', 'Pocattello', 'Boston'],
            'Occupation': ['Engineer', 'Nurse', 'Doctor']}  
new_df = pd.DataFrame(new_data, index=['A', 'B', 'C'])
print("Original DataFrame:")
print(new_df)
# Insert a new column at a specific position
new_df.insert(3, 'Country', ['Denmark', 'China', 'Canada'])
# print the modified DataFrame
print("\nDataFrame after inserting a new column:")
print(new_df)


# replacing the Contents of a Column in a dataframe
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
# replace the contents of a column
df['city'] = ['San Diego', 'Pocatello', 'Boston']
# print the modified DataFrame
print("\nDataFrame after replacing the contents of a column:")
print(df)
