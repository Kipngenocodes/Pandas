import pandas as pd 
'''
Excel files using the pandas.read_excel() method,
covering different scenarios like loading a single sheet,
specific sheets, and multiple sheets.'''

data = r'C:\Users\p1\OneDrive\Desktop\Pandas\employee_data.xlsx'

# reading the excel file
df = pd.read_excel(data)

print("Dataframe:")
print(df)

