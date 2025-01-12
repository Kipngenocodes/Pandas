import pandas as pd
import numpy as np

'''
Cumulative functions provide running totals or products and maintain the same shape as the input data. These are useful in time series analysis or for understanding trends −
Sr.No.	Methods & Description
1	cumsum() :Return cumulative sum over a DataFrame or Series axis.
2	cumprod() : Return cumulative product over a DataFrame or Series axis.
3   cummax() :Return cumulative maximum over a DataFrame or Series axis.
4	cummin() :Return cumulative minimum over a DataFrame or Series axis.
'''
# create a series
s = pd.Series([1, 2, 3, 4, 5])
print("Original Series:")

# create a pandas dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [6, 7, 8, 9, 10],
                   'C': [11, 12, 13, 14, 15],
                   'D': [16, 17, 18, 19, 20]})

# create a cumulative sum of the series
print("\n Cumulative Sum of Series: ", s.cumsum())
print("\n Cumulative Sum of DataFrame: ", df.cumsum())

# create a cumulative product of the series
print("\n Cumulative Product of Series: ", s.cumprod())
print("\n Cumulative Product of Dataframe: ", df.cumprod())

# create a cumulative max of the series
print("\n Cumulative Max of Series: ", s.cummax())
print("\n Cumulative Max of DataFrame: ", df.cummax())

# create a cumulative min of the series
print("\n Cumulative Min of Series: ", s.cummin())
print("\n Cumulative Min of DataFrame: ", df.cummin())
