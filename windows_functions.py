import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

'''
Rolling Window: A sliding window that can be fixed or variable in size.
Weighted Window: A non-rectangular, weighted window supplied by the scipy.signal library.
Expanding Window: An accumulating window that includes all data points up to the current one.
Exponentially Weighted Window: An accumulating window that 
applies exponential weighting to previous data points.'''


# Create a dataframe with random integers
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=['a', 'b', 'c', 'd'])

print('\n Original DataFrame: \n', df)

# showing a  rolling window of 3 rows
rolling_window = df.rolling(window=3).mean()

print ('\n Rolling Window of 3 rows: \n', rolling_window)


# working with weighted window
# create a series 
series = pd.Series(np.random.randint(0, 100, size=100))

# applying a weighted window to the series
result = series.rolling(window=5, win_type= 'triang').mean()
print('\n Weighted Window: \n', result)

# Expanding windows 
df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print(df.expanding(min_periods=3).mean())