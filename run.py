import pandas as pd
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