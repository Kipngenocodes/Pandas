import pandas as pd

'''
JSON (JavaScript Object Notation) is a lightweight data interchange 
format that can be easily read and written by humans. 
JSON is widely used for transmitting data between a server and a web application.
'''

# File path of the JSON file
json_file_path = r'C:\Users\p1\OneDrive\Desktop\Pandas\employee_data.json'

# Read the JSON file into a pandas DataFrame
df = pd.read_json(json_file_path)

# Display the DataFrame
print(df)

