import pandas as pd

# Read tables from a SQL tutorial
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
tables = pd.read_html(url)

# Access the first table from the URL
df = tables[0]

# Display the resultant DataFrame
print('Output First DataFrame:', df.head())