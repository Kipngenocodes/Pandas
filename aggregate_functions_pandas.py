import pandas as pd
import numpy as np
'''
Aggregation Functions
Aggregation functions produce a single value from a series of data, 
providing a concise summary of your dataset. Here are some key aggregation functions −
Sr.No.	Methods & Description
1. mean()
Returns the mean of the values over the requested axis.
2.	sum()
Return the sum of the values over the requested axis.
3.	median()
Returns the Arithmetic median of values.
4.	min()
It return the minimum of the values over the requested axis.
5.	max()
Returns the maximum of the values over the requested axis.
6.	count()
Returns the number of non-NA/null observations in the given object.
7.	quantile()
Returns the value at the given quantile(s).
8.	mode()
Returns the mode(s) of each element along the selected axis/Series.
9.  var()
Return unbiased variance over requested axis.
10.	kurt()
Return unbiased kurtosis over requested axis.
11.	skew()
Return unbiased skew over requested axis.
12.	sem()
Return unbiased skew over requested axis.
13.	corr()
Compute correlation with other objects, excluding missing values.
14.	cov()
Computes the covariance between two objects, excluding NA/null values.
15.	autocorr()
Computes the lag-N autocorrelation.'''

# create series and dataframes
s = pd.Series([1, 2, 3, 4, 5])
df = pd.DataFrame({'A': [1, 2, 3, 4 ,5],
                   'B': [6, 7, 8, 9, 10],
                   'C': [11, 12, 13, 14, 15]})
df2= pd.DataFrame({'A': [10, 20, 30, 40, 50],
                   'B': [60, 70, 80, 90, 100],
                   'C': [110, 120, 130, 140, 150]}) 

print("Series: \n ", s)
print("\nDataFrame: \n", df)
print("\nDataFrame2: \n", df2)


# calculate the mean of the series
print("\nMean of the series: ", s.mean())

# calculate the mean of the dataframe
print("\nMean of the dataframe: \n", df.mean()) 
print('\n Mean of the dataframe2: \n', df2.mean())

# sum of the values of the series
print("\nSum of the series: ", s.sum())

# sum of the values over the requested axis
print("\nSum of the values over the requested axis: \n", df.sum(axis=0))

# calculating the median of the series
print("\nMedian of the series: ", s.median())
# calculating the median of the dataframe
print("\nMedian of the dataframe: \n", df.median())
# calculating the median of the dataframe2
print("\nMedian of the dataframe2: \n", df2.median())


# checking for min and max on the series
print("\nMin of the series: ", s.min())
print("\nMax of the series: ", s.max())
# checking for min and max on the dataframe
print("\nMin of the dataframe: \n", df.min())
print("\nMax of the dataframe: \n", df.max())
# checking for min and max on the dataframe2
print("\nMin of the dataframe2: \n", df2.min())
print("\nMax of the dataframe2: \n", df2.max())


# checking for the count of the series
print("\nCount of the series: ", s.count())
# checking for the count of the dataframe
print("\nCount of the dataframe: \n", df.count())
# checking for the count of the dataframe2
print("\nCount of the dataframe2: \n", df2.count())

# checking for quantile of the series
print("\nQuantile of the series: ", s.quantile(0.5))
# checking for quantile of the dataframe
print("\nQuantile of the dataframe: \n", df.quantile(0.5))
# checking for quantile of the dataframe2
print("\nQuantile of the dataframe2: \n", df2.quantile(0.5))

# checking for the kurtosis of the series
print("\nKurtosis of the series: ", s.kurtosis())
# checking for the kurtosis of the dataframe
print("\nKurtosis of the dataframe: \n", df.kurtosis())
# checking for the kurtosis of the dataframe2
print("\nKurtosis of the dataframe2: \n", df2.kurtosis())

# checking for the skewness of the series
print("\nSkewness of the series: ", s.skew())
# checking for the skewness of the dataframe
print("\nSkewness of the dataframe: \n", df.skew())
# checking for the skewness of the dataframe2
print("\nSkewness of the dataframe2: \n", df2.skew())

# claculate the sem of the series
print("\nSem of the series: ", s.sem())
# claculate the sem of the dataframe
print("\nSem of the dataframe: \n", df.sem())
# claculate the sem of the dataframe2
print("\nSem of the dataframe2: \n", df2.sem())
# claculate the std of the series
print("\nStd of the series: ", s.std())
