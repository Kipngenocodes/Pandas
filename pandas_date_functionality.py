import pandas as pd
import numpy as np

# Working with date functionality in pandas
# Create a date range 
date_range = pd.date_range('2022-01-01', periods=10, freq=' D')
print(date_range)