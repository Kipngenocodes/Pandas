import pandas as pd
import numpy as np

'''
Covariance measures how two variables change together.
In Pandas, the cov() method computes the covariance
between two Series objects or across all pairs of columns in a DataFrame.
'''

# create two pandas series with random data
series1 = pd.Series(np.random.randn(100))
series2 = pd.Series(np.random.randn(100))

# output
print("Series 1: ", series1.head())

print(series1.cov(series2))