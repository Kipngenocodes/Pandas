import pandas as pd
import numpy as np

# Working with timedelta data
# Create a date range
start_date = '2020-01-01'
end_date = '2020-01-31'
date_range = pd.date_range(start=start_date, end=end_date)
print(date_range)

# working string 
date = '2 days 2 hours 15 minutes 30 seconds'
# Convert the string to a timedelta object
td = pd.to_timedelta(date)
print(td)

# Alternatively, you can use the unit parameter
td = pd.to_timedelta(6, unit='h')
print("\nTimedelta using unit parameter:")
print(td)
