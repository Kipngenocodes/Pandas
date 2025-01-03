'''
A Series is a one-dimensional labeled array that can hold any data type. 
It can store integers, strings, floating-point numbers, etc. 
Each value in a Series is associated with a label (index), which can be an integer or a string.
'''

# Example of creating a Series
import pandas as pd
data = ['Kipngeno', '35', 'Male', 'Kenya', 'Nairobi', 'Engineer']
series = pd.Series(data, index=['Name', 'Age', 'Gender', 'Country', 'City', 'Profession'])
print(series)


# DataFrames are two-dimensional data structures with columns of potentially different types.
#  It is similar to a table in a database or a spreadsheet.
# example 

data = {'Name': ['Kipngeno', 'Kipkoech', 'Kiprotich', 'Kipchumba'],
        'Age': [35, 30, 40, 45],
        'Gender': ['Male', 'Male', 'Male', 'Male'],
        'Country': ['Kenya', 'South Africa', 'Uganda', 'Tanzania'],
        'Profession': ['Engineer', 'Doctor', 'Teacher', 'Lawyer'],
        'City': ['Nairobi', 'Cape Town', 'Kampala', 'Dodoma'],
        'Salary': [1000, 2000, 1500, 3000],
        'Bonus': [500, 1000, 750, 1500],
        'marital_status': ['Married', 'Single', 'Married', 'Single']}
# creating a DataFrame
df = pd.DataFrame(data)
# output the DataFrame
print(df)

# purpose of dat
# DataFrames are used for data manipulation and analysis. 
# They can be used to store and manipulate large datasets in a tabular format.
# DataFrames can be used to perform various operations such as filtering, sorting, grouping, merging, and joining data.
# DataFrames can also be used to perform statistical analysis, data visualization, and data mining.
# DataFrames can be used to store and manipulate data from various sources such as databases, CSV files, Excel files, and JSON files.
# DataFrames are widely used in data science, machine learning, and other fields that require data analysis and manipulation.
# DataFrames are also used in data visualization tools such as Matplotlib and Seaborn to creat
# DataFrames are used to store and manipulate data in a structured way.
# DataFrames are used to perform various operations such as filtering, sorting, grouping, merging, and joining data.
# DataFrames are used to perform statistical analysis, data visualization, and data mining.

#Example of creating a series from dataframes
# creating a DataFrame
data = {'Name': ['Kipngeno', 'Kipkoech', 'Kiprotich', 'Kipchumba'],
        'Age': [35, 30, 40, 45],
        'Gender': ['Male', 'Male', 'Male', 'Male'],
        'Country': ['Kenya', 'South Africa', 'Uganda', 'Tanzania'],
        'Profession': ['Engineer', 'Doctor', 'Teacher', 'Lawyer'],
        'City': ['Nairobi', 'Cape Town', 'Kampala', 'Dodoma'],
        'Salary': [1000, 2000, 1500, 3000],
        'Bonus': [500, 1000, 750, 1500],
        'marital_status': ['Married', 'Single', 'Married', 'Single']
        }
# Displaying the series from the DataFrame
print(df['Name'])