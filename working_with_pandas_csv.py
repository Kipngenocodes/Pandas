import pandas as pd

# Import StringIO to load a file-like object for reading CSV
from io import StringIO
'''
The pandas.read_csv() function is used to read the CSV format file into the Pandas DataFrame or TextFileReader. 
This function accepts a URL or a local file path to load the data into the Pandas environment.'''

# Create string representing CSV data
data = """Name,Gender,Age
Braund,male,22
Cumings,female,38
Heikkinen,female,26
Futrelle,female,35"""

# Use StringIO to convert the string data into a file-like object
obj = StringIO(data)

# read CSV into a Pandas DataFrame
df = pd.read_csv(obj)

print(df)