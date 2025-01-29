import pandas as pd
import numpy as np

# create a dataframe with 5 columns and 5 rows with random data and missing values
df = pd.DataFrame(np.random.randint(0,100,size=(5, 5)), columns=list ('ABCDE'))
df.loc[1, 'B'] = np.nan
df.loc[2, 'C'] = np.nan
df.loc[3, 'D'] = np.nan
df.loc[4, 'E'] = np.nan

# Output the dataframe
print( df)

# Using the  interpolate() method
result = df.interpolate()
print(result)

'''
Different Interpolating Methods
Pandas supports several interpolation methods,
including linear, polynomial, pchip, akima, spline, and more. 
These methods provide flexibility for filling
the missing values depending on the nature of your data.
'''
# Using the  interpolate() method with different interpolation methods
result_linear = df.interpolate()
result_polynomial = df.interpolate(method='polynomial', order=2)    
result_pchip = df.interpolate(method='pchip')
result_akima = df.interpolate(method='akima')
result_spline = df.interpolate(method='spline', order=2)

# outputs 
print(result_spline)
print('\n')
print(result_linear)
print('\n')
print(result_akima)
print('\n')
print(result_polynomial)
print('\n')
print(result_pchip)

# Handling the limit in the interpolation method
result_linear = df.interpolate(limit_direction='both')
print(result_linear)

# Applying the interpolate() with limit
result = df.interpolate(method='spline', order=2, limit=1)

print("\nResultant DataFrame after applying the interpolation:")
print(result)
