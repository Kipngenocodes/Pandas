import pandas as pd 
import numpy as np

# loading data
url = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv'

tips=pd.read_csv(url)
print(tips.head())


# outputing the first 5 rows of the data in pandas
# Output:
x = tips[['total_bill', 'tip', 'smoker', 'time']].head(2)
print(x)