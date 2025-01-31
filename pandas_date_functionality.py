import pandas as pd
import numpy as np

# Working with date functionality in pandas
# Create a date range 
date_range = pd.date_range('2022-01-01', periods=10, freq=' D')
print(date_range)

# Changing date frequency 
date_range = pd.date_range('2022-01-01', periods=10, freq='ME')
print(date_range)

# bdate_range() stands for business date ranges. Unlike date_range(), it excludes Saturday and Sunday.
date_range = pd.bdate_range('2022-01-01', periods=10)
print(date_range)