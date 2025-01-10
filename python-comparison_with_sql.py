import pandas as pd 
import numpy as np

# loading data
url = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv'

tips=pd.read_csv(url)
print(tips.head())

print('/n')
# outputing the first 5 rows of the data in pandas
# Output:
x = tips[['total_bill', 'tip', 'smoker', 'time']].head(2)
print(x)
print('/n')

# filtering rows
y = tips[tips['time'] == 'Dinner'].head(5)
print(y)
print('/n')

p= tips[tips['size'] > 2].head(5)
print(p)

#print('/n')
# Grouping data
g = tips.groupby('sex').size()
print(g)